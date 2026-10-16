---
key: 视频生成/图生视频/Wan 2.2 SVI 2.0 PRO 长视频最新版！_2005892831866744833.json
name: Wan 2.2 SVI 2.0 PRO 长视频最新版！_2005892831866744833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2005892831866744833.json
hash: 28f4445733f657d8
coverage: 0.566929
learned_at: 2026-10-15 22:33:59
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, CLIPTextEncode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEEncode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, GetNode, easy indexAnything, easy indexAnything, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, easy indexAnything, ShowText|pysssss, easy indexAnything, ShowText|pysssss, easy indexAnything, ShowText|pysssss, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageBatchExtendWithOverlap, easy indexAnything, ImageBatchExtendWithOverlap, VHS_VideoCombine, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, LoadImage, easy promptLine, LayerUtility: ImageScaleByAspectRatio V2, DiffusionModelLoaderKJ]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan 2.2 SVI 2.0 PRO 长视频最新版！_2005892831866744833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005892831866744833.json`

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
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
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
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `easy indexAnything`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `easy promptLine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DiffusionModelLoaderKJ`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（72/127）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`INTConstant`、`DiffusionModelLoaderKJ`、`VAEEncode`、`easy indexAnything`、`VHS_VideoCombine`、`LoadImage`、`easy promptLine`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
