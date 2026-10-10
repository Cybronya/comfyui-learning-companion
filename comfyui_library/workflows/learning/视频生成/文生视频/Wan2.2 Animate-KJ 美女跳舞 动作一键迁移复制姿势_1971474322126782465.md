---
key: 视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json
name: Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json
hash: cdabf0da50efbabf
coverage: 0.535211
learned_at: 2026-10-10 23:06:45
nodes: [SetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, SetNode, GetNode, SetNode, GetNode, GIMMVFI_interpolate, SetNode, GetNode, DownloadAndLoadGIMMVFIModel, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, SetNode, WanVideoTextEncodeCached, SetNode, SetNode, ImageConcatMulti, GetNode, VHS_VideoCombine, SetNode, WanVideoClipVisionEncode, VHS_VideoCombine, BlockifyMask, WanVideoTorchCompileSettings, INTConstant, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, GetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, INTConstant, INTConstant, PreviewImage, VHS_VideoCombine, ImageBlend, OnnxDetectionModelLoader, PreviewImage, PreviewImage, DownloadAndLoadSAM2Model, PoseAndFaceDetection, DrawViTPose, SetNode, SetNode, Sam2Segmentation, VHS_VideoCombine, GetNode, GetNode, GetNode, GrowMask, GetNode, DrawMaskOnImage, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（71 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `SetNode`
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
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `BlockifyMask`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageBlend`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `Sam2Segmentation`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `GetNode`
- `DrawMaskOnImage`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **54%**（38/71）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`BlockifyMask`、`WanVideoTorchCompileSettings`、`INTConstant`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageBlend`、`OnnxDetectionModelLoader`、`DownloadAndLoadSAM2Model`、`PoseAndFaceDetection`、`DrawViTPose`、`Sam2Segmentation`、`GrowMask`、`DrawMaskOnImage`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
