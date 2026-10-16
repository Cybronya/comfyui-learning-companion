---
key: 视频生成/图生视频/wan2.2 animate动物替换+姿态迁移_1976916291078524930.json
name: wan2.2 animate动物替换+姿态迁移_1976916291078524930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976916291078524930.json
hash: 5f902e22344d82d3
coverage: 0.537634
learned_at: 2026-10-15 22:32:13
nodes: [GetNode, GetNode, GetImageSizeAndCount, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoClipVisionEncode, SetNode, EmptyImage, MarkdownNote, FloatConstant, GetNode, GetNode, VHS_VideoCombine, WanVideoModelLoader, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, GetNode, MarkdownNote, WanVideoSampler, GetImageSizeAndCount, VHS_VideoCombine, WanVideoDecode, ImageConcatMulti, GetNode, DrawMaskOnImage, SetNode, DrawMaskOnImage, SetNode, BlockifyMask, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, MaskToImage, Sam2Segmentation, DownloadAndLoadSAM2Model, PreviewImage, easy imageRemBg, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, GrowMaskWithBlur, TextBox1, MarkdownNote, easy anythingIndexSwitch, Sam2Segmentation, GetNode, AnimalPosePreprocessor, SetNode, VHS_VideoCombine, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, easy anythingIndexSwitch, OnnxDetectionModelLoader, GetNode, DownloadAndLoadSAM2Model, PoseAndFaceDetection, GetNode, GetImageSizeAndCount, GetNode, VHS_LoadVideo, INTConstant, INTConstant, Int, GetNode, SetNode, SetNode, LoadImage, SetNode, PreviewAny, MarkdownNote, PointsEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 animate动物替换+姿态迁移_1976916291078524930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976916291078524930.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（93 个）：
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `SetNode`
- `EmptyImage`
- `MarkdownNote`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `GetNode`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `MaskToImage`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `PreviewImage`
- `easy imageRemBg`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `TextBox1`
- `MarkdownNote`
- `easy anythingIndexSwitch`
- `Sam2Segmentation`
- `GetNode`
- `AnimalPosePreprocessor`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `easy anythingIndexSwitch`
- `OnnxDetectionModelLoader`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `PoseAndFaceDetection`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `Int`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `PreviewAny`
- `MarkdownNote`
- `PointsEditor`

## 知识

覆盖率 **54%**（50/93）

**有卡**：`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`EmptyImage`、`FloatConstant`、`VHS_VideoCombine`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`DrawMaskOnImage`、`BlockifyMask`、`MaskToImage`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`easy imageRemBg`、`GrowMaskWithBlur`、`TextBox1`、`easy anythingIndexSwitch`、`AnimalPosePreprocessor`、`WanVideoAnimateEmbeds`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`VHS_LoadVideo`、`INTConstant`、`Int`、`LoadImage`、`PointsEditor`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
