# Timed Water Captions / Kelime zamanlaması

## Türkçe

[Canlı aracı aç](https://omerbek.github.io/timed-water-captions/).

Elle yazılmış örnek zaman kodlarıyla konuşma altyazısını vurgula.

## Çalıştırma

`index.html` dosyasını bir tarayıcıda aç. Oynat düğmesini ve zaman çizelgesini kullanarak sekiz saniyelik sahneyi incele. HTML ve Canvas 2D ile çevrimdışı çalışır.


## Kelime zamanlı altyazı

Python 3 ile mevcut WhisperX hizalama JSON dosyasını WebVTT altyazıya çevir. Sesten üretim için WhisperX CLI, FFmpeg ve model indirmesi gerekir. CPU ve CUDA seçilebilir. Tarayıcı animasyonu sabit bir örnektir.

```sh
python captions.py --json aligned.json -o captions.vtt
python captions.py --audio input.wav --language tr --device cpu -o captions.vtt
```

Sekiz saniyelik zaman çizelgesinden bir kare seçip **PNG indir** ile 720 × 405 piksel dışa aktarabilirsin.

## English

Generate word-timed WebVTT captions from alignment data or local media.

Open [the live tool](https://omerbek.github.io/timed-water-captions/) or open `index.html` in a browser. Switch between Turkish and English in the page header. Use the timeline to select a frame and **Download PNG** to save it at 720 × 405 pixels.

### Command line

Requires Python 3. Converting alignment JSON works directly. Creating alignment from audio also requires WhisperX, FFmpeg and the speech models.

```sh
python captions.py --json aligned.json -o captions.vtt
python captions.py --audio input.wav --language tr --device cpu -o captions.vtt
```
