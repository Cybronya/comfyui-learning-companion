---
key: 图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json
name: 去掉字幕水印 wan2.2 animate_1971821276849434626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json
hash: 9fea0a6bf5507b94
coverage: 0.571429
learned_at: 2026-10-23 12:34:03
nodes: [SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, SetNode, GetNode, SetNode, GetNode, SetNode, DownloadAndLoadGIMMVFIModel, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, SetNode, ImageConcatMulti, GetNode, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, GetImageSizeAndCount, DrawMaskOnImage, OnnxDetectionModelLoader, SetNode, easy showTensorShape, easy showTensorShape, Reroute, SetNode, SetNode, INTConstant, INTConstant, INTConstant, BlockifyMask, MarkdownNote, VHS_VideoCombine, easy showTensorShape, GetNode, GetNode, GetNode, GetNode, GIMMVFI_interpolate, easy showAnything, VHS_VideoCombine, VHS_VideoInfo, ImageResizeKJv2, Frame Select, WanVideoSampler, WanVideoAnimateEmbeds, DF_Get_image_size, WanVideoClipVisionEncode, GetNode, Sam2Segmentation, PreviewImage, GetNode, SetNode, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, AILab_MaskPreview, RH_Translator, VHS_LoadVideo, DownloadAndLoadSAM2Model, Textbox, LoadImage, WanVideoTextEncodeCached, PointsEditor, MarkdownNote]
patterns: []
missing: []
---

# 图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
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
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `easy showTensorShape`
- `easy showTensorShape`
- `Reroute`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `BlockifyMask`
- `MarkdownNote`
- `VHS_VideoCombine`
- `easy showTensorShape`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `Frame Select`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `DF_Get_image_size`
- `WanVideoClipVisionEncode`
- `GetNode`
- `Sam2Segmentation`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `AILab_MaskPreview`
- `RH_Translator`
- `VHS_LoadVideo`
- `DownloadAndLoadSAM2Model`
- `Textbox`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `PointsEditor`
- `MarkdownNote`

## 知识

覆盖率 **57%**（44/77）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`easy showTensorShape`、`INTConstant`、`BlockifyMask`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`VHS_VideoInfo`、`Frame Select`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`DF_Get_image_size`、`WanVideoClipVisionEncode`、`Sam2Segmentation`、`AILab_MaskPreview`、`RH_Translator`、`VHS_LoadVideo`、`DownloadAndLoadSAM2Model`、`Textbox`、`LoadImage`、`WanVideoTextEncodeCached`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
