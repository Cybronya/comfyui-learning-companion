---
key: 平台全量/毛胚房装修样图 XL+F.1_1904408953780867073.json
name: 毛胚房装修样图 XL+F.1_1904408953780867073
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/毛胚房装修样图 XL+F.1_1904408953780867073.json
hash: 2ae67be4be6b9f22
coverage: 0.886792
learned_at: 2026-11-14 02:19:10
nodes: [RH_Prompter, SetUnionControlNetType, ControlNetLoader, AIO_Preprocessor, PreviewImage, ControlNetApplySD3, SetUnionControlNetType, ControlNetLoader, ImageBlend, DownloadAndLoadDepthAnythingV2Model, PreviewImage, LeReS-DepthMapPreprocessor, DepthAnything_V2, easy cleanGpuUsed, EmptyLatentImage, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, RandomNoise, FluxGuidance, ModelSamplingFlux, CLIPTextEncode, UNETLoader, DualCLIPLoader, RH_Captioner, easy cleanGpuUsed, VAELoader, VAEDecode, Bjornulf_ShowText, RH_Captioner, RH_Captioner, Bjornulf_ShowText, Text Concatenate (JPS), RH_Translator, ShowText|pysssss, KSampler, ControlNetApplySD3, CLIPTextEncode, PreviewImage, CLIPTextEncode, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoader, Image Comparer (rgthree), ImageResizeKJ, VAEDecode, LoraLoader, VAEEncode, ImageScaleBy, BasicScheduler, SaveImage, LoadImage, JjkText]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "黑格建筑及室内大模型_SDXL1.0.safetensors", "controlnet_strength": 0.6, "denoise": 1, "height": 512, "lora_name": "FLUX.1-Turbo-Alpha.safetensors", "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 892368942186507, "steps": 30, "strength_clip": 1, "strength_model": 1, "width": 512}
---

# 平台全量/毛胚房装修样图 XL+F.1_1904408953780867073.json

> 来源文件 `comfyui_library/workflows/平台全量/毛胚房装修样图 XL+F.1_1904408953780867073.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `RH_Prompter`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `ImageBlend`
- `DownloadAndLoadDepthAnythingV2Model`
- `PreviewImage`
- `LeReS-DepthMapPreprocessor`
- `DepthAnything_V2`
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `FluxGuidance`
- `ModelSamplingFlux`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `VAELoader`
- `VAEDecode` ★核心
- `Bjornulf_ShowText`
- `RH_Captioner`
- `RH_Captioner`
- `Bjornulf_ShowText`
- `Text Concatenate (JPS)`
- `RH_Translator`
- `ShowText|pysssss`
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `VAEEncode` ★核心
- `ImageScaleBy`
- `BasicScheduler`
- `SaveImage`
- `LoadImage`
- `JjkText`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `controlnet_strength` = `0.6`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `892368942186507`
- `steps` = `30`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `黑格建筑及室内大模型_SDXL1.0.safetensors`
- `lora_name` = `FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **89%**（47/53）

**有卡**：`RH_Prompter`、`SetUnionControlNetType`、`ControlNetLoader`、`AIO_Preprocessor`、`ControlNetApplySD3`、`ImageBlend`、`DownloadAndLoadDepthAnythingV2Model`、`LeReS-DepthMapPreprocessor`、`DepthAnything_V2`、`easy cleanGpuUsed`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`ModelSamplingFlux`、`CLIPTextEncode`、`UNETLoader`、`DualCLIPLoader`、`RH_Captioner`、`VAELoader`、`VAEDecode`、`Bjornulf_ShowText`、`Text Concatenate (JPS)`、`RH_Translator`、`KSampler`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LoraLoader`、`ImageResizeKJ`、`VAEEncode`、`ImageScaleBy`、`BasicScheduler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage
