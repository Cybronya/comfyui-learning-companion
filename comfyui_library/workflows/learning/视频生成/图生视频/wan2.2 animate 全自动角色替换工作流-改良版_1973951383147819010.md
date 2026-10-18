---
key: 视频生成/图生视频/wan2.2 animate 全自动角色替换工作流-改良版_1973951383147819010.json
name: wan2.2 animate 全自动角色替换工作流-改良版_1973951383147819010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 animate 全自动角色替换工作流-改良版_1973951383147819010.json
hash: 7479337bdca939a8
coverage: 0.4
learned_at: 2026-10-15 22:32:04
nodes: [SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, ModelSamplingSD3, CLIPLoader, VAELoader, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, SetNode, Int, Int, SetNode, SetNode, SetNode, SetNode, GetNode, CLIPVisionEncode, GetNode, GetNode, DWPreprocessor, PreviewImage, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, Int, SetNode, GetNode, SimpleMath+, TrimVideoLatent, GetNode, GetNode, easy showAnything, KSampler, GetNode, TrimVideoLatent, VAEDecode, GetNode, WanAnimateToVideo, easy showAnything, GetNode, SetNode, GetNode, easy showAnything, SimpleMath+, GetNode, GetNode, GetNode, UNETLoader, CLIPVisionLoader, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, PreviewImage, PixelPerfectResolution, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, easy forLoopStart, ImageBatch, GetNode, VAEDecode, ImageFromBatch, GetNode, ImageFromBatch, GetNode, SetNode, SetNode, VHS_VideoCombine, easy forLoopEnd, SetNode, SetNode, VHS_VideoCombine, Reroute, LoadImage, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, ImageScale, VHS_LoadVideo, DWPreprocessor, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, GrowMask, BlockifyMask, DrawMaskOnImage, AILab_MaskPreview, PreviewImage, SetNode, SetNode, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 218094680204822, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2 animate 全自动角色替换工作流-改良版_1973951383147819010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973951383147819010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `Int`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `KSampler` ★核心
- `GetNode`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetNode`
- `WanAnimateToVideo`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `PixelPerfectResolution`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopStart`
- `ImageBatch`
- `GetNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `Reroute`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `ImageScale`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `AILab_MaskPreview`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `PreviewImage`

## 关键参数

- `seed` = `218094680204822`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **40%**（44/110）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`Int`、`CLIPVisionEncode`、`DWPreprocessor`、`KSampler`、`SimpleMath+`、`TrimVideoLatent`、`VAEDecode`、`WanAnimateToVideo`、`UNETLoader`、`CLIPVisionLoader`、`VHS_VideoInfo`、`PixelPerfectResolution`、`VHS_VideoCombine`、`easy forLoopStart`、`ImageBatch`、`ImageFromBatch`、`easy forLoopEnd`、`LoadImage`、`ImageScale`、`VHS_LoadVideo`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`AILab_MaskPreview`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
