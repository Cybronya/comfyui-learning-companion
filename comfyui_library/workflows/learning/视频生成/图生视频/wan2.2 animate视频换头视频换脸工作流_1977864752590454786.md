---
key: 视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json
name: wan2.2 animate视频换头视频换脸工作流_1977864752590454786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json
hash: 81edcda487293478
coverage: 0.477612
learned_at: 2026-10-13 00:04:36
nodes: [SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, GetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, GrowMaskWithBlur, BlockifyMask, Note, Sam2Segmentation, GetImageSizeAndCount, SetNode, SetNode, GetNode, DownloadAndLoadSAM2Model, Note, MarkdownNote, WanVideoModelLoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoDecode, GetNode, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncodeCached, Bookmark (rgthree), Bookmark (rgthree), Label (rgthree), LoadImage, Bookmark (rgthree), PoseAndFaceDetection, DrawViTPose, MarkdownNote, INTConstant, INTConstant, VHS_LoadVideo, SetNode, WanVideoAnimateEmbeds, easy cleanGpuUsed, WanVideoContextOptions, Note, WanVideoSampler, Note, WanVideoVAELoader]
patterns: []
missing: [Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), Label (rgthree), easy cleanGpuUsed]
discoveries: [次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
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

覆盖率 **48%**（32/67）

**有卡**：`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2Segmentation`、`GetImageSizeAndCount`、`DownloadAndLoadSAM2Model`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoDecode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`LoadImage`、`PoseAndFaceDetection`、`DrawViTPose`、`INTConstant`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoVAELoader`

**缺卡**（5）：`Bookmark (rgthree)`、`Bookmark (rgthree)`、`Bookmark (rgthree)`、`Label (rgthree)`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
