---
key: 数字人/数字人/dnf_scail.json_2081553214935228418.json
name: dnf_scail.json_2081553214935228418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/dnf_scail.json_2081553214935228418.json
hash: 1d414a09653b4d45
coverage: 0.575758
learned_at: 2026-10-26 01:58:31
nodes: [GetNode, GetNode, GetImageSizeAndCount, GetNode, DrawMaskOnImage, WanVideoDecode, SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoSetLoRAs, BlockifyMask, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, WanVideoBlockSwap, SetNode, MathExpression|pysssss, DF_Int_to_Float, SetNode, SetNode, LayerUtility: PurgeVRAM V2, JWInteger, CLIPVisionLoader, WanVideoVAELoader, Reroute, WanVideoModelLoader, PixelPerfectResolution, GrowMask, WanVideoTextEncodeCached, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM V2, GetNode, SetNode, RMBG, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, DWPreprocessor, ImageCropByMaskAndResize, WanVideoSampler, SetNode, FaceMaskFromPoseKeypoints, SetNode, SetNode, GetNode, LayerUtility: PurgeVRAM V2, ImageConcatMulti, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, WanVideoAnimateEmbeds, JWInteger, VHS_LoadVideo, JWInteger, JWInteger, JWInteger, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/dnf_scail.json_2081553214935228418.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/dnf_scail.json_2081553214935228418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `DrawMaskOnImage`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `MathExpression|pysssss`
- `DF_Int_to_Float`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `JWInteger`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `Reroute`
- `WanVideoModelLoader`
- `PixelPerfectResolution`
- `GrowMask`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `SetNode`
- `RMBG`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `WanVideoSampler` ★核心
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `WanVideoAnimateEmbeds`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **58%**（38/66）

**有卡**：`GetImageSizeAndCount`、`DrawMaskOnImage`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`BlockifyMask`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`DF_Int_to_Float`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`PixelPerfectResolution`、`GrowMask`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`RMBG`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`ImageConcatMulti`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
