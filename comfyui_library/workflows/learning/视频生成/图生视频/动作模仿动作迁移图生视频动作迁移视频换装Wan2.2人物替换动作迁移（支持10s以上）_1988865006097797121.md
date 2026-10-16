---
key: 视频生成/图生视频/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上）_1988865006097797121.json
name: 动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上）_1988865006097797121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988865006097797121.json
hash: 28ea7fa3231e97f0
coverage: 0.633803
learned_at: 2026-10-15 22:33:04
nodes: [GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CR Text, Int, MathExpression|pysssss, Int, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, Int, Int, SetNode, SetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_LoadVideo, LayerMask: SegformerB2ClothesUltra, GetNode, RMBG, ImageResizeKJv2, LoadImage, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, SetNode, ImageResizeKJv2, SetNode, PreviewImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上）_1988865006097797121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988865006097797121.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（71 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `GetNode`
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
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `RMBG`
- `ImageResizeKJv2`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **63%**（45/71）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`CR Text`、`Int`、`MathExpression|pysssss`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`GrowMask`、`BlockifyMask`、`VHS_LoadVideo`、`LayerMask: SegformerB2ClothesUltra`、`RMBG`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
