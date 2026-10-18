---
key: 视频生成/图生视频/SVI2.0PRO长视频循环流_2073295137563828226.json
name: SVI2.0PRO长视频循环流_2073295137563828226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SVI2.0PRO长视频循环流_2073295137563828226.json
hash: 19284c5c405a1956
coverage: 0.506173
learned_at: 2026-10-15 22:41:03
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, easy forLoopStart, SetNode, SetNode, VAEDecode, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, WanImageToVideoSVIPro, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, seed _O, VHS_VideoCombine, GetNode, GetNode, easy forLoopEnd, SimpleMath+, GetNode, VHS_VideoCombine, ImageBatchExtendWithOverlap, TextListSelelct, GetNode, VAELoader, CLIPLoader, GetNode, GetNode, GetNode, INTConstant, INTConstant, VAEEncode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, SetNode, seed _O, GetNode, Note, SetNode, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, GetNode, SimpleMath+, KSamplerAdvanced, TextListSelelct, GODMT_SplitString, LoadImage, ImpactInt, ImpactInt, Int]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI2.0PRO长视频循环流_2073295137563828226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073295137563828226.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（81 个）：
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy forLoopStart`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
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
- `ImageBatchExtendWithOverlap`
- `TextListSelelct`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `seed _O`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `TextListSelelct`
- `GODMT_SplitString`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **51%**（41/81）

**有卡**：`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`easy forLoopStart`、`VAEDecode`、`WanImageToVideoSVIPro`、`CLIPTextEncode`、`seed _O`、`VHS_VideoCombine`、`easy forLoopEnd`、`SimpleMath+`、`ImageBatchExtendWithOverlap`、`TextListSelelct`、`VAELoader`、`CLIPLoader`、`INTConstant`、`VAEEncode`、`ImageResizeKJv2`、`KSamplerAdvanced`、`GODMT_SplitString`、`LoadImage`、`ImpactInt`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、seed _O
