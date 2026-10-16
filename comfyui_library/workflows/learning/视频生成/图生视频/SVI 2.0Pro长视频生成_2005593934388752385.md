---
key: 视频生成/图生视频/SVI 2.0Pro长视频生成_2005593934388752385.json
name: SVI 2.0Pro长视频生成_2005593934388752385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2005593934388752385.json
hash: 53485ec8199bfcdf
coverage: 0.570175
learned_at: 2026-10-15 22:33:57
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, VAEDecode, VAEEncode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, SetNode, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, CLIPTextEncode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, GetNode, GetNode, SetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LoadImage, ImageBatchExtendWithOverlap, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI 2.0Pro长视频生成_2005593934388752385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005593934388752385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（114 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `SetNode`
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
- `WanImageToVideoSVIPro`
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
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
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
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageBatchExtendWithOverlap`
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
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（65/114）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`INTConstant`、`DiffusionModelLoaderKJ`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
