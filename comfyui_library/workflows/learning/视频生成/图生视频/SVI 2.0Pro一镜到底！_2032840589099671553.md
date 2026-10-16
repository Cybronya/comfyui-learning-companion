---
key: 视频生成/图生视频/SVI 2.0Pro一镜到底！_2032840589099671553.json
name: SVI 2.0Pro一镜到底！_2032840589099671553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032840589099671553.json
hash: f61fc850c480f31c
coverage: 0.577586
learned_at: 2026-10-15 22:35:37
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, VAEDecode, VAEEncode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, SetNode, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageResizeKJv2, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LoadImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, ImageBatchExtendWithOverlap, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI 2.0Pro一镜到底！_2032840589099671553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032840589099671553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（116 个）：
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
- `GetNode`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
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
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **58%**（67/116）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`VHS_VideoCombine`、`DiffusionModelLoaderKJ`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
