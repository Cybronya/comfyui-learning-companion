---
key: 视频生成/文生视频/Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json
name: Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json
hash: ed6b5c5a3019d571
coverage: 0.528571
learned_at: 2026-10-15 22:43:47
nodes: [SetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, GetNode, SetNode, GetNode, GIMMVFI_interpolate, SetNode, GetNode, GetNode, GetNode, DownloadAndLoadGIMMVFIModel, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, SetNode, WanVideoTextEncodeCached, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, GetNode, SetNode, GetNode, WanVideoClipVisionEncode, GetNode, SetNode, PreviewImage, DownloadAndLoadSAM2Model, VHS_VideoCombine, Sam2Segmentation, DrawMaskOnImage, GrowMask, BlockifyMask, WanVideoTorchCompileSettings, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, OnnxDetectionModelLoader, ImageBlend, PreviewImage, GetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, SetNode, PreviewImage, PoseAndFaceDetection, MarkdownNote, INTConstant, INTConstant, INTConstant, VHS_LoadVideo, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1970355314094710785.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（70 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `VHS_VideoCombine`
- `Sam2Segmentation`
- `DrawMaskOnImage`
- `GrowMask`
- `BlockifyMask`
- `WanVideoTorchCompileSettings`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `OnnxDetectionModelLoader`
- `ImageBlend`
- `PreviewImage`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewImage`
- `PoseAndFaceDetection`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **53%**（37/70）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`DrawMaskOnImage`、`GrowMask`、`BlockifyMask`、`WanVideoTorchCompileSettings`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`INTConstant`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
