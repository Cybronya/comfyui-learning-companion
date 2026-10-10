---
key: 视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json
name: 🦖Wan Animate2.2换主体_1970311265270853633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json
hash: dd2002917d8442ee
coverage: 0.588235
learned_at: 2026-10-10 23:14:55
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, Note, WanVideoSampler, GetNode, VHS_VideoCombine, WanVideoUni3C_embeds, Note, WanVideoTextEncodeCached, WanVideoDecode, ResizeLongestToNode, ImageGetSize, GetNode, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, VHS_LoadVideo, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, SetNode, JWInteger, CR Prompt Text, VHS_LoadVideo, PixelPerfectResolution, SetNode, ImageGetSize, SimpleMath+, Bjornulf_ShowInt, JWInteger, SetNode, JWInteger, PointsEditor, VHS_VideoCombine, SetNode, GetImageSizeAndCount, WanVideoModelLoader, ImageResize, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **59%**（50/85）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ResizeLongestToNode`、`ImageGetSize`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`JWInteger`、`PixelPerfectResolution`、`Bjornulf_ShowInt`、`PointsEditor`、`WanVideoModelLoader`、`ImageResize`、`LoadImage`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
