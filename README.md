# Kelime zamanlaması

Elle yazılmış örnek zaman kodlarıyla konuşma altyazısını vurgula.

## Çalıştırma

`index.html` dosyasını bir tarayıcıda aç. Oynat düğmesini ve zaman çizelgesini kullanarak sekiz saniyelik sahneyi incele. HTML ve Canvas 2D ile çevrimdışı çalışır.

## İlham kaynağı

Bu bağımsız sahne sentetik su istasyonu örnekleri kullanır. [Kaynak proje](https://github.com/m-bain/whisperX).

## Kelime zamanlı altyazı

Python 3 ile mevcut WhisperX hizalama JSON dosyasını WebVTT altyazıya çevir. Sesten üretim için WhisperX CLI, FFmpeg ve model indirmesi gerekir. CPU ve CUDA seçilebilir. Tarayıcı animasyonu sabit bir örnektir.

```sh
python captions.py --json aligned.json -o captions.vtt
python captions.py --audio input.wav --language tr --device cpu -o captions.vtt
```

Sekiz saniyelik zaman çizelgesinden bir kare seçip **PNG indir** ile 720 × 405 piksel dışa aktarabilirsin.
