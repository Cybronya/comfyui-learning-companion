---
key: 平台全量/换脸视频+动作迁移视频Wan2.2_1997227928914169858.json
name: 换脸视频+动作迁移视频Wan2.2_1997227928914169858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/换脸视频+动作迁移视频Wan2.2_1997227928914169858.json
hash: e85ab35086c786aa
coverage: 0.638889
learned_at: 2026-11-14 02:08:41
nodes: [MathExpression|pysssss, SetNode, SetNode, SetNode, Int, LoadImage, VHS_LoadVideo, Int, GrowMask, BlockifyMask, DrawMaskOnImage, LayerMask: SegformerB2ClothesUltra, GetNode, PreviewImage, SetNode, SetNode, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, WanVideoBlockSwap, GetNode, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, PixelPerfectResolution, ImageResizeKJv2, GetNode, ImageCropByMaskAndResize, SetNode, FaceMaskFromPoseKeypoints, DWPreprocessor, Reroute, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoDecode, easy cleanGpuUsed, GetNode, WanVideoSampler, VHS_VideoInfo, JWInteger, SetNode, SetNode, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, Int, Int, CR Text, MathExpression|pysssss, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 平台全量/换脸视频+动作迁移视频Wan2.2_1997227928914169858.json

> 来源文件 `comfyui_library/workflows/平台全量/换脸视频+动作迁移视频Wan2.2_1997227928914169858.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `LoadImage`
- `VHS_LoadVideo`
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
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **64%**（46/72）

**有卡**：`MathExpression|pysssss`、`Int`、`LoadImage`、`VHS_LoadVideo`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`LayerMask: SegformerB2ClothesUltra`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoSampler`、`VHS_VideoInfo`、`JWInteger`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
