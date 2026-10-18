---
key: 视频生成/图生视频/wan2.2 animate动物替换实验成功_2016418267958616065.json
name: wan2.2 animate动物替换实验成功_2016418267958616065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 animate动物替换实验成功_2016418267958616065.json
hash: d63f40e0e7bf6b30
coverage: 0.537634
learned_at: 2026-10-15 22:34:42
nodes: [GetNode, GetNode, GetImageSizeAndCount, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoClipVisionEncode, SetNode, EmptyImage, MarkdownNote, FloatConstant, GetNode, GetNode, VHS_VideoCombine, WanVideoModelLoader, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, GetNode, MarkdownNote, WanVideoSampler, GetImageSizeAndCount, VHS_VideoCombine, WanVideoDecode, ImageConcatMulti, GetNode, DrawMaskOnImage, SetNode, DrawMaskOnImage, SetNode, BlockifyMask, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, MaskToImage, PreviewImage, easy imageRemBg, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, GrowMaskWithBlur, MarkdownNote, easy anythingIndexSwitch, Sam2Segmentation, GetNode, AnimalPosePreprocessor, SetNode, VHS_VideoCombine, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, easy anythingIndexSwitch, OnnxDetectionModelLoader, GetNode, DownloadAndLoadSAM2Model, PoseAndFaceDetection, GetNode, GetImageSizeAndCount, GetNode, Int, GetNode, SetNode, SetNode, MarkdownNote, VHS_LoadVideo, LoadImage, TextBox1, WanVideoTextEncodeCached, INTConstant, INTConstant, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, PreviewAny, PointsEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 animate动物替换实验成功_2016418267958616065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016418267958616065.json`

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
- `PreviewImage`
- `easy imageRemBg`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMaskWithBlur`
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
- `Int`
- `GetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `VHS_LoadVideo`
- `LoadImage`
- `TextBox1`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `PreviewAny`
- `PointsEditor`

## 知识

覆盖率 **54%**（50/93）

**有卡**：`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoClipVisionEncode`、`EmptyImage`、`FloatConstant`、`VHS_VideoCombine`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`DrawMaskOnImage`、`BlockifyMask`、`MaskToImage`、`easy imageRemBg`、`GrowMaskWithBlur`、`easy anythingIndexSwitch`、`Sam2Segmentation`、`AnimalPosePreprocessor`、`WanVideoAnimateEmbeds`、`OnnxDetectionModelLoader`、`DownloadAndLoadSAM2Model`、`PoseAndFaceDetection`、`Int`、`VHS_LoadVideo`、`LoadImage`、`TextBox1`、`WanVideoTextEncodeCached`、`INTConstant`、`PointsEditor`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
