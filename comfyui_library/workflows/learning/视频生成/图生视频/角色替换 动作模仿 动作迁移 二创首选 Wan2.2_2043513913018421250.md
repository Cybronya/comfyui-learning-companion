---
key: 视频生成/图生视频/角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2043513913018421250.json
name: 角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2043513913018421250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043513913018421250.json
hash: 5e9d84606ca2d8b2
coverage: 0.555556
learned_at: 2026-10-15 22:36:32
nodes: [GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CR Text, WanVideoAnimateEmbeds, WanVideoDecode, GetNode, GetNode, GetImageSizeAndCount, WanVideoTextEncodeCached, easy cleanGpuUsed, ImageConcanate, easy cleanGpuUsed, WanVideoSampler, WanVideoBlockSwap, WanVideoSetLoRAs, PreviewImage, Note, INTConstant, INTConstant, SetNode, SetNode, GetNode, INTConstant, ImageFromBatch+, PointsEditor, SeCModelLoader, GetImageSizeAndCount, OnnxDetectionModelLoader, SeCVideoSegmentation, InvertMask, MaskToImage, LayerUtility: ImageBlend, PoseAndFaceDetection, easy cleanGpuUsed, SetNode, VHS_VideoCombine, SetNode, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, SetNode, SetNode, VHS_VideoInfo, GetNode, GetNode, SetNode, GetNode, VHS_LoadVideo, GetNode, ImageResizeKJv2, SetNode, GrowMask, SetNode, SetNode, GetNode, DrawMaskOnImage, GetNode, VHS_VideoCombine, DrawViTPose, BlockifyMask, SetNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, VHS_VideoCombine, SetNode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换 动作模仿 动作迁移 二创首选 Wan2.2_2043513913018421250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043513913018421250.json`

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
- `PointsEditor`
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
- `VHS_LoadVideo`
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
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`

## 知识

覆盖率 **56%**（45/81）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`CR Text`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`easy cleanGpuUsed`、`ImageConcanate`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`INTConstant`、`ImageFromBatch+`、`PointsEditor`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`VHS_VideoInfo`、`VHS_LoadVideo`、`ImageResizeKJv2`、`GrowMask`、`DrawMaskOnImage`、`DrawViTPose`、`BlockifyMask`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
