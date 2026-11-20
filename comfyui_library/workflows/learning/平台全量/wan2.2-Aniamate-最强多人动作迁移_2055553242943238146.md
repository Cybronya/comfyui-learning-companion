---
key: 平台全量/wan2.2-Aniamate-最强多人动作迁移_2055553242943238146.json
name: wan2.2-Aniamate-最强多人动作迁移_2055553242943238146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-Aniamate-最强多人动作迁移_2055553242943238146.json
hash: 7213cd3b9b87ca24
coverage: 0.975
learned_at: 2026-11-14 01:19:26
nodes: [INTConstant, INTConstant, INTConstant, WanVideoLoraSelectMulti, SimpleMath+, WanVideoModelLoader, WanVideoTorchCompileSettings, LoadImage, INTConstant, VHS_VideoCombine, ImageResizeKJv2, BodyRatioMapperSDPoseRender, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoTextEncodeCached, OnnxDetectionModelLoader, PoseAndFaceDetection, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, YOLOModelLoader, YOLOModelLoader, ImageResizeKJv2, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, PreviewImage, BodyRatioMapperProportionTransfer, BBoxYOLO, WanVideoSamplerSettings, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoVAELoader, VHS_VideoInfoLoaded, VHS_LoadVideo, BBoxYOLO, VHS_VideoCombine, CLIPVisionLoader, WanVideoSamplerFromSettings, WanVideoDecode]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/wan2.2-Aniamate-最强多人动作迁移_2055553242943238146.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-Aniamate-最强多人动作迁移_2055553242943238146.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `BodyRatioMapperSDPoseRender`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoTextEncodeCached`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `YOLOModelLoader`
- `ImageResizeKJv2`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `PreviewImage`
- `BodyRatioMapperProportionTransfer`
- `BBoxYOLO`
- `WanVideoSamplerSettings` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `VHS_VideoInfoLoaded`
- `VHS_LoadVideo`
- `BBoxYOLO`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoDecode`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`INTConstant`、`WanVideoLoraSelectMulti`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadImage`、`VHS_VideoCombine`、`ImageResizeKJv2`、`BodyRatioMapperSDPoseRender`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`YOLOModelLoader`、`BodyRatioMapperProportionTransfer`、`BBoxYOLO`、`WanVideoSamplerSettings`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`CLIPVisionLoader`、`WanVideoSamplerFromSettings`、`WanVideoDecode`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader
