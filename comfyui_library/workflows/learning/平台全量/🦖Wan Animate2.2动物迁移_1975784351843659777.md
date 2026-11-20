---
key: 平台全量/🦖Wan Animate2.2动物迁移_1975784351843659777.json
name: 🦖Wan Animate2.2动物迁移_1975784351843659777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🦖Wan Animate2.2动物迁移_1975784351843659777.json
hash: 26ed151452dc519c
coverage: 0.605634
learned_at: 2026-11-14 02:55:46
nodes: [GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, BlockifyMask, SetNode, Note, GetNode, SetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, Sam2Segmentation, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, Note, WanVideoSampler, VHS_VideoCombine, WanVideoUni3C_embeds, WanVideoModelLoader, Note, WanVideoTextEncodeCached, WanVideoDecode, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, SetNode, SetNode, ImageResizeKJv2, SetNode, VHS_VideoCombine, SetNode, VHS_VideoCombine, SetNode, SetNode, Reroute, PixelPerfectResolution, WanVideoClipVisionEncode, AnimalPosePreprocessor, ImageConcatMulti, GetNode, ImageConcatMulti, GrowMask, SimpleMath+, Bjornulf_ShowInt, VHS_LoadVideo, JWInteger, CR Prompt Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, SetNode, SetNode, PointsEditor, VHS_VideoCombine, GetNode]
patterns: []
missing: []
---

# 平台全量/🦖Wan Animate2.2动物迁移_1975784351843659777.json

> 来源文件 `comfyui_library/workflows/平台全量/🦖Wan Animate2.2动物迁移_1975784351843659777.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（71 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `BlockifyMask`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
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
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `Note`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoUni3C_embeds`
- `WanVideoModelLoader`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `Reroute`
- `PixelPerfectResolution`
- `WanVideoClipVisionEncode`
- `AnimalPosePreprocessor`
- `ImageConcatMulti`
- `GetNode`
- `ImageConcatMulti`
- `GrowMask`
- `SimpleMath+`
- `Bjornulf_ShowInt`
- `VHS_LoadVideo`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `GetNode`

## 知识

覆盖率 **61%**（43/71）

**有卡**：`DownloadAndLoadSAM2Model`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Sam2Segmentation`、`DrawMaskOnImage`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`PixelPerfectResolution`、`WanVideoClipVisionEncode`、`AnimalPosePreprocessor`、`ImageConcatMulti`、`GrowMask`、`SimpleMath+`、`Bjornulf_ShowInt`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`PointsEditor`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
