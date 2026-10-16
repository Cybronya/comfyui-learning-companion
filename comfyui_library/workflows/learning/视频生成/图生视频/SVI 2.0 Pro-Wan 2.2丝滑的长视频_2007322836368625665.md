---
key: 视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json
name: SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007322836368625665.json
hash: fd02482208d39a0b
coverage: 0.55814
learned_at: 2026-10-15 22:34:03
nodes: [SetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, KSamplerAdvanced, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, CLIPTextEncode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, easy indexAnything, easy indexAnything, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, CLIPLoader, GetNode, VHS_VideoCombine, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SetNode, GetNode, VAELoader, INTConstant, MarkdownNote, GetNode, VAEDecode, GetNode, easy indexAnything, ImageBatchExtendWithOverlap, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideoSVIPro, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, GetNode, VHS_VideoCombine, ShowText|pysssss, easy indexAnything, ShowText|pysssss, ShowText|pysssss, KSamplerAdvanced, GetNode, WanImageToVideoSVIPro, GetNode, easy indexAnything, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, CLIPTextEncode, ShowText|pysssss, easy indexAnything, ShowText|pysssss, easy promptLine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007322836368625665.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（129 个）：
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
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
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `easy indexAnything`
- `easy indexAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPLoader`
- `GetNode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `VAELoader`
- `INTConstant`
- `MarkdownNote`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `easy indexAnything`
- `ImageBatchExtendWithOverlap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `easy indexAnything`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `easy indexAnything`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `easy indexAnything`
- `ShowText|pysssss`
- `easy promptLine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **56%**（72/129）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`INTConstant`、`DiffusionModelLoaderKJ`、`easy indexAnything`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`easy promptLine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
