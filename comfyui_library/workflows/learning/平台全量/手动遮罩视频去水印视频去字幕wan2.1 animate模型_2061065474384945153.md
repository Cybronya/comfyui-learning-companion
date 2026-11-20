---
key: 平台全量/手动遮罩视频去水印视频去字幕wan2.1 animate模型_2061065474384945153.json
name: 手动遮罩视频去水印视频去字幕wan2.1 animate模型_2061065474384945153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/手动遮罩视频去水印视频去字幕wan2.1 animate模型_2061065474384945153.json
hash: 12e99dc9d5a6b3c2
coverage: 0.645161
learned_at: 2026-11-14 02:04:48
nodes: [GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, Bookmark (rgthree), Bookmark (rgthree), SetNode, Primitive integer [Crystools], GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, GetImageSizeAndCount, ImageResizeKJv2, easy showTensorShape, VHS_VideoInfo, DF_Get_image_size, Frame Select, ImageResizeKJv2, INTConstant, INTConstant, SetNode, SetNode, PreviewImage, SimpleMath+, SetNode, Primitive integer [Crystools], SimpleMath+, SetNode, SetNode, Primitive integer [Crystools], Textbox, WanVideoSampler, SetNode, SetNode, SetNode, easy showTensorShape, SetNode, ImageResizeKJv2, PreviewImage, SetNode, easy showTensorShape, easy cleanGpuUsed, Sam2Segmentation, BlockifyMask, RHHiddenNodes, easy cleanGpuUsed, AILab_MaskPreview, SetNode, DrawMaskOnImage, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, SetNode, PreviewImage, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoVAELoader, SetNode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoSetBlockSwap, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, easy showAnything, LayerUtility: PurgeVRAM V2, RHHiddenNodes, GetNode, GetNode, easy cleanGpuUsed, RH_Translator, VHS_LoadVideo, LoadImage, PointsEditor, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, WanVideoAnimateEmbeds]
patterns: []
missing: []
---

# 平台全量/手动遮罩视频去水印视频去字幕wan2.1 animate模型_2061065474384945153.json

> 来源文件 `comfyui_library/workflows/平台全量/手动遮罩视频去水印视频去字幕wan2.1 animate模型_2061065474384945153.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（93 个）：
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `SetNode`
- `Primitive integer [Crystools]`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `easy showTensorShape`
- `VHS_VideoInfo`
- `DF_Get_image_size`
- `Frame Select`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SimpleMath+`
- `SetNode`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `Textbox`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showTensorShape`
- `SetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `easy showTensorShape`
- `easy cleanGpuUsed`
- `Sam2Segmentation`
- `BlockifyMask`
- `RHHiddenNodes`
- `easy cleanGpuUsed`
- `AILab_MaskPreview`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `RH_Translator`
- `VHS_LoadVideo`
- `LoadImage`
- `PointsEditor`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`

## 知识

覆盖率 **65%**（60/93）

**有卡**：`ImageConcatMulti`、`Bookmark (rgthree)`、`Primitive integer [Crystools]`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`easy showTensorShape`、`VHS_VideoInfo`、`DF_Get_image_size`、`Frame Select`、`INTConstant`、`SimpleMath+`、`Textbox`、`WanVideoSampler`、`easy cleanGpuUsed`、`Sam2Segmentation`、`BlockifyMask`、`RHHiddenNodes`、`AILab_MaskPreview`、`DrawMaskOnImage`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`RH_Translator`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`、`WanVideoAnimateEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs、CLIPVisionLoader
