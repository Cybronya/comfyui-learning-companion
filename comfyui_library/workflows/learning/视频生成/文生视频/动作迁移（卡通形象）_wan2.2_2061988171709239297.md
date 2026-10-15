---
key: 视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json
name: 动作迁移（卡通形象）_wan2.2_2061988171709239297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json
hash: d056f853d0994276
coverage: 0.896552
learned_at: 2026-10-15 22:48:14
nodes: [LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, ImageFromBatch, easy int, LoraLoaderModelOnly, CLIPVisionEncode, WanAnimateToVideo, easy int, easy int, WanAnimateToVideo, KSampler, easy int, CLIPTextEncode, easy int, SDPoseKeypointExtractor, PrimitiveBoolean, RTDETR_detect, SDPoseKeypointExtractor, LayerUtility: If , Reroute, SDPoseDrawKeypoints, CLIPVisionLoader, ImageResizeKJv2, Reroute, PrimitiveFloat, CheckpointLoaderSimple, UNETLoader, RTDETR_detect, CheckpointLoaderSimple, CLIPTextEncode, PrimitiveString, SAM3_Detect, CropByBBoxes, ComfyMathExpression, VHS_VideoCombine, easy showAnything, ImageResizeKJv2, easy forLoopEnd, TrimVideoLatent, VAEDecode, ImageFromBatch, ImageBatch, easy forLoopStart, KSampler, VAEDecode, TrimVideoLatent, easy int, ComfyMathExpression, Int, VHS_LoadVideo, LoadImage, CLIPTextEncode, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, MarkdownNote, UNETLoader, CLIPLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 822907241674085, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `ImageFromBatch`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `WanAnimateToVideo`
- `easy int`
- `easy int`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `easy int`
- `CLIPTextEncode` ★核心
- `easy int`
- `SDPoseKeypointExtractor`
- `PrimitiveBoolean`
- `RTDETR_detect`
- `SDPoseKeypointExtractor`
- `LayerUtility: If `
- `Reroute`
- `SDPoseDrawKeypoints`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `Reroute`
- `PrimitiveFloat`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `RTDETR_detect`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveString`
- `SAM3_Detect`
- `CropByBBoxes`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `easy showAnything`
- `ImageResizeKJv2`
- `easy forLoopEnd`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageBatch`
- `easy forLoopStart`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `easy int`
- `ComfyMathExpression`
- `Int`
- `VHS_LoadVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`

## 关键参数

- `seed` = `822907241674085`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **90%**（52/58）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`ImageFromBatch`、`easy int`、`CLIPVisionEncode`、`WanAnimateToVideo`、`KSampler`、`CLIPTextEncode`、`SDPoseKeypointExtractor`、`PrimitiveBoolean`、`RTDETR_detect`、`LayerUtility: If `、`SDPoseDrawKeypoints`、`CLIPVisionLoader`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`UNETLoader`、`SAM3_Detect`、`CropByBBoxes`、`ComfyMathExpression`、`VHS_VideoCombine`、`easy forLoopEnd`、`TrimVideoLatent`、`VAEDecode`、`ImageBatch`、`easy forLoopStart`、`Int`、`VHS_LoadVideo`、`LoadImage`、`BodyRatioMapperProportionTransfer`、`BodyRatioMapperSDPoseRender`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
