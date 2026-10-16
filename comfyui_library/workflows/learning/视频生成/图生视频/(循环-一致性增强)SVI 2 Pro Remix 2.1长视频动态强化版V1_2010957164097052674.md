---
key: 视频生成/图生视频/(循环-一致性增强)SVI 2 Pro Remix 2.1长视频动态强化版V1_2010957164097052674.json
name: (循环-一致性增强)SVI 2 Pro Remix 2.1长视频动态强化版V1_2010957164097052674.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010957164097052674.json
hash: 360724a549d89f0a
coverage: 0.894737
learned_at: 2026-10-15 22:34:19
nodes: [CLIPTextEncode, VAEDecode, ImageBatchExtendWithOverlap, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, Note, Note, VAEEncode, SimpleMath+, CLIPLoader, DiffusionModelLoaderKJ, KSamplerAdvanced, CLIPTextEncode, easy promptLine, CLIPTextEncode, easy promptLine, LoadImage, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, VAELoader, SimpleMath+, LoraLoaderModelOnly, LoraLoaderModelOnly, easy forLoopStart, VAEDecode, easy forLoopEnd, WanImageToVideoSVIPro, VHS_VideoCombine, WanImageToVideoSVIPro, CR Text, Int, DiffusionModelLoaderKJ, VHS_VideoCombine, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/(循环-一致性增强)SVI 2 Pro Remix 2.1长视频动态强化版V1_2010957164097052674.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010957164097052674.json`

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
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy forLoopStart`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `WanImageToVideoSVIPro`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `CR Text`
- `Int`
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`KSamplerAdvanced`、`VAEEncode`、`SimpleMath+`、`CLIPLoader`、`DiffusionModelLoaderKJ`、`easy promptLine`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`VAELoader`、`easy forLoopStart`、`easy forLoopEnd`、`WanImageToVideoSVIPro`、`VHS_VideoCombine`、`CR Text`、`Int`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
