---
key: 平台全量/【一键AI换人，秒变K歌之王！】ComfyUI + Wan2.2 实战工作流公开！_1976167970101690370.json
name: 【一键AI换人，秒变K歌之王！】ComfyUI + Wan2.2 实战工作流公开！_1976167970101690370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【一键AI换人，秒变K歌之王！】ComfyUI + Wan2.2 实战工作流公开！_1976167970101690370.json
hash: d0bd14009de471c1
coverage: 0.521739
learned_at: 2026-11-14 01:22:34
nodes: [GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, GetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, WanVideoContextOptions, Note, WanVideoBlockSwap, WanVideoSetLoRAs, GrowMaskWithBlur, BlockifyMask, Note, Sam2Segmentation, GetImageSizeAndCount, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, GetNode, PoseAndFaceDetection, DownloadAndLoadSAM2Model, Note, WanVideoSampler, MarkdownNote, MarkdownNote, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, INTConstant, INTConstant, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, LoadImage, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, ImageConcatMulti, GetImageSizeAndCount, VHS_LoadVideo, Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/【一键AI换人，秒变K歌之王！】ComfyUI + Wan2.2 实战工作流公开！_1976167970101690370.json

> 来源文件 `comfyui_library/workflows/平台全量/【一键AI换人，秒变K歌之王！】ComfyUI + Wan2.2 实战工作流公开！_1976167970101690370.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（69 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
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
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoContextOptions`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `Note`
- `Sam2Segmentation`
- `GetImageSizeAndCount`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `DownloadAndLoadSAM2Model`
- `Note`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `INTConstant`
- `INTConstant`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `Label (rgthree)`

## 知识

覆盖率 **52%**（36/69）

**有卡**：`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2Segmentation`、`GetImageSizeAndCount`、`DrawViTPose`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`DownloadAndLoadSAM2Model`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`INTConstant`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`LoadImage`、`ImageResizeKJv2`、`VHS_LoadVideo`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
