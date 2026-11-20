---
key: 平台全量/视频去水印视频去字幕去除指定物品工作流基于wan2.2 animate_1978289406870183937.json
name: 视频去水印视频去字幕去除指定物品工作流基于wan2.2 animate_1978289406870183937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频去水印视频去字幕去除指定物品工作流基于wan2.2 animate_1978289406870183937.json
hash: 129818443e42d2be
coverage: 0.5875
learned_at: 2026-11-14 02:36:52
nodes: [SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, SetNode, GetNode, SetNode, GetNode, SetNode, DownloadAndLoadGIMMVFIModel, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, SetNode, ImageConcatMulti, GetNode, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, GetImageSizeAndCount, DrawMaskOnImage, OnnxDetectionModelLoader, SetNode, easy showTensorShape, easy showTensorShape, Reroute, SetNode, SetNode, INTConstant, INTConstant, INTConstant, BlockifyMask, MarkdownNote, easy showTensorShape, GetNode, GetNode, GetNode, GetNode, GIMMVFI_interpolate, easy showAnything, VHS_VideoCombine, VHS_VideoInfo, ImageResizeKJv2, Frame Select, WanVideoSampler, WanVideoAnimateEmbeds, DF_Get_image_size, WanVideoClipVisionEncode, GetNode, Sam2Segmentation, PreviewImage, GetNode, SetNode, ImageResizeKJv2, PreviewImage, AILab_MaskPreview, RH_Translator, VHS_LoadVideo, DownloadAndLoadSAM2Model, LoadImage, WanVideoTextEncodeCached, MarkdownNote, Bookmark (rgthree), PointsEditor, Bookmark (rgthree), VHS_VideoCombine, VHS_VideoCombine, Bookmark (rgthree), Textbox]
patterns: []
missing: []
---

# 平台全量/视频去水印视频去字幕去除指定物品工作流基于wan2.2 animate_1978289406870183937.json

> 来源文件 `comfyui_library/workflows/平台全量/视频去水印视频去字幕去除指定物品工作流基于wan2.2 animate_1978289406870183937.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
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
- `ImageResizeKJv2`
- `PreviewImage`
- `AILab_MaskPreview`
- `RH_Translator`
- `VHS_LoadVideo`
- `DownloadAndLoadSAM2Model`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `MarkdownNote`
- `Bookmark (rgthree)`
- `PointsEditor`
- `Bookmark (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Bookmark (rgthree)`
- `Textbox`

## 知识

覆盖率 **59%**（47/80）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`easy showTensorShape`、`INTConstant`、`BlockifyMask`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`VHS_VideoInfo`、`Frame Select`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`DF_Get_image_size`、`WanVideoClipVisionEncode`、`Sam2Segmentation`、`AILab_MaskPreview`、`RH_Translator`、`VHS_LoadVideo`、`DownloadAndLoadSAM2Model`、`LoadImage`、`WanVideoTextEncodeCached`、`Bookmark (rgthree)`、`PointsEditor`、`Textbox`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
