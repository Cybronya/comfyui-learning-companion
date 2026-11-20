---
key: 平台全量/极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490.json
name: 极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490.json
hash: 5e44686090cb41e2
coverage: 0.795455
learned_at: 2026-11-14 02:17:23
nodes: [ImageResizeKJv2, GetImageSizeAndCount, PoseAndFaceDetection, LayerUtility: PurgeVRAM, SDPoseOODProcessor, LayerUtility: PurgeVRAM, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoClipVisionEncode, GetNode, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, SDPoseOODLoader, CLIPVisionLoader, WanVideoContextOptions, PreviewImage, GetNode, GetNode, GetNode, SetNode, OnnxDetectionModelLoader, SetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note, WanVideoUni3C_ControlnetLoader, WanVideoEncode, WanVideoUni3C_embeds, SetNode, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoAnimateEmbeds, VHS_VideoInfoLoaded, INTConstant, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490.json

> 来源文件 `comfyui_library/workflows/平台全量/极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `PoseAndFaceDetection`
- `LayerUtility: PurgeVRAM`
- `SDPoseOODProcessor`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SDPoseOODLoader`
- `CLIPVisionLoader`
- `WanVideoContextOptions`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Note`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoAnimateEmbeds`
- `VHS_VideoInfoLoaded`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **80%**（35/44）

**有卡**：`ImageResizeKJv2`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`LayerUtility: PurgeVRAM`、`SDPoseOODProcessor`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`SDPoseOODLoader`、`CLIPVisionLoader`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoAnimateEmbeds`、`VHS_VideoInfoLoaded`、`INTConstant`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
