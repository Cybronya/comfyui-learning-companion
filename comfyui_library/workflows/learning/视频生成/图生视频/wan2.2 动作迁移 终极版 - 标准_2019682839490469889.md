---
key: 视频生成/图生视频/wan2.2 动作迁移 终极版 - 标准_2019682839490469889.json
name: wan2.2 动作迁移 终极版 - 标准_2019682839490469889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019682839490469889.json
hash: 283cb2916c51a766
coverage: 0.938776
learned_at: 2026-10-15 22:35:03
nodes: [WanVideoClipVisionEncode, WanVideoDecode, Reroute, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSamplerv2, WanVideoSampler, WanVideoSamplerExtraArgs, WanVideoSchedulerv2, Text, WanVideoTextEncodeCached, YOLOModelLoader, OnnxDetectionModelLoader, BatchCount+, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoVAELoader, CheckpointLoaderSimple, SDPoseOODLoader, BBoxYOLO, SDPoseDrawKeypoints, SDPoseOODProcessor, YOLOModelLoader, WanVideoLoraSelectMulti, ImageFromBatch, easy int, LoadImage, SDPoseKeypointExtractor, VHS_VideoCombine, LoadImage, RIFE VFI, Reroute, MathExpression|pysssss, WanVideoLoraSelectMulti, Int, VHS_VideoInfo, PoseAndFaceDetection, AdaptiveWanVideoAnimateEmbeds, WanVideoSetLoRAs, CLIPVisionLoader, SetNode, ImageBatch, RHHiddenNodes, Int, Int, VHS_LoadVideo, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/wan2.2 动作迁移 终极版 - 标准_2019682839490469889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019682839490469889.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `Reroute`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSamplerv2` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoSchedulerv2`
- `Text`
- `WanVideoTextEncodeCached`
- `YOLOModelLoader`
- `OnnxDetectionModelLoader`
- `BatchCount+`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoVAELoader`
- `CheckpointLoaderSimple` ★核心
- `SDPoseOODLoader`
- `BBoxYOLO`
- `SDPoseDrawKeypoints`
- `SDPoseOODProcessor`
- `YOLOModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `LoadImage`
- `SDPoseKeypointExtractor`
- `VHS_VideoCombine`
- `LoadImage`
- `RIFE VFI`
- `Reroute`
- `MathExpression|pysssss`
- `WanVideoLoraSelectMulti`
- `Int`
- `VHS_VideoInfo`
- `PoseAndFaceDetection`
- `AdaptiveWanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `SetNode`
- `ImageBatch`
- `RHHiddenNodes`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `ImageResizeKJv2`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **94%**（46/49）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSamplerv2`、`WanVideoSampler`、`WanVideoSamplerExtraArgs`、`WanVideoSchedulerv2`、`Text`、`WanVideoTextEncodeCached`、`YOLOModelLoader`、`OnnxDetectionModelLoader`、`BatchCount+`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoVAELoader`、`CheckpointLoaderSimple`、`SDPoseOODLoader`、`BBoxYOLO`、`SDPoseDrawKeypoints`、`SDPoseOODProcessor`、`ImageFromBatch`、`easy int`、`LoadImage`、`SDPoseKeypointExtractor`、`VHS_VideoCombine`、`RIFE VFI`、`MathExpression|pysssss`、`Int`、`VHS_VideoInfo`、`PoseAndFaceDetection`、`AdaptiveWanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`ImageBatch`、`RHHiddenNodes`、`VHS_LoadVideo`、`ImageResizeKJv2`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoSampler、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
