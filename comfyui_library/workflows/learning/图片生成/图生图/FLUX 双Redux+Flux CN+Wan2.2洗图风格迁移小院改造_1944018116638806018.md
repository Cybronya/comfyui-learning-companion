---
key: 图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json
name: FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json
hash: f84e66e18992dec7
coverage: 0.916667
learned_at: 2026-10-23 10:53:35
nodes: [KSamplerSelect, DF_Get_image_size, VAEEncode, ControlNetLoader, SetUnionControlNetType, SamplerCustomAdvanced, BasicGuider, CLIPTextEncode, CLIPTextEncode, RandomNoise, Image Comparer (rgthree), EmptyLatentImage, DualCLIPLoader, PreviewImage, ImageResize, ShowText, StyleModelLoader, CLIPVisionLoader, LoadImage, PreviewImage, easy cleanGpuUsed, easy cleanGpuUsed, VAELoader, LoadImage, FluxGuidance, easy cleanGpuUsed, ImageMirror, ImageMirror, ReduxAdvanced, UNETLoader, BasicScheduler, LoraLoader, ControlNetApplyAdvanced, ReduxAdvanced, UNETLoader, CLIPTextEncode, SaveImage, easy cleanGpuUsed, ImageConcatMulti, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, PreviewImage, CLIPLoader, CLIPTextEncode, CLIPTextEncode, PreviewImage, UpscaleModelLoader, SDXLPromptStyler, LoadImage, SDXLPromptStyler, RH_Captioner, VAELoader, LoraLoaderModelOnly, VAEEncode, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, CFGGuider, BasicScheduler, Image Comparer (rgthree), UltimateSDUpscale, KSamplerSelect, VAEDecode, easy cleanGpuUsed, VAEDecode, RH_Captioner, CombinationText, easy cleanGpuUsed, AIO_Preprocessor]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.7000000000000002, "height": 1024, "lora_name": "白色别墅.safetensors", "strength_clip": 1, "strength_model": 0.30000000000000004, "width": 768}
---

# 图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `KSamplerSelect` ★核心
- `DF_Get_image_size`
- `VAEEncode` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `ImageResize`
- `ShowText`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LoadImage`
- `PreviewImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAELoader`
- `LoadImage`
- `FluxGuidance`
- `easy cleanGpuUsed`
- `ImageMirror`
- `ImageMirror`
- `ReduxAdvanced`
- `UNETLoader` ★核心
- `BasicScheduler`
- `LoraLoader` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ReduxAdvanced`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `UpscaleModelLoader`
- `SDXLPromptStyler`
- `LoadImage`
- `SDXLPromptStyler`
- `RH_Captioner`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `CFGGuider`
- `BasicScheduler`
- `Image Comparer (rgthree)`
- `UltimateSDUpscale`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `RH_Captioner`
- `CombinationText`
- `easy cleanGpuUsed`
- `AIO_Preprocessor`

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `白色别墅.safetensors`
- `strength_model` = `0.30000000000000004`
- `strength_clip` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **92%**（66/72）

**有卡**：`KSamplerSelect`、`DF_Get_image_size`、`VAEEncode`、`ControlNetLoader`、`SetUnionControlNetType`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPTextEncode`、`RandomNoise`、`EmptyLatentImage`、`DualCLIPLoader`、`ImageResize`、`ShowText`、`StyleModelLoader`、`CLIPVisionLoader`、`LoadImage`、`easy cleanGpuUsed`、`VAELoader`、`FluxGuidance`、`ImageMirror`、`ReduxAdvanced`、`UNETLoader`、`BasicScheduler`、`LoraLoader`、`ControlNetApplyAdvanced`、`SaveImage`、`ImageConcatMulti`、`SplitSigmas`、`DisableNoise`、`CLIPLoader`、`UpscaleModelLoader`、`SDXLPromptStyler`、`RH_Captioner`、`LoraLoaderModelOnly`、`WanVideoNAG`、`ModelSamplingSD3`、`CFGGuider`、`UltimateSDUpscale`、`VAEDecode`、`CombinationText`、`AIO_Preprocessor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
