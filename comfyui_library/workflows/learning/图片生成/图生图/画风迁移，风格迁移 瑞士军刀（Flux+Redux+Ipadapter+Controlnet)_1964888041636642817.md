---
key: 图片生成/图生图/画风迁移，风格迁移 瑞士军刀（Flux+Redux+Ipadapter+Controlnet)_1964888041636642817.json
name: 画风迁移，风格迁移 瑞士军刀（Flux+Redux+Ipadapter+Controlnet)_1964888041636642817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/画风迁移，风格迁移 瑞士军刀（Flux+Redux+Ipadapter+Controlnet)_1964888041636642817.json
hash: 341f9c88dd2c2fd9
coverage: 0.857143
learned_at: 2026-10-23 13:17:56
nodes: [StyleModelLoader, CLIPVisionLoader, ReduxAdvanced, IPAdapterFluxLoader, ControlNetLoader, ControlNetApplyAdvanced, VAELoader, easy cleanGpuUsed, UNETLoader, DualCLIPLoader, easy cleanGpuUsed, ApplyIPAdapterFlux, Anything Everywhere3, easy cleanGpuUsed, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetLoader, ControlNetLoader, PreviewImage, AIO_Preprocessor, PreviewImage, AIO_Preprocessor, PreviewImage, AIO_Preprocessor, LoraLoaderModelOnly, LoraLoaderModelOnly, RH_Translator, ShowText, ZML_TextInput, Fast Groups Bypasser (rgthree), CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, FluxGuidance, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, EmptyLatentImage, ConditioningZeroOut, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "controlnet_strength": 0.6000000000000001, "denoise": "simple", "height": 512, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 512}
---

# 图片生成/图生图/画风迁移，风格迁移 瑞士军刀（Flux+Redux+Ipadapter+Controlnet)_1964888041636642817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/画风迁移，风格迁移 瑞士军刀（Flux+Redux+Ipadapter+Controlnet)_1964888041636642817.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `IPAdapterFluxLoader`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `ApplyIPAdapterFlux`
- `Anything Everywhere3`
- `easy cleanGpuUsed`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `AIO_Preprocessor`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `ShowText`
- `ZML_TextInput`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `FluxGuidance`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `PreviewImage`

## 关键参数

- `controlnet_strength` = `0.6000000000000001`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`StyleModelLoader`、`CLIPVisionLoader`、`ReduxAdvanced`、`IPAdapterFluxLoader`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`VAELoader`、`easy cleanGpuUsed`、`UNETLoader`、`DualCLIPLoader`、`ApplyIPAdapterFlux`、`AIO_Preprocessor`、`LoraLoaderModelOnly`、`RH_Translator`、`ShowText`、`ZML_TextInput`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`FluxGuidance`、`KSamplerAdvanced`、`VAEDecode`、`EmptyLatentImage`、`ConditioningZeroOut`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
