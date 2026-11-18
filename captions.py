"""Convert aligned speech to one WebVTT cue per timed word."""
import argparse
import json
import math
import shutil
import subprocess
import tempfile
from html import escape
from pathlib import Path


def timestamp(total_ms):
    hours, remaining = divmod(total_ms, 3_600_000)
    minutes, remaining = divmod(remaining, 60_000)
    seconds, millis = divmod(remaining, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"


def render(data):
    words = data.get("word_segments") or [
        word for segment in data.get("segments", []) for word in segment.get("words", [])
    ]
    cues = []
    for item in words:
        start, end = item.get("start"), item.get("end")
        word = " ".join(str(item.get("word", "")).split())
        if not word or not all(isinstance(x, (int, float)) and math.isfinite(x)
                               for x in (start, end)):
            continue
        if start < 0 or end <= start:
            continue
        first = round(start * 1000)
        last = max(first + 1, round(end * 1000))
        cues.append((first, last, word))
    if not cues:
        raise ValueError("No aligned words with valid timestamps were found.")
    return "WEBVTT\n\n" + "\n\n".join(
        f"{timestamp(start)} --> {timestamp(end)}\n{escape(word, quote=False)}"
        for start, end, word in sorted(cues)
    ) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--json", type=Path, help="Existing WhisperX alignment JSON")
    inputs.add_argument("--audio", type=Path, help="Local audio or video to transcribe")
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--model", default="small")
    parser.add_argument("--device", choices=["cpu", "cuda"], default="cpu")
    parser.add_argument("--language", default=None)
    args = parser.parse_args()
    try:
        if args.json:
            data = json.loads(args.json.read_text(encoding="utf-8"))
        else:
            binary = shutil.which("whisperx")
            if not binary:
                parser.error("Install WhisperX or pass an existing alignment with --json.")
            with tempfile.TemporaryDirectory() as output_dir:
                command = [binary, str(args.audio.resolve(strict=True)), "--model", args.model,
                           "--device", args.device, "--compute_type",
                           "int8" if args.device == "cpu" else "float16",
                           "--output_format", "json", "--output_dir", output_dir]
                if args.language:
                    command += ["--language", args.language]
                subprocess.run(command, check=True)
                result = Path(output_dir) / (args.audio.stem + ".json")
                data = json.loads(result.read_text(encoding="utf-8"))
        args.output.write_text(render(data), encoding="utf-8")
    except (OSError, ValueError, TypeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
