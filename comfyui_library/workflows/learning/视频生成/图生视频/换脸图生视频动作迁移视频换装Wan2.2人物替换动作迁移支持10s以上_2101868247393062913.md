---
key: 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json
name: 换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json
hash: cdd32e2124c9cc51
coverage: 0.630137
learned_at: 2026-10-17 02:15:04
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CR Text, Int, MathExpression|pysssss, Int, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, SetNode, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, Int, Int, SetNode, SetNode, GetNode, GetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, PreviewImage, GetNode, LayerMask: SegformerB2ClothesUltra, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VHS_LoadVideo, LoadImage, VHS_VideoCombine, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（73 个）：
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
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `LayerMask: SegformerB2ClothesUltra`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **63%**（46/73）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`CR Text`、`Int`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`GrowMask`、`BlockifyMask`、`LayerMask: SegformerB2ClothesUltra`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`EmptyImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
