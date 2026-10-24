---
key: 图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json
name: flux.1 dev 背景高清（噪点去除）_2043925009676115969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json
hash: 28e1255c4af211f7
coverage: 0.911765
learned_at: 2026-10-23 11:35:49
nodes: [SamplerCustomAdvanced, SeedVR2, BasicGuider, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, DualCLIPLoader, VAELoader, KSamplerSelect, ControlNetLoader, ConditioningZeroOut, LoraLoaderModelOnly, UNETLoader, GrowMask, SeedVR2BlockSwap, LayerUtility: ImageReel, LoadImage, VAEDecode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, ImageCompositeMasked, ControlNetApplyAdvanced, LayerMask: SegmentAnythingUltra V2, Florence2ModelLoader, Florence2Run, BasicScheduler, ShowText|pysssss, CLIPTextEncodeFlux, LayerMask: MaskEdgeShrink, LayerUtility: ImageReelComposit, SaveImage, PreviewImage, easy imageRemBg]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6500000000000001}
---

# 图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `SamplerCustomAdvanced` ★核心
- `SeedVR2`
- `BasicGuider`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `ControlNetLoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `GrowMask`
- `SeedVR2BlockSwap`
- `LayerUtility: ImageReel`
- `LoadImage`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `ImageCompositeMasked`
- `ControlNetApplyAdvanced` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `Florence2ModelLoader`
- `Florence2Run`
- `BasicScheduler`
- `ShowText|pysssss`
- `CLIPTextEncodeFlux` ★核心
- `LayerMask: MaskEdgeShrink`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `PreviewImage`
- `easy imageRemBg`

## 关键参数

- `controlnet_strength` = `0.6500000000000001`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`SamplerCustomAdvanced`、`SeedVR2`、`BasicGuider`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`KSamplerSelect`、`ControlNetLoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`UNETLoader`、`GrowMask`、`SeedVR2BlockSwap`、`LayerUtility: ImageReel`、`VAEDecode`、`VAEEncode`、`RandomNoise`、`ImageCompositeMasked`、`ControlNetApplyAdvanced`、`LayerMask: SegmentAnythingUltra V2`、`Florence2ModelLoader`、`Florence2Run`、`BasicScheduler`、`CLIPTextEncodeFlux`、`LayerMask: MaskEdgeShrink`、`LayerUtility: ImageReelComposit`、`SaveImage`、`easy imageRemBg`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
