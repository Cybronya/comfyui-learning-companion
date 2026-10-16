---
key: 视频生成/图生视频/(循环)Smooth 2.1高噪 SVI 2 Pro长视频动态强化版V1_2011030476026286081.json
name: (循环)Smooth 2.1高噪 SVI 2 Pro长视频动态强化版V1_2011030476026286081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2011030476026286081.json
hash: b75c21ac07a3c564
coverage: 0.894737
learned_at: 2026-10-15 22:34:20
nodes: [CLIPTextEncode, VAEDecode, ImageBatchExtendWithOverlap, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, JWInteger, Note, Note, VAEEncode, SimpleMath+, CLIPLoader, DiffusionModelLoaderKJ, KSamplerAdvanced, CLIPTextEncode, easy promptLine, CLIPTextEncode, easy promptLine, LoadImage, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SimpleMath+, LoraLoaderModelOnly, LoraLoaderModelOnly, easy forLoopStart, VAEDecode, VHS_VideoCombine, easy forLoopEnd, WanImageToVideoSVIPro, VHS_VideoCombine, WanImageToVideoSVIPro, CR Text, Int, LoraLoaderModelOnly, DiffusionModelLoaderKJ]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/(循环)Smooth 2.1高噪 SVI 2 Pro长视频动态强化版V1_2011030476026286081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011030476026286081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `Note`
- `Note`
- `VAEEncode` ★核心
- `SimpleMath+`
- `CLIPLoader`
- `DiffusionModelLoaderKJ`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `LoadImage`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy forLoopStart`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `WanImageToVideoSVIPro`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `CR Text`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`KSamplerAdvanced`、`JWInteger`、`VAEEncode`、`SimpleMath+`、`CLIPLoader`、`DiffusionModelLoaderKJ`、`easy promptLine`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`LoraLoaderModelOnly`、`easy forLoopStart`、`VHS_VideoCombine`、`easy forLoopEnd`、`WanImageToVideoSVIPro`、`CR Text`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
