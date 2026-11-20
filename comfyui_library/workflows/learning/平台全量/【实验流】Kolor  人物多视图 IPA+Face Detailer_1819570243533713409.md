---
key: 平台全量/【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409.json
name: 【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409.json
hash: 9a1f17f71e6cffa2
coverage: 0.781818
learned_at: 2026-11-14 01:24:03
nodes: [MZ_ChatGLM3_V2, Reroute, ControlNetLoader, MZ_KolorsControlNetPatch, ControlNetApply, MiDaS-NormalMapPreprocessor, PreviewImage, ControlNetLoader, MZ_KolorsControlNetPatch, ControlNetApply, AIO_Preprocessor, PreviewImage, ControlNetLoader, MZ_KolorsControlNetPatch, ControlNetApply, AIO_Preprocessor, PreviewImage, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, KSampler, VAEDecode, VAELoader, SaveImage, CLIPTextEncode, UltralyticsDetectorProvider, CLIPTextEncode, MZ_KolorsUNETLoaderV2, MZ_ChatGLM3Loader, WD14Tagger|pysssss, EmptyLatentImage, ImageResize+, MZ_IPAdapterAdvancedKolors, LoadImage, PatchModelAddDownscale, PreviewImage, PreviewImage, ImageUpscaleWithModelBatched, UpscaleModelLoader, TextCombinerTwo, JjkText, MZ_ChatGLM3_V2, ShowText|pysssss, Translate2Chinese|fofo, DownloadAndLoadFlorence2Model, ShowText|pysssss, Florence2Run, ShowText|pysssss, Translate2Chinese|fofo, ShowText|pysssss, WD14Tagger|pysssss, LoadImage, SAMLoader, CheckpointLoaderSimple, FaceDetailer, PreviewImage]
patterns: [text_to_image, controlnet]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1248, "sampler_name": "dpmpp_sde", "scheduler": "sgm_uniform", "seed": 1124765694289151, "steps": 25, "width": 1024}
---

# 平台全量/【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409.json

> 来源文件 `comfyui_library/workflows/平台全量/【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `MZ_ChatGLM3_V2`
- `Reroute`
- `ControlNetLoader`
- `MZ_KolorsControlNetPatch`
- `ControlNetApply` ★核心
- `MiDaS-NormalMapPreprocessor`
- `PreviewImage`
- `ControlNetLoader`
- `MZ_KolorsControlNetPatch`
- `ControlNetApply` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetLoader`
- `MZ_KolorsControlNetPatch`
- `ControlNetApply` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_KolorsCLIPVisionLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `CLIPTextEncode` ★核心
- `MZ_KolorsUNETLoaderV2` ★核心
- `MZ_ChatGLM3Loader`
- `WD14Tagger|pysssss`
- `EmptyLatentImage` ★核心
- `ImageResize+`
- `MZ_IPAdapterAdvancedKolors`
- `LoadImage`
- `PatchModelAddDownscale`
- `PreviewImage`
- `PreviewImage`
- `ImageUpscaleWithModelBatched`
- `UpscaleModelLoader`
- `TextCombinerTwo`
- `JjkText`
- `MZ_ChatGLM3_V2`
- `ShowText|pysssss`
- `Translate2Chinese|fofo`
- `DownloadAndLoadFlorence2Model`
- `ShowText|pysssss`
- `Florence2Run`
- `ShowText|pysssss`
- `Translate2Chinese|fofo`
- `ShowText|pysssss`
- `WD14Tagger|pysssss`
- `LoadImage`
- `SAMLoader`
- `CheckpointLoaderSimple` ★核心
- `FaceDetailer`
- `PreviewImage`

**识别到的模式**：text_to_image、controlnet

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `1124765694289151`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1248`
- `batch_size` = `1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **78%**（43/55）

**有卡**：`MZ_ChatGLM3_V2`、`ControlNetLoader`、`MZ_KolorsControlNetPatch`、`ControlNetApply`、`MiDaS-NormalMapPreprocessor`、`AIO_Preprocessor`、`MZ_IPAdapterModelLoaderKolors`、`MZ_KolorsCLIPVisionLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`SaveImage`、`CLIPTextEncode`、`UltralyticsDetectorProvider`、`MZ_KolorsUNETLoaderV2`、`MZ_ChatGLM3Loader`、`WD14Tagger|pysssss`、`EmptyLatentImage`、`ImageResize+`、`MZ_IPAdapterAdvancedKolors`、`LoadImage`、`PatchModelAddDownscale`、`ImageUpscaleWithModelBatched`、`UpscaleModelLoader`、`TextCombinerTwo`、`Translate2Chinese|fofo`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`SAMLoader`、`CheckpointLoaderSimple`、`FaceDetailer`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApply
