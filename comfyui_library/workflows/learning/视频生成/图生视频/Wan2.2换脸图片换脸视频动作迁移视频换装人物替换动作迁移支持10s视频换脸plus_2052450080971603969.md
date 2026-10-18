---
key: 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json
name: Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json
hash: a5dd3fc6ab4581c3
coverage: 0.638889
learned_at: 2026-10-15 22:37:30
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CR Text, Int, MathExpression|pysssss, Int, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, SetNode, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, Int, SetNode, SetNode, GetNode, GetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, PreviewImage, GetNode, VHS_VideoCombine, LoadImage, LoadImage, VHS_VideoCombine, LoadImage, SetNode, LayerMask: SegformerB2ClothesUltra, GetNode, SetNode, Int, SetNode, SetNode, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052450080971603969.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `JWInteger`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `Reroute`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `CR Text`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **64%**（46/72）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`CR Text`、`Int`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`GrowMask`、`BlockifyMask`、`VHS_VideoCombine`、`LoadImage`、`LayerMask: SegformerB2ClothesUltra`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
