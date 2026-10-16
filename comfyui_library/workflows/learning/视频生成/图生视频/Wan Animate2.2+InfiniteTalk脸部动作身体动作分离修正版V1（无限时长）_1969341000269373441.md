---
key: 视频生成/图生视频/Wan Animate2.2+InfiniteTalk脸部动作身体动作分离修正版V1（无限时长）_1969341000269373441.json
name: Wan Animate2.2+InfiniteTalk脸部动作身体动作分离修正版V1（无限时长）_1969341000269373441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969341000269373441.json
hash: 7baedd46d8130030
coverage: 0.586957
learned_at: 2026-10-15 22:31:48
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, Sam2Segmentation, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoClipVisionEncode, PointsEditor, Note, WanVideoContextOptions, GetNode, VHS_VideoCombine, WanVideoUni3C_embeds, SetNode, DownloadAndLoadSAM2Model, ImageResizeKJv2, SetNode, VHS_VideoCombine, PixelPerfectResolution, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, Reroute, DWPreprocessor, WanVideoModelLoader, LoadImage, MultiTalkModelLoader, JWInteger, JWInteger, Note, CR Prompt Text, Note, AudioSeparation, AudioCrop, PreviewAny, DownloadAndLoadWav2VecModel, VHS_LoadVideo, VHS_LoadVideo, MultiTalkWav2VecEmbeds, WanVideoImageToVideoMultiTalk, WanVideoCombineEmbeds, Note, Note, VHS_VideoCombine, WanVideoSampler, JWInteger, Note, Note, CR Prompt Text, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2+InfiniteTalk脸部动作身体动作分离修正版V1（无限时长）_1969341000269373441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969341000269373441.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（92 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `Sam2Segmentation`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `PointsEditor`
- `Note`
- `WanVideoContextOptions`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoUni3C_embeds`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `Reroute`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `LoadImage`
- `MultiTalkModelLoader`
- `JWInteger`
- `JWInteger`
- `Note`
- `CR Prompt Text`
- `Note`
- `AudioSeparation`
- `AudioCrop`
- `PreviewAny`
- `DownloadAndLoadWav2VecModel`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `MultiTalkWav2VecEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoCombineEmbeds`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `JWInteger`
- `Note`
- `Note`
- `CR Prompt Text`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **59%**（54/92）

**有卡**：`ImageConcatMulti`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Sam2Segmentation`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`PointsEditor`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LoadImage`、`MultiTalkModelLoader`、`JWInteger`、`CR Prompt Text`、`AudioSeparation`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoCombineEmbeds`、`WanVideoSampler`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
