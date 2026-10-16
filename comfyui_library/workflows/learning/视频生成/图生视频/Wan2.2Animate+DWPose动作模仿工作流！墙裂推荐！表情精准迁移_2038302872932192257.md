---
key: 视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json
name: Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038302872932192257.json
hash: dc5d1753326f6d45
coverage: 0.818182
learned_at: 2026-10-15 22:36:01
nodes: [GetNode, GetNode, LayerUtility: PurgeVRAM, FaceMaskFromPoseKeypoints, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, CLIPVisionLoader, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, easy cleanGpuUsed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, PreviewImage, VHS_VideoCombine, DWPreprocessor, ImageCropByMaskAndResize, SetNode, WanVideoAnimateEmbeds, ImageResizeKJv2, PixelPerfectResolution, VHS_VideoInfoLoaded, SetNode, Text, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038302872932192257.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `FaceMaskFromPoseKeypoints`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `ImageResizeKJv2`
- `PixelPerfectResolution`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Text`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`LayerUtility: PurgeVRAM`、`FaceMaskFromPoseKeypoints`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`PixelPerfectResolution`、`VHS_VideoInfoLoaded`、`Text`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
