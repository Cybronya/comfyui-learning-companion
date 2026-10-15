---
key: 视频生成/文生视频/EverAnimate Long Video Consistent Editing_2072998873179922432.json
name: EverAnimate Long Video Consistent Editing_2072998873179922432
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/EverAnimate Long Video Consistent Editing_2072998873179922432.json
hash: 7619ac6d675dcfa4
coverage: 0.822785
learned_at: 2026-10-15 22:44:08
nodes: [BlockifyMask, GrowMaskWithBlur, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, CLIPTextEncode, VAELoader, Reroute, ComfyEverAnimateTrimImages, TrimVideoLatent, VAEDecode, ComfyEverAnimate, ModelSamplingSD3, KSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, ComfyEverAnimate, KSampler, TrimVideoLatent, VAEDecode, ComfyEverAnimateTrimImages, easy forLoopEnd, VHS_VideoInfo, CheckpointLoaderSimple, YOLOModelLoader, BBoxYOLO, SDPoseKeypointExtractor, YOLOModelLoader, BBoxYOLO, SDPoseKeypointExtractor, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, INTConstant, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, ImageResizeKJv2, ComfyMathExpression, VHS_VideoCombine, WD14Tagger|pysssss, LoadImage, DrawMaskOnImage, GetImageSizeAndCount, LayerMask: SAM2VideoUltra, LoadImage, SDPoseDrawKeypoints, easy imageIndexSwitch, LoraLoaderModelOnly, WanChunkFeedForward, ModelMemoryUsageFactorOverride, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, easy forLoopStart, ImageBatch, Note, Note, Note, Note, VHS_LoadVideo, CLIPTextEncode, CLIPTextEncode, INTConstant, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "lcm", "scheduler": "normal", "seed": 42, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/EverAnimate Long Video Consistent Editing_2072998873179922432.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/EverAnimate Long Video Consistent Editing_2072998873179922432.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（79 个）：
- `BlockifyMask`
- `GrowMaskWithBlur`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Reroute`
- `ComfyEverAnimateTrimImages`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ComfyEverAnimate`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ComfyEverAnimate`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ComfyEverAnimateTrimImages`
- `easy forLoopEnd`
- `VHS_VideoInfo`
- `CheckpointLoaderSimple` ★核心
- `YOLOModelLoader`
- `BBoxYOLO`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `BBoxYOLO`
- `SDPoseKeypointExtractor`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `INTConstant`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `WD14Tagger|pysssss`
- `LoadImage`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `LayerMask: SAM2VideoUltra`
- `LoadImage`
- `SDPoseDrawKeypoints`
- `easy imageIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `WanChunkFeedForward`
- `ModelMemoryUsageFactorOverride`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy forLoopStart`
- `ImageBatch`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `42`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **82%**（65/79）

**有卡**：`BlockifyMask`、`GrowMaskWithBlur`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`CLIPTextEncode`、`VAELoader`、`ComfyEverAnimateTrimImages`、`TrimVideoLatent`、`VAEDecode`、`ComfyEverAnimate`、`ModelSamplingSD3`、`KSampler`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy forLoopEnd`、`VHS_VideoInfo`、`CheckpointLoaderSimple`、`YOLOModelLoader`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`BodyRatioMapperProportionTransfer`、`BodyRatioMapperSDPoseRender`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageResizeKJv2`、`ComfyMathExpression`、`VHS_VideoCombine`、`WD14Tagger|pysssss`、`LoadImage`、`DrawMaskOnImage`、`GetImageSizeAndCount`、`LayerMask: SAM2VideoUltra`、`SDPoseDrawKeypoints`、`easy imageIndexSwitch`、`WanChunkFeedForward`、`ModelMemoryUsageFactorOverride`、`easy forLoopStart`、`ImageBatch`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
