---
key: 平台全量/wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545.json
name: wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545.json
hash: 17fdada100f800ff
coverage: 0.585366
learned_at: 2026-11-14 01:19:43
nodes: [Primitive integer [Crystools], VHS_VideoInfoLoaded, Display Int (rgthree), SimpleMath+, Display Int (rgthree), SetNode, SetNode, SetNode, Int, GetNode, GetNode, GetNode, ImageResizeKJv2, SimpleMath+, SetNode, SetNode, SetNode, CM_IntToFloat, GetNode, GetNode, Int, Int, Int, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, SetNode, PathchSageAttentionKJ, CLIPLoader, CLIPVisionLoader, CLIPVisionLoader, GetNode, SetNode, VAELoader, SetNode, CLIPVisionEncode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageScale, PoseAndFaceDetection, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy seed, GetNode, SimpleMath+, Display Int (rgthree), GetNode, GetNode, KSampler, KSampler, KSampler, VAEDecode, TrimVideoLatent, TrimVideoLatent, VAEDecode, VHS_GetImageCount, SetNode, Display Int (rgthree), VHS_GetImageCount, SetNode, Display Int (rgthree), TrimVideoLatent, Display Int (rgthree), VHS_GetImageCount, VAEDecode, SetNode, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, ImageBatchMulti, SetNode, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, ImageResizeKJv2, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, BBoxYOLO, BBoxYOLO, PreviewImage, BodyRatioMapperSDPoseRender, ImageResizeKJv2, BodyRatioMapperProportionTransfer, Note, LoadImage, VHS_LoadVideo, Note, SetNode, LoraLoaderModelOnly, YOLOModelLoader, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 183841061922479, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
- `Primitive integer [Crystools]`
- `VHS_VideoInfoLoaded`
- `Display Int (rgthree)`
- `SimpleMath+`
- `Display Int (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `CM_IntToFloat`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPVisionEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy seed`
- `GetNode`
- `SimpleMath+`
- `Display Int (rgthree)`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `SetNode`
- `Display Int (rgthree)`
- `VHS_GetImageCount`
- `SetNode`
- `Display Int (rgthree)`
- `TrimVideoLatent`
- `Display Int (rgthree)`
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `SetNode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `BBoxYOLO`
- `BBoxYOLO`
- `PreviewImage`
- `BodyRatioMapperSDPoseRender`
- `ImageResizeKJv2`
- `BodyRatioMapperProportionTransfer`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`
- `Note`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `YOLOModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `183841061922479`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **59%**（72/123）

**有卡**：`Primitive integer [Crystools]`、`VHS_VideoInfoLoaded`、`Display Int (rgthree)`、`SimpleMath+`、`Int`、`ImageResizeKJv2`、`CM_IntToFloat`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`、`ImageScale`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`easy seed`、`KSampler`、`VAEDecode`、`TrimVideoLatent`、`VHS_GetImageCount`、`GetImageRangeFromBatch`、`ImageBatchMulti`、`WanAnimateToVideo`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BBoxYOLO`、`BodyRatioMapperSDPoseRender`、`BodyRatioMapperProportionTransfer`、`LoadImage`、`VHS_LoadVideo`、`YOLOModelLoader`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
