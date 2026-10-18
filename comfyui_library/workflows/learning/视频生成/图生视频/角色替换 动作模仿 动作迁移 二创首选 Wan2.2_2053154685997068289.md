---
key: 视频生成/图生视频/角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2053154685997068289.json
name: 角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2053154685997068289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2053154685997068289.json
hash: 9dbf228e7fedc79a
coverage: 0.555556
learned_at: 2026-10-15 22:37:36
nodes: [GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CR Text, WanVideoAnimateEmbeds, WanVideoDecode, GetNode, GetNode, GetImageSizeAndCount, WanVideoTextEncodeCached, easy cleanGpuUsed, ImageConcanate, easy cleanGpuUsed, WanVideoSampler, WanVideoBlockSwap, WanVideoSetLoRAs, PreviewImage, Note, INTConstant, INTConstant, SetNode, SetNode, GetNode, INTConstant, ImageFromBatch+, SeCModelLoader, GetImageSizeAndCount, OnnxDetectionModelLoader, SeCVideoSegmentation, InvertMask, MaskToImage, LayerUtility: ImageBlend, PoseAndFaceDetection, easy cleanGpuUsed, SetNode, VHS_VideoCombine, SetNode, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, SetNode, SetNode, VHS_VideoInfo, GetNode, GetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, GrowMask, SetNode, SetNode, GetNode, DrawMaskOnImage, GetNode, VHS_VideoCombine, DrawViTPose, BlockifyMask, SetNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, SetNode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, WanVideoModelLoader, SetNode, PointsEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2053154685997068289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053154685997068289.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（81 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CR Text`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `PreviewImage`
- `Note`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `ImageFromBatch+`
- `SeCModelLoader`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `SeCVideoSegmentation`
- `InvertMask`
- `MaskToImage`
- `LayerUtility: ImageBlend`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GrowMask`
- `SetNode`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `BlockifyMask`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `SetNode`
- `PointsEditor`

## 知识

覆盖率 **56%**（45/81）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`CR Text`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`easy cleanGpuUsed`、`ImageConcanate`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`INTConstant`、`ImageFromBatch+`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`VHS_VideoInfo`、`ImageResizeKJv2`、`GrowMask`、`DrawMaskOnImage`、`DrawViTPose`、`BlockifyMask`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
