---
key: 平台全量/换装视频换装Wan2.2换装人物替换动作迁移（支持10s）_1972851274611904513.json
name: 换装视频换装Wan2.2换装人物替换动作迁移（支持10s）_1972851274611904513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/换装视频换装Wan2.2换装人物替换动作迁移（支持10s）_1972851274611904513.json
hash: 303ca1c6a3b61a73
coverage: 0.625
learned_at: 2026-11-14 02:09:27
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageResizeKJv2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, SetNode, JWInteger, JWInteger, SetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, SetNode, Reroute, GetNode, WanVideoBlockSwap, GetNode, GetNode, GetNode, SetNode, WanVideoTextEncodeCached, LoadImage, ImageResizeKJv2, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CR Text, VHS_LoadVideo, Int, MathExpression|pysssss, Int, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, SetNode, easy cleanGpuUsed, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyImage, BlockifyMask, GrowMask, Int, Int, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_VideoCombine, GetNode, LayerMask: SegformerB2ClothesUltra]
patterns: []
missing: []
---

# 平台全量/换装视频换装Wan2.2换装人物替换动作迁移（支持10s）_1972851274611904513.json

> 来源文件 `comfyui_library/workflows/平台全量/换装视频换装Wan2.2换装人物替换动作迁移（支持10s）_1972851274611904513.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（72 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `SetNode`
- `Reroute`
- `GetNode`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `CR Text`
- `VHS_LoadVideo`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `BlockifyMask`
- `GrowMask`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `LayerMask: SegformerB2ClothesUltra`

## 知识

覆盖率 **62%**（45/72）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`LoadImage`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`CR Text`、`VHS_LoadVideo`、`Int`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`EmptyImage`、`BlockifyMask`、`GrowMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: SegformerB2ClothesUltra`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
