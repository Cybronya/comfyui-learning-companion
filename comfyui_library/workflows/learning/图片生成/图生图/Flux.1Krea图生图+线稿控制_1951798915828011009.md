---
key: 图片生成/图生图/Flux.1Krea图生图+线稿控制_1951798915828011009.json
name: Flux.1Krea图生图+线稿控制_1951798915828011009
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1Krea图生图+线稿控制_1951798915828011009.json
hash: e84631ca46d20737
coverage: 0.941176
learned_at: 2026-10-23 10:58:44
nodes: [VAEDecode, SaveImage, ClipInterrogator, KSampler, ControlNetApplyAdvanced, CLIPTextEncode, ConditioningZeroOut, ControlNetLoader, VAELoader, PreviewImage, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 553161027095254, "steps": 20}
---

# 图片生成/图生图/Flux.1Krea图生图+线稿控制_1951798915828011009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1Krea图生图+线稿控制_1951798915828011009.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `ClipInterrogator`
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ControlNetLoader`
- `VAELoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `553161027095254`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAEDecode`、`SaveImage`、`ClipInterrogator`、`KSampler`、`ControlNetApplyAdvanced`、`CLIPTextEncode`、`ConditioningZeroOut`、`ControlNetLoader`、`VAELoader`、`AIO_Preprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
