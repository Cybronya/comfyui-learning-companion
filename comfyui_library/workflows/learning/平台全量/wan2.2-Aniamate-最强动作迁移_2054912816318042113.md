---
key: 平台全量/wan2.2-Aniamate-最强动作迁移_2054912816318042113.json
name: wan2.2-Aniamate-最强动作迁移_2054912816318042113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-Aniamate-最强动作迁移_2054912816318042113.json
hash: cce820ec11204683
coverage: 1
learned_at: 2026-11-14 01:19:25
nodes: [INTConstant, INTConstant, INTConstant, INTConstant, WanVideoSamplerSettings, WanVideoContextOptions, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoVAELoader, SimpleMath+, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, WanVideoSamplerFromSettings, WanVideoDecode, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoAnimateEmbeds, OnnxDetectionModelLoader, ImageResizeKJv2, PoseAndFaceDetection, CheckpointLoaderSimple, SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, SDPoseKeypointExtractor, VHS_VideoCombine, LoadImage, WanVideoTorchCompileSettings, VHS_LoadVideo, BodyRatioMapperProportionTransfer, VHS_VideoCombine, BodyRatioMapperSDPoseRender, VHS_VideoCombine, VHS_VideoInfoLoaded]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/wan2.2-Aniamate-最强动作迁移_2054912816318042113.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-Aniamate-最强动作迁移_2054912816318042113.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoSamplerSettings` ★核心
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SimpleMath+`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoAnimateEmbeds`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `PoseAndFaceDetection`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `SDPoseKeypointExtractor`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `VHS_LoadVideo`
- `BodyRatioMapperProportionTransfer`
- `VHS_VideoCombine`
- `BodyRatioMapperSDPoseRender`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **100%**（34/34）

**有卡**：`INTConstant`、`WanVideoSamplerSettings`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`SimpleMath+`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoSamplerFromSettings`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`VHS_LoadVideo`、`BodyRatioMapperProportionTransfer`、`VHS_VideoInfoLoaded`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader
