---
key: 平台全量/【AI发牌舞】只需上传一寸照，AI把你变成跳舞男神，Wan2.2 Animate KJ升级版工作流讲解，附「发牌舞」和「bobo摇」AI舞蹈案例展示_1974504783128170497.json
name: 【AI发牌舞】只需上传一寸照，AI把你变成跳舞男神，Wan2.2 Animate KJ升级版工作流讲解，附「发牌舞」和「bobo摇」AI舞蹈案例展示_1974504783128170497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【AI发牌舞】只需上传一寸照，AI把你变成跳舞男神，Wan2.2 Animate KJ升级版工作流讲解，附「发牌舞」和「bobo摇」AI舞蹈案例展示_1974504783128170497.json
hash: 7abc144a199b3590
coverage: 0.529412
learned_at: 2026-11-14 01:21:27
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, GetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, WanVideoContextOptions, Note, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, GrowMaskWithBlur, BlockifyMask, Note, Sam2Segmentation, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SetNode, DownloadAndLoadSAM2Model, Note, VHS_VideoCombine, MarkdownNote, MarkdownNote, INTConstant, INTConstant, SetNode, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, WanVideoSampler, LoadImage, GetImageSizeAndCount, ImageConcatMulti, WanVideoAnimateEmbeds, GetNode, VHS_LoadVideo, DrawViTPose, ImageResizeKJv2, WanVideoTextEncodeCached, Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/【AI发牌舞】只需上传一寸照，AI把你变成跳舞男神，Wan2.2 Animate KJ升级版工作流讲解，附「发牌舞」和「bobo摇」AI舞蹈案例展示_1974504783128170497.json

> 来源文件 `comfyui_library/workflows/平台全量/【AI发牌舞】只需上传一寸照，AI把你变成跳舞男神，Wan2.2 Animate KJ升级版工作流讲解，附「发牌舞」和「bobo摇」AI舞蹈案例展示_1974504783128170497.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（68 个）：
- `GetNode`
- `GetNode`
- `GetNode`
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `Note`
- `Sam2Segmentation`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `Note`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `WanVideoSampler` ★核心
- `LoadImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `VHS_LoadVideo`
- `DrawViTPose`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `Label (rgthree)`

## 知识

覆盖率 **53%**（36/68）

**有卡**：`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2Segmentation`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`DownloadAndLoadSAM2Model`、`INTConstant`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoSampler`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
