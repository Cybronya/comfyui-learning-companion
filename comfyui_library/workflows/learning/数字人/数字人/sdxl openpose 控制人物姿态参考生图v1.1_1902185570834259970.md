---
key: 数字人/数字人/sdxl openpose 控制人物姿态参考生图v1.1_1902185570834259970.json
name: sdxl openpose 控制人物姿态参考生图v1.1_1902185570834259970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/sdxl openpose 控制人物姿态参考生图v1.1_1902185570834259970.json
hash: 88fe8bd1524016b8
coverage: 0.7
learned_at: 2026-10-26 01:59:19
nodes: [VAEDecode, SetUnionControlNetType, Anything Everywhere, IPAdapterAdvanced, ImageUpscaleWithModel, ImageScaleBy, VAEEncode, Reroute, Reroute, Reroute, SaveImage, Reroute, RembgByBiRefNet, SetUnionControlNetType, Reroute, PreviewImage, VAEDecode, FaceDetailer, CLIPTextEncode, Reroute, Joy_caption_two_load, PreviewImage, AIO_Preprocessor, SaveImage, SaveImage, ShowText|pysssss, LoraLoader, LoadImage, LoraLoader|pysssss, easy cleanGpuUsed, String, KSampler, KSampler, ControlNetApplySD3, ControlNetApplySD3, EmptyLatentImage, PreviewImage, ImageResize+, Joy_caption_two, IPAdapterUnifiedLoader, Anything Everywhere, CLIPTextEncode, ETN_Translate, ShowText|pysssss, LoadRembgByBiRefNetModel, PreviewImage, Fast Groups Muter (rgthree), Note, Reroute, UpscaleModelLoader, UltralyticsDetectorProvider, SAMLoader, CheckpointLoaderSimple, LoadImage, AIO_Preprocessor, ControlNetLoader, ControlNetLoader, DWPreprocessor, LoadImage, PreviewImage]
patterns: [text_to_image, image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 3, "checkpoint": "DreamShaper XL v2.1 Turbo 闪电.safetensors", "controlnet_strength": 0.8, "denoise": 1, "height": 1024, "lora_name": "None", "sampler_name": "dpmpp_sde_gpu", "scheduler": "karras", "seed": 1110510183360042, "steps": 30, "strength_clip": 0.8, "strength_model": 0.8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/sdxl openpose 控制人物姿态参考生图v1.1_1902185570834259970.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/sdxl openpose 控制人物姿态参考生图v1.1_1902185570834259970.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `VAEDecode` ★核心
- `SetUnionControlNetType`
- `Anything Everywhere`
- `IPAdapterAdvanced`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `SaveImage`
- `Reroute`
- `RembgByBiRefNet`
- `SetUnionControlNetType`
- `Reroute`
- `PreviewImage`
- `VAEDecode` ★核心
- `FaceDetailer`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Joy_caption_two_load`
- `PreviewImage`
- `AIO_Preprocessor`
- `SaveImage`
- `SaveImage`
- `ShowText|pysssss`
- `LoraLoader` ★核心
- `LoadImage`
- `LoraLoader|pysssss` ★核心
- `easy cleanGpuUsed`
- `String`
- `KSampler` ★核心
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `ImageResize+`
- `Joy_caption_two`
- `IPAdapterUnifiedLoader`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `ETN_Translate`
- `ShowText|pysssss`
- `LoadRembgByBiRefNetModel`
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `Note`
- `Reroute`
- `UpscaleModelLoader`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `ControlNetLoader`
- `DWPreprocessor`
- `LoadImage`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `lora_name` = `None`
- `strength_model` = `0.8`
- `strength_clip` = `0.8`
- `seed` = `1110510183360042`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `dpmpp_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `0.8`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `4`
- `checkpoint` = `DreamShaper XL v2.1 Turbo 闪电.safetensors`

## 知识

覆盖率 **70%**（42/60）

**有卡**：`VAEDecode`、`SetUnionControlNetType`、`IPAdapterAdvanced`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEEncode`、`SaveImage`、`RembgByBiRefNet`、`FaceDetailer`、`CLIPTextEncode`、`Joy_caption_two_load`、`AIO_Preprocessor`、`LoraLoader`、`LoadImage`、`LoraLoader|pysssss`、`easy cleanGpuUsed`、`String`、`KSampler`、`ControlNetApplySD3`、`EmptyLatentImage`、`ImageResize+`、`Joy_caption_two`、`IPAdapterUnifiedLoader`、`ETN_Translate`、`LoadRembgByBiRefNetModel`、`UpscaleModelLoader`、`UltralyticsDetectorProvider`、`SAMLoader`、`CheckpointLoaderSimple`、`ControlNetLoader`、`DWPreprocessor`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、SetUnionControlNetType

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
