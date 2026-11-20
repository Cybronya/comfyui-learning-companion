---
key: 平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2033978370362445825.json
name: 动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2033978370362445825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2033978370362445825.json
hash: fd7f678a662f69a1
coverage: 0.648649
learned_at: 2026-11-14 01:44:28
nodes: [GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageCropByMaskAndResize, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoVAELoader, SetNode, WanVideoSetBlockSwap, Int, MathExpression|pysssss, SetNode, GetNode, DrawMaskOnImage, ImageConcatMulti, ImageConcatMulti, Int, Int, SetNode, SetNode, GetNode, GrowMask, BlockifyMask, SetNode, SetNode, SetNode, SetNode, GetNode, LayerMask: SegformerB2ClothesUltra, GetNode, RMBG, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, CR Text, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Int, ImageResizeKJv2, WanVideoLoraSelectMulti, TT_img_enc_v2, LayerUtility: PurgeVRAM V2, SaveImage, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoInfo, DWPreprocessor, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2033978370362445825.json

> 来源文件 `comfyui_library/workflows/平台全量/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上） (1)_2033978370362445825.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（74 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `GetNode`
- `ImageCropByMaskAndResize`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
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
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
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
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `RMBG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `Int`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `TT_img_enc_v2`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **65%**（48/74）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`Int`、`MathExpression|pysssss`、`DrawMaskOnImage`、`ImageConcatMulti`、`GrowMask`、`BlockifyMask`、`LayerMask: SegformerB2ClothesUltra`、`RMBG`、`ImageResizeKJv2`、`VHS_VideoCombine`、`CR Text`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`TT_img_enc_v2`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`easy cleanGpuUsed`、`VHS_VideoInfo`、`DWPreprocessor`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
