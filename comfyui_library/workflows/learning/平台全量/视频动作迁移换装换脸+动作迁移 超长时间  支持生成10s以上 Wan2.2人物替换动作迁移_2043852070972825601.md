---
key: 平台全量/视频动作迁移换装换脸+动作迁移 超长时间  支持生成10s以上 Wan2.2人物替换动作迁移_2043852070972825601.json
name: 视频动作迁移换装换脸+动作迁移 超长时间  支持生成10s以上 Wan2.2人物替换动作迁移_2043852070972825601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频动作迁移换装换脸+动作迁移 超长时间  支持生成10s以上 Wan2.2人物替换动作迁移_2043852070972825601.json
hash: fdb9831bf235f358
coverage: 0.628571
learned_at: 2026-11-14 02:35:47
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, MathExpression|pysssss, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, SetNode, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, Int, SetNode, SetNode, GetNode, GetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, Int, Int, Int, LayerMask: SegformerB2ClothesUltra, GetNode, PreviewImage, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, LoadImage, CR Text, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频动作迁移换装换脸+动作迁移 超长时间  支持生成10s以上 Wan2.2人物替换动作迁移_2043852070972825601.json

> 来源文件 `comfyui_library/workflows/平台全量/视频动作迁移换装换脸+动作迁移 超长时间  支持生成10s以上 Wan2.2人物替换动作迁移_2043852070972825601.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（70 个）：
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
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Int`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `VHS_LoadVideo`

## 知识

覆盖率 **63%**（44/70）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`Int`、`GrowMask`、`BlockifyMask`、`VHS_VideoCombine`、`LayerMask: SegformerB2ClothesUltra`、`LoadImage`、`CR Text`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
