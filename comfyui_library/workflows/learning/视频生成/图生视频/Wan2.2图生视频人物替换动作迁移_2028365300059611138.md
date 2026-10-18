---
key: 视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json
name: Wan2.2图生视频人物替换动作迁移_2028365300059611138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json
hash: 219d7f83c1437368
coverage: 0.633803
learned_at: 2026-10-15 22:35:19
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, MathExpression|pysssss, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, SetNode, easy cleanGpuUsed, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, SetNode, GetNode, LoadImage, GetNode, PreviewImage, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, SetNode, LayerUtility: ImageScaleByAspectRatio V2, Int, CR Text, LayerMask: SegformerB2ClothesUltra, LoadImage, Int, Int, Int, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2028365300059611138.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（71 个）：
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
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `CR Text`
- `LayerMask: SegformerB2ClothesUltra`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`

## 知识

覆盖率 **63%**（45/71）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`ImageConcatMulti`、`VHS_VideoInfo`、`GrowMask`、`BlockifyMask`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`CR Text`、`LayerMask: SegformerB2ClothesUltra`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
