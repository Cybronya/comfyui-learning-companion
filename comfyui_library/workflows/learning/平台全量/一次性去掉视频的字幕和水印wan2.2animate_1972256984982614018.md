---
key: 平台全量/一次性去掉视频的字幕和水印wan2.2animate_1972256984982614018.json
name: 一次性去掉视频的字幕和水印wan2.2animate_1972256984982614018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一次性去掉视频的字幕和水印wan2.2animate_1972256984982614018.json
hash: a3d3a3ac6a8d72cb
coverage: 0.550725
learned_at: 2026-11-14 01:27:04
nodes: [SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, SetNode, GetNode, SetNode, GetNode, SetNode, DownloadAndLoadGIMMVFIModel, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, SetNode, ImageConcatMulti, GetNode, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, GetImageSizeAndCount, DrawMaskOnImage, SetNode, easy showTensorShape, easy showTensorShape, SetNode, SetNode, INTConstant, INTConstant, INTConstant, BlockifyMask, VHS_VideoCombine, easy showTensorShape, GetNode, GetNode, GetNode, GetNode, GIMMVFI_interpolate, easy showAnything, VHS_VideoCombine, WanVideoSampler, WanVideoAnimateEmbeds, DF_Get_image_size, WanVideoClipVisionEncode, GetNode, PreviewImage, GetNode, SetNode, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, RH_Translator, VHS_LoadVideo, Textbox, LoadImage, WanVideoTextEncodeCached, MarkdownNote, ImageResizeKJv2, RHHiddenNodes]
patterns: []
missing: []
---

# 平台全量/一次性去掉视频的字幕和水印wan2.2animate_1972256984982614018.json

> 来源文件 `comfyui_library/workflows/平台全量/一次性去掉视频的字幕和水印wan2.2animate_1972256984982614018.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（69 个）：
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
- `SetNode`
- `easy showTensorShape`
- `easy showTensorShape`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `BlockifyMask`
- `VHS_VideoCombine`
- `easy showTensorShape`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `easy showAnything`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `DF_Get_image_size`
- `WanVideoClipVisionEncode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `RH_Translator`
- `VHS_LoadVideo`
- `Textbox`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `MarkdownNote`
- `ImageResizeKJv2`
- `RHHiddenNodes`

## 知识

覆盖率 **55%**（38/69）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`DrawMaskOnImage`、`easy showTensorShape`、`INTConstant`、`BlockifyMask`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`DF_Get_image_size`、`WanVideoClipVisionEncode`、`RH_Translator`、`VHS_LoadVideo`、`Textbox`、`LoadImage`、`WanVideoTextEncodeCached`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
