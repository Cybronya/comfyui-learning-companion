---
key: 视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json
name: 🦖Wan Animate2.2换主体_1970311265270853633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json
hash: dd2002917d8442ee
coverage: 0.623529
learned_at: 2026-10-15 22:49:14
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, Note, WanVideoSampler, GetNode, VHS_VideoCombine, WanVideoUni3C_embeds, Note, WanVideoTextEncodeCached, WanVideoDecode, ResizeLongestToNode, ImageGetSize, GetNode, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, VHS_LoadVideo, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, SetNode, JWInteger, CR Prompt Text, VHS_LoadVideo, PixelPerfectResolution, SetNode, ImageGetSize, SimpleMath+, Bjornulf_ShowInt, JWInteger, SetNode, JWInteger, PointsEditor, VHS_VideoCombine, SetNode, GetImageSizeAndCount, WanVideoModelLoader, ImageResize, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（85 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
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
- `DWPreprocessor`
- `Sam2Segmentation`
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
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoClipVisionEncode`
- `Note`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoUni3C_embeds`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `ResizeLongestToNode`
- `ImageGetSize`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `SetNode`
- `JWInteger`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `PixelPerfectResolution`
- `SetNode`
- `ImageGetSize`
- `SimpleMath+`
- `Bjornulf_ShowInt`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `PointsEditor`
- `VHS_VideoCombine`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `ImageResize`
- `LoadImage`

## 知识

覆盖率 **62%**（53/85）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ResizeLongestToNode`、`ImageGetSize`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`CR Prompt Text`、`PixelPerfectResolution`、`SimpleMath+`、`Bjornulf_ShowInt`、`PointsEditor`、`WanVideoModelLoader`、`ImageResize`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
