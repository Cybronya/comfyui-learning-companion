---
key: 平台全量/换脸视频+动作迁移视频Wan2.2_2067197085480480770.json
name: 换脸视频+动作迁移视频Wan2.2_2067197085480480770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/换脸视频+动作迁移视频Wan2.2_2067197085480480770.json
hash: 1f5eac175d9d464e
coverage: 0.628571
learned_at: 2026-11-14 02:08:41
nodes: [MathExpression|pysssss, SetNode, SetNode, SetNode, Int, Int, GrowMask, BlockifyMask, DrawMaskOnImage, LayerMask: SegformerB2ClothesUltra, GetNode, PreviewImage, SetNode, SetNode, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, WanVideoBlockSwap, GetNode, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, PixelPerfectResolution, ImageResizeKJv2, GetNode, ImageCropByMaskAndResize, SetNode, FaceMaskFromPoseKeypoints, DWPreprocessor, Reroute, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoDecode, easy cleanGpuUsed, GetNode, WanVideoSampler, VHS_VideoInfo, JWInteger, SetNode, SetNode, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, Int, Int, CR Text, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/换脸视频+动作迁移视频Wan2.2_2067197085480480770.json

> 来源文件 `comfyui_library/workflows/平台全量/换脸视频+动作迁移视频Wan2.2_2067197085480480770.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（70 个）：
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `PixelPerfectResolution`
- `ImageResizeKJv2`
- `GetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `Reroute`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoInfo`
- `JWInteger`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `CR Text`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **63%**（44/70）

**有卡**：`MathExpression|pysssss`、`Int`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`LayerMask: SegformerB2ClothesUltra`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoSampler`、`VHS_VideoInfo`、`JWInteger`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
