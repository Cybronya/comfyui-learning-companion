---
key: 平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2026731459997868033.json
name: 动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2026731459997868033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2026731459997868033.json
hash: 6b1a7cef5f88680c
coverage: 0.638889
learned_at: 2026-11-14 01:44:27
nodes: [GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoVAELoader, SetNode, WanVideoSetBlockSwap, Int, MathExpression|pysssss, Int, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, Int, SetNode, SetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, SetNode, GetNode, LayerMask: SegformerB2ClothesUltra, GetNode, RMBG, ImageResizeKJv2, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, SetNode, ImageResizeKJv2, SetNode, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti, CR Text, LoadImage, WanVideoLoraSelectMulti, Int, VHS_LoadVideo, easy cleanGpuUsed]
patterns: []
missing: []
---

# 平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2026731459997868033.json

> 来源文件 `comfyui_library/workflows/平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2026731459997868033.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
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
- `WanVideoSetBlockSwap`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoInfo`
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
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `RMBG`
- `ImageResizeKJv2`
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
- `WanVideoLoraSelectMulti`
- `CR Text`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `Int`
- `VHS_LoadVideo`
- `easy cleanGpuUsed`

## 知识

覆盖率 **64%**（46/72）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`Int`、`MathExpression|pysssss`、`DrawMaskOnImage`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VHS_VideoInfo`、`GrowMask`、`BlockifyMask`、`LayerMask: SegformerB2ClothesUltra`、`RMBG`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`CR Text`、`LoadImage`、`VHS_LoadVideo`、`easy cleanGpuUsed`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
