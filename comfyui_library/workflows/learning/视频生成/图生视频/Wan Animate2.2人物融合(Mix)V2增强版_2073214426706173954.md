---
key: 视频生成/图生视频/Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json
name: Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json
hash: e5ae5ed8d8290a7c
coverage: 0.493151
learned_at: 2026-10-15 22:41:01
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, WanVideoTextEncodeCached, Note, Note, Note, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, CR Prompt Text, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, Note, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoBlockSwap, GetNode, LayerUtility: PurgeVRAM, GetNode, WanVideoClipVisionEncode, ImageResizeKJv2, VHS_VideoCombine, GetNode, SetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, Reroute, OnnxDetectionModelLoader, DrawViTPose, SetNode, SetNode, LoadImage, SetNode, PoseAndFaceDetection, MarkdownNote, ACE_ImageFaceCrop, GetNode, GetNode, VHS_LoadVideo, PointsEditor, VHS_VideoCombine, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073214426706173954.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（73 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `Note`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `CR Prompt Text`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `Note`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `Reroute`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `PoseAndFaceDetection`
- `MarkdownNote`
- `ACE_ImageFaceCrop`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `PointsEditor`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **49%**（36/73）

**有卡**：`ImageConcatMulti`、`WanVideoTextEncodeCached`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`CLIPVisionLoader`、`CR Prompt Text`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`DrawViTPose`、`LoadImage`、`PoseAndFaceDetection`、`ACE_ImageFaceCrop`、`VHS_LoadVideo`、`PointsEditor`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
