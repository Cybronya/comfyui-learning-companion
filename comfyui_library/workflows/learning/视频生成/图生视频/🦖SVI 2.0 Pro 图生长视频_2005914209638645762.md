---
key: 视频生成/图生视频/🦖SVI 2.0 Pro 图生长视频_2005914209638645762.json
name: 🦖SVI 2.0 Pro 图生长视频_2005914209638645762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🦖SVI 2.0 Pro 图生长视频_2005914209638645762.json
hash: 756ebf93671cb9ee
coverage: 0.565891
learned_at: 2026-10-15 22:33:59
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, SetNode, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, KSamplerAdvanced, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, KSamplerAdvanced, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, GetNode, WanImageToVideoSVIPro, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, KSamplerAdvanced, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, GetNode, VAEEncode, SetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, WanImageToVideoSVIPro, JWInteger, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, Note, Note, Note, Note, LoadImage, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, Note, CR Prompt Text, Note, Note, ImageBatchExtendWithOverlap]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/🦖SVI 2.0 Pro 图生长视频_2005914209638645762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005914209638645762.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（129 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `SetNode`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `WanImageToVideoSVIPro`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`
- `CR Prompt Text`
- `Note`
- `Note`
- `ImageBatchExtendWithOverlap`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（73/129）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`INTConstant`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`VAEEncode`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
