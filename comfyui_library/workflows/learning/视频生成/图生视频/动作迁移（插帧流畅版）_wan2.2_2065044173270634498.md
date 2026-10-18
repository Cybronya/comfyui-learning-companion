---
key: 视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json
name: 动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json
hash: 9870f15389ae846f
coverage: 0.888889
learned_at: 2026-10-15 22:39:35
nodes: [LoraLoaderModelOnly, TrimVideoLatent, ImageFromBatch, ImageBatch, VAEDecode, ImageFromBatch, easy int, CLIPVisionEncode, WanAnimateToVideo, easy int, VAEDecode, TrimVideoLatent, easy int, WanAnimateToVideo, CheckpointLoaderSimple, UNETLoader, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, CLIPTextEncode, PrimitiveString, SAM3_Detect, CropByBBoxes, easy showAnything, LayerUtility: If , Reroute, easy forLoopStart, KSampler, KSampler, LoraLoaderModelOnly, Reroute, easy int, easy int, easy int, easy forLoopEnd, ComfyMathExpression, Reroute, ModelSamplingSD3, UnetLoaderGGUF, VAELoader, VHS_VideoInfo, FrameInterpolate, PrimitiveBoolean, BodyRatioMapperSDPoseRender, BodyRatioMapperProportionTransfer, SDPoseDrawKeypoints, SDPoseKeypointExtractor, RTDETR_detect, ImageResizeKJv2, ImageResizeKJv2, SDPoseKeypointExtractor, RTDETR_detect, easy showAnything, FrameInterpolationModelLoader, VHS_VideoCombine, LoadImage, PrimitiveInt, VHS_LoadVideo, CLIPLoaderGGUF, CLIPVisionLoader, easy int, ComfyMathExpression, ComfyMathExpression]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 121207885649684, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065044173270634498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（63 个）：
- `LoraLoaderModelOnly` ★核心
- `TrimVideoLatent`
- `ImageFromBatch`
- `ImageBatch`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `easy int`
- `CLIPVisionEncode`
- `WanAnimateToVideo`
- `easy int`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `easy int`
- `WanAnimateToVideo`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveString`
- `SAM3_Detect`
- `CropByBBoxes`
- `easy showAnything`
- `LayerUtility: If `
- `Reroute`
- `easy forLoopStart`
- `KSampler` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `easy int`
- `easy int`
- `easy int`
- `easy forLoopEnd`
- `ComfyMathExpression`
- `Reroute`
- `ModelSamplingSD3`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `VHS_VideoInfo`
- `FrameInterpolate`
- `PrimitiveBoolean`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperProportionTransfer`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `RTDETR_detect`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SDPoseKeypointExtractor`
- `RTDETR_detect`
- `easy showAnything`
- `FrameInterpolationModelLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `CLIPLoaderGGUF`
- `CLIPVisionLoader`
- `easy int`
- `ComfyMathExpression`
- `ComfyMathExpression`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `121207885649684`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（56/63）

**有卡**：`LoraLoaderModelOnly`、`TrimVideoLatent`、`ImageFromBatch`、`ImageBatch`、`VAEDecode`、`easy int`、`CLIPVisionEncode`、`WanAnimateToVideo`、`CheckpointLoaderSimple`、`UNETLoader`、`CLIPTextEncode`、`SAM3_Detect`、`CropByBBoxes`、`LayerUtility: If `、`easy forLoopStart`、`KSampler`、`easy forLoopEnd`、`ComfyMathExpression`、`ModelSamplingSD3`、`UnetLoaderGGUF`、`VAELoader`、`VHS_VideoInfo`、`FrameInterpolate`、`PrimitiveBoolean`、`BodyRatioMapperSDPoseRender`、`BodyRatioMapperProportionTransfer`、`SDPoseDrawKeypoints`、`SDPoseKeypointExtractor`、`RTDETR_detect`、`ImageResizeKJv2`、`FrameInterpolationModelLoader`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`CLIPLoaderGGUF`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
