---
key: 视频生成/图生视频/wan2.2-Animate局部重绘+视频转绘_1969957827202719745.json
name: wan2.2-Animate局部重绘+视频转绘_1969957827202719745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969957827202719745.json
hash: c4c1113301aa1487
coverage: 0.965909
learned_at: 2026-10-15 22:31:51
nodes: [VHS_VideoCombine, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, DrawMaskOnImage, PixelPerfectResolution, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, DWPreprocessor, AudioCropProcessUTK, Sam2Segmentation, DownloadAndLoadSAM2Model, ImageConcatMulti, ImageConcatMulti, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoModelLoader, ImageResizeKJv2, PreviewImage, WanVideoBlockSwap, GrowMaskWithBlur, PointsEditor, LoadImage, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoClipVisionEncode, GetImageRangeFromBatch, GetImageSizeAndCount, AudioCropProcessUTK, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, Int, INTConstant, VHS_VideoCombine, VHS_LoadVideo, Int, PreviewImage, CLIPVisionLoader, WanVideoSampler, DWPreprocessor, CM_IntToFloat, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, PixelPerfectResolution, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PreviewImage, Int, ImageFromBatch, ImageResizeKJv2, LoadImage, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, WanVideoDecode, VHS_LoadVideo, Int, Int, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, MathExpression|pysssss, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), WanVideoTextEncodeCached, INTConstant, BlockifyMask, CM_IntToFloat, CR Text, WanVideoAnimateEmbeds, Switch any [Crystools], Text, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, Fast Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Animate局部重绘+视频转绘_1969957827202719745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969957827202719745.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（88 个）：
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `DrawMaskOnImage`
- `PixelPerfectResolution`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `DWPreprocessor`
- `AudioCropProcessUTK`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoBlockSwap`
- `GrowMaskWithBlur`
- `PointsEditor`
- `LoadImage`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `AudioCropProcessUTK`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `Int`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Int`
- `PreviewImage`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `DWPreprocessor`
- `CM_IntToFloat`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `PreviewImage`
- `Int`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `Int`
- `Int`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `MathExpression|pysssss`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `BlockifyMask`
- `CM_IntToFloat`
- `CR Text`
- `WanVideoAnimateEmbeds`
- `Switch any [Crystools]`
- `Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `Fast Bypasser (rgthree)`

## 知识

覆盖率 **97%**（85/88）

**有卡**：`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`DrawMaskOnImage`、`PixelPerfectResolution`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`DWPreprocessor`、`AudioCropProcessUTK`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`GrowMaskWithBlur`、`PointsEditor`、`LoadImage`、`Int`、`INTConstant`、`VHS_LoadVideo`、`CM_IntToFloat`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`ImageFromBatch`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`BlockifyMask`、`CR Text`、`Switch any [Crystools]`、`Text`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
