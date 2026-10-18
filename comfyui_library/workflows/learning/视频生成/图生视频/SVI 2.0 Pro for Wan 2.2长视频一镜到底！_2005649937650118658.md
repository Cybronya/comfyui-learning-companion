---
key: 视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json
name: SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json
hash: 7cf29e5951d9e796
coverage: 0.566929
learned_at: 2026-10-15 22:33:58
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, CLIPTextEncode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEEncode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetNode, easy indexAnything, easy indexAnything, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, easy indexAnything, ShowText|pysssss, easy indexAnything, ShowText|pysssss, easy indexAnything, ShowText|pysssss, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, ImageBatchExtendWithOverlap, VHS_VideoCombine, easy promptLine, easy indexAnything]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005649937650118658.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（127 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
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
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `easy indexAnything`
- `easy indexAnything`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `easy indexAnything`
- `ShowText|pysssss`
- `easy indexAnything`
- `ShowText|pysssss`
- `easy indexAnything`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `easy promptLine`
- `easy indexAnything`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（72/127）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`INTConstant`、`DiffusionModelLoaderKJ`、`VAEEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy indexAnything`、`VHS_VideoCombine`、`easy promptLine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
