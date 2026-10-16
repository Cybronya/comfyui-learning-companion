---
key: 视频生成/图生视频/SVI2.0PRO视频延长_2073295687021846529.json
name: SVI2.0PRO视频延长_2073295687021846529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073295687021846529.json
hash: f26ad8e49e93357a
coverage: 0.521739
learned_at: 2026-10-15 22:41:03
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, easy forLoopStart, SetNode, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, WanImageToVideoSVIPro, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, seed _O, VHS_VideoCombine, GetNode, GetNode, easy forLoopEnd, SimpleMath+, GetNode, VHS_VideoCombine, TextListSelelct, GetNode, CLIPLoader, INTConstant, INTConstant, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, seed _O, GetNode, Note, SetNode, SetNode, SetNode, SetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, GetNode, SimpleMath+, KSamplerAdvanced, TextListSelelct, ImpactInt, ImpactInt, VAELoader, GetImageRangeFromBatch, VAEEncode, VAEEncode, SetNode, GetNode, SimpleMath+, SimpleMath+, VHS_VideoInfo, GetNode, GetNode, GetNode, SetNode, SetNode, GODMT_SplitString, Int, ImageBatchExtendWithOverlap, GetNode, GetImageRangeFromBatch, ImageResizeKJv2, VAEDecode, ImageBatchExtendWithOverlap, VHS_VideoCombine, SetNode, VHS_LoadVideo, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI2.0PRO视频延长_2073295687021846529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073295687021846529.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（92 个）：
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `easy forLoopStart`
- `SetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `seed _O`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `easy forLoopEnd`
- `SimpleMath+`
- `GetNode`
- `VHS_VideoCombine`
- `TextListSelelct`
- `GetNode`
- `CLIPLoader`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `seed _O`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `TextListSelelct`
- `ImpactInt`
- `ImpactInt`
- `VAELoader`
- `GetImageRangeFromBatch`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GODMT_SplitString`
- `Int`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **52%**（48/92）

**有卡**：`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`easy forLoopStart`、`WanImageToVideoSVIPro`、`VAEDecode`、`CLIPTextEncode`、`seed _O`、`VHS_VideoCombine`、`easy forLoopEnd`、`SimpleMath+`、`TextListSelelct`、`CLIPLoader`、`INTConstant`、`KSamplerAdvanced`、`ImpactInt`、`VAELoader`、`GetImageRangeFromBatch`、`VAEEncode`、`VHS_VideoInfo`、`GODMT_SplitString`、`Int`、`ImageBatchExtendWithOverlap`、`ImageResizeKJv2`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSamplerAdvanced、seed _O、VAEEncode
