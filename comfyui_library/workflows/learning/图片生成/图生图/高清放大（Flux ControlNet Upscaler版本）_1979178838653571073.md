---
key: 图片生成/图生图/高清放大（Flux ControlNet Upscaler版本）_1979178838653571073.json
name: 高清放大（Flux ControlNet Upscaler版本）_1979178838653571073
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清放大（Flux ControlNet Upscaler版本）_1979178838653571073.json
hash: bf8c0169eaa87f63
coverage: 0.592593
learned_at: 2026-10-23 13:35:07
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, FluxGuidance, LoadImage, JWInteger, DualCLIPLoader, VAELoader, Anything Everywhere3, ShowText|pysssss, RHHiddenNodes, PreviewImage, Image Comparer (rgthree), VAEEncode, KSampler, RHHiddenNodes, UNETLoader, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "simple", "seed": 307691566557845, "steps": 30}
---

# 图片生成/图生图/高清放大（Flux ControlNet Upscaler版本）_1979178838653571073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清放大（Flux ControlNet Upscaler版本）_1979178838653571073.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LoadImage`
- `JWInteger`
- `DualCLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `307691566557845`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（16/27）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxGuidance`、`LoadImage`、`JWInteger`、`DualCLIPLoader`、`VAELoader`、`RHHiddenNodes`、`VAEEncode`、`KSampler`、`UNETLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
