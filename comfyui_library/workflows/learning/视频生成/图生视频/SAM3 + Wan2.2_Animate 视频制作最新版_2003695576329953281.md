---
key: 视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json
name: SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json
hash: e51eb194b569d403
coverage: 0.965517
learned_at: 2026-10-15 22:33:51
nodes: [WanVideoDecode, WanVideoAnimateEmbeds, VHS_VideoCombine, ImageFromBatch, VHS_VideoCombine, SDPoseOODProcessor, SDPoseOODLoader, ColorToMask, LayerUtility: ImageBlend V2, PreviewImage, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoBlockSwap, ImageResizeKJv2, WanVideoSampler, VHS_VideoInfo, DrawViTPose, PoseAndFaceDetection, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, CLIPVisionLoader, WanVideoModelLoader, WanVideoVAELoader, INTConstant, INTConstant, OnnxDetectionModelLoader, WanVideoLoraSelectMulti, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003695576329953281.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `SDPoseOODProcessor`
- `SDPoseOODLoader`
- `ColorToMask`
- `LayerUtility: ImageBlend V2`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `VHS_VideoInfo`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `OnnxDetectionModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`WanVideoDecode`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`ImageFromBatch`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`ColorToMask`、`LayerUtility: ImageBlend V2`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`WanVideoSampler`、`VHS_VideoInfo`、`DrawViTPose`、`PoseAndFaceDetection`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`INTConstant`、`OnnxDetectionModelLoader`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeSingle、WanVideoLoraSelectMulti
