---
key: 视频生成/图生视频/SVI+2.0Pro长视频生成_2005982973738565633.json
name: SVI+2.0Pro长视频生成_2005982973738565633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SVI+2.0Pro长视频生成_2005982973738565633.json
hash: 4b5ce1351a246679
coverage: 0.537634
learned_at: 2026-10-15 22:33:59
nodes: [CLIPLoader, SetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, GetNode, GetNode, SetNode, INTConstant, SetNode, SetNode, SetNode, WanImageToVideoSVIPro, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, GetNode, KSamplerAdvanced, GetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, GetNode, VAELoader, CLIPTextEncode, VAEDecode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, SetNode, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, INTConstant, GetNode, GetNode, WanImageToVideoSVIPro, ImageResizeKJv2, VAEEncode, GetNode, LoadImage, ImageBatchExtendWithOverlap, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/SVI+2.0Pro长视频生成_2005982973738565633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005982973738565633.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（93 个）：
- `CLIPLoader`
- `SetNode`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `GetNode`
- `LoadImage`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `1`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **54%**（50/93）

**有卡**：`CLIPLoader`、`WanImageToVideoSVIPro`、`ImageBatchExtendWithOverlap`、`KSamplerAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`INTConstant`、`CLIPTextEncode`、`VAELoader`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`VAEEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
