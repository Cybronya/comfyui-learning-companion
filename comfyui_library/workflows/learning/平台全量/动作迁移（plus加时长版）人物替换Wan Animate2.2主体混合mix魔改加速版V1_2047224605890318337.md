---
key: 平台全量/动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337.json
name: 动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337.json
hash: e5b2666b6b2a416c
coverage: 0.541667
learned_at: 2026-11-14 01:46:06
nodes: [Reroute, FaceMaskFromPoseKeypoints, SetNode, Note, GetNode, GetNode, GetImageSizeAndCount, WanVideoSetBlockSwap, DWPreprocessor, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, GetNode, GetImageSizeAndCount, WanVideoLoraSelectMulti, WanVideoModelLoader, ImageCropByMaskAndResize, Note, WanVideoUni3C_embeds, JWInteger, WanVideoDecode, GetNode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, SetNode, SetNode, JWInteger, PixelPerfectResolution, WanVideoTorchCompileSettings, WanVideoSetLoRAs, SetNode, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, GrowMask, BlockifyMask, RMBG, VHS_LoadVideo, PreviewImage, GetNode, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SetNode, LoadImage, Note, Note, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoTextEncodeCached, PrimitiveStringMultiline, MarkdownNote, SetNode, CLIPVisionLoader, WanVideoVAELoader, SetNode, WanVideoBlockSwap, SetNode, JWInteger, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, WanVideoContextOptions, GetNode, VHS_VideoCombine, MathExpression|pysssss, DF_Int_to_Float, SetNode, SetNode, WanVideoClipVisionEncode, WanVideoEncode]
patterns: []
missing: []
---

# 平台全量/动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（96 个）：
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `DWPreprocessor`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `ImageCropByMaskAndResize`
- `Note`
- `WanVideoUni3C_embeds`
- `JWInteger`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `SetNode`
- `SetNode`
- `JWInteger`
- `PixelPerfectResolution`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `BlockifyMask`
- `RMBG`
- `VHS_LoadVideo`
- `PreviewImage`
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `LoadImage`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoContextOptions`
- `GetNode`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `DF_Int_to_Float`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`

## 知识

覆盖率 **54%**（52/96）

**有卡**：`FaceMaskFromPoseKeypoints`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`DWPreprocessor`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`ImageCropByMaskAndResize`、`WanVideoUni3C_embeds`、`JWInteger`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`PixelPerfectResolution`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMask`、`BlockifyMask`、`RMBG`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`ImageConcatMulti`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`MathExpression|pysssss`、`DF_Int_to_Float`、`WanVideoClipVisionEncode`、`WanVideoEncode`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
