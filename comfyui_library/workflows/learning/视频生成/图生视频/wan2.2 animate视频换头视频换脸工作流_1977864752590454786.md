---
key: 视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json
name: wan2.2 animate视频换头视频换脸工作流_1977864752590454786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json
hash: 81edcda487293478
coverage: 0.552239
learned_at: 2026-10-15 22:42:59
nodes: [SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, GetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, GrowMaskWithBlur, BlockifyMask, Note, Sam2Segmentation, GetImageSizeAndCount, SetNode, SetNode, GetNode, DownloadAndLoadSAM2Model, Note, MarkdownNote, WanVideoModelLoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoDecode, GetNode, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncodeCached, Bookmark (rgthree), Bookmark (rgthree), Label (rgthree), LoadImage, Bookmark (rgthree), PoseAndFaceDetection, DrawViTPose, MarkdownNote, INTConstant, INTConstant, VHS_LoadVideo, SetNode, WanVideoAnimateEmbeds, easy cleanGpuUsed, WanVideoContextOptions, Note, WanVideoSampler, Note, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `Note`
- `Sam2Segmentation`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `Note`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `WanVideoDecode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `Bookmark (rgthree)`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `WanVideoContextOptions`
- `Note`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoVAELoader`

## 知识

覆盖率 **55%**（37/67）

**有卡**：`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2Segmentation`、`GetImageSizeAndCount`、`DownloadAndLoadSAM2Model`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoDecode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`Bookmark (rgthree)`、`Label (rgthree)`、`LoadImage`、`PoseAndFaceDetection`、`DrawViTPose`、`INTConstant`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
