---
key: 平台全量/SmoothMixWan2.2+SVI无限长视频_2005987580808216578.json
name: SmoothMixWan2.2+SVI无限长视频_2005987580808216578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SmoothMixWan2.2+SVI无限长视频_2005987580808216578.json
hash: 7e04408fbdb609ad
coverage: 0.581967
learned_at: 2026-11-14 01:00:44
nodes: [CLIPTextEncode, VAEDecode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, WanImageToVideoSVIPro, CLIPTextEncode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, CLIPTextEncode, VHS_VideoCombine, DiffusionModelLoaderKJ, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, SetNode, SetNode, INTConstant, VAEEncode, GetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, CR Prompt Text, ImageBatchExtendWithOverlap, VHS_VideoCombine, ImageBatchExtendWithOverlap, GetNode, PreviewImage, LoadImage, ImageResizeKJv2, CR Prompt Text, CR Prompt Text, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/SmoothMixWan2.2+SVI无限长视频_2005987580808216578.json

> 来源文件 `comfyui_library/workflows/平台全量/SmoothMixWan2.2+SVI无限长视频_2005987580808216578.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
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
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `VAEEncode` ★核心
- `GetNode`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `PreviewImage`
- `LoadImage`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **58%**（71/122）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`INTConstant`、`VHS_VideoCombine`、`DiffusionModelLoaderKJ`、`VAEEncode`、`CR Prompt Text`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerAdvanced、VAEEncode
