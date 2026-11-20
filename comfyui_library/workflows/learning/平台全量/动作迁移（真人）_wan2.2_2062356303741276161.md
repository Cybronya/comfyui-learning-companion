---
key: 平台全量/动作迁移（真人）_wan2.2_2062356303741276161.json
name: 动作迁移（真人）_wan2.2_2062356303741276161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移（真人）_wan2.2_2062356303741276161.json
hash: 9f19139e80fcf42e
coverage: 0.921569
learned_at: 2026-11-14 01:46:08
nodes: [PrimitiveFloat, ModelSamplingSD3, VAELoader, CLIPVisionEncode, CLIPTextEncode, RTDETR_detect, UNETLoader, PixelPerfectResolution, ResizeImageMaskNode, SDPoseKeypointExtractor, SDPoseDrawKeypoints, LayerUtility: ImageRemoveAlpha, PrimitiveString, CLIPTextEncode, SAM3_Detect, CheckpointLoaderSimple, DrawMaskOnImage, WanAnimateToVideo, KSampler, TrimVideoLatent, VAEDecode, ImageFromBatch, KSampler, TrimVideoLatent, VAEDecode, ImageFromBatch, ImageBatch, easy forLoopEnd, CropByBBoxes, BlockifyMask, GrowMask, easy forLoopStart, LoadImage, CheckpointLoaderSimple, easy showAnything, ComfyMathExpression, ComfyMathExpression, easy int, easy int, Int, SAM3_Detect, Reroute, CLIPVisionLoader, CLIPTextEncode, VHS_LoadVideo, WanAnimateToVideo, LoraLoaderModelOnly, UNETLoader, VHS_VideoCombine, CLIPTextEncode, CLIPLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 123, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/动作迁移（真人）_wan2.2_2062356303741276161.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移（真人）_wan2.2_2062356303741276161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `PrimitiveFloat`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `RTDETR_detect`
- `UNETLoader` ★核心
- `PixelPerfectResolution`
- `ResizeImageMaskNode`
- `SDPoseKeypointExtractor`
- `SDPoseDrawKeypoints`
- `LayerUtility: ImageRemoveAlpha`
- `PrimitiveString`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `DrawMaskOnImage`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageBatch`
- `easy forLoopEnd`
- `CropByBBoxes`
- `BlockifyMask`
- `GrowMask`
- `easy forLoopStart`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `easy showAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy int`
- `easy int`
- `Int`
- `SAM3_Detect`
- `Reroute`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `WanAnimateToVideo`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPLoader`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `123`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（47/51）

**有卡**：`ModelSamplingSD3`、`VAELoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`RTDETR_detect`、`UNETLoader`、`PixelPerfectResolution`、`ResizeImageMaskNode`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`LayerUtility: ImageRemoveAlpha`、`SAM3_Detect`、`CheckpointLoaderSimple`、`DrawMaskOnImage`、`WanAnimateToVideo`、`KSampler`、`TrimVideoLatent`、`VAEDecode`、`ImageFromBatch`、`ImageBatch`、`easy forLoopEnd`、`CropByBBoxes`、`BlockifyMask`、`GrowMask`、`easy forLoopStart`、`LoadImage`、`ComfyMathExpression`、`easy int`、`Int`、`CLIPVisionLoader`、`VHS_LoadVideo`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
