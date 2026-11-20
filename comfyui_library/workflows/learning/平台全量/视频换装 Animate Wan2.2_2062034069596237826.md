---
key: 平台全量/视频换装 Animate Wan2.2_2062034069596237826.json
name: 视频换装 Animate Wan2.2_2062034069596237826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频换装 Animate Wan2.2_2062034069596237826.json
hash: 9b20633a346ff977
coverage: 0.580645
learned_at: 2026-11-14 02:39:06
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, JWInteger, SetNode, GetNode, LoadImage, GetNode, LoadImage, GrowMask, BlockifyMask, GetNode, LayerMask: SegformerB2ClothesUltra, SetNode, GetNode, SetNode, DrawMaskOnImage, LayerUtility: PurgeVRAM, SetNode, WanVideoModelLoader, WanVideoVAELoader, Reroute, SetNode, FaceMaskFromPoseKeypoints, LayerUtility: PurgeVRAM, DWPreprocessor, PixelPerfectResolution, SetNode, ImageConcatMulti, ImageConcatMulti, SetNode, ImageCropByMaskAndResize, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoClipVisionEncode, easy cleanGpuUsed, SetNode, WanVideoSampler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, CLIPVisionLoader, WanVideoLoraSelectMulti, JWInteger, Float, WanVideoTextEncodeCached, VHS_VideoInfo, WanVideoBlockSwap, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/视频换装 Animate Wan2.2_2062034069596237826.json

> 来源文件 `comfyui_library/workflows/平台全量/视频换装 Animate Wan2.2_2062034069596237826.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（62 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `JWInteger`
- `SetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `LoadImage`
- `GrowMask`
- `BlockifyMask`
- `GetNode`
- `LayerMask: SegformerB2ClothesUltra`
- `SetNode`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `Reroute`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `LayerUtility: PurgeVRAM`
- `DWPreprocessor`
- `PixelPerfectResolution`
- `SetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `ImageCropByMaskAndResize`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `JWInteger`
- `Float`
- `WanVideoTextEncodeCached`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 知识

覆盖率 **58%**（36/62）

**有卡**：`WanVideoDecode`、`WanVideoAnimateEmbeds`、`JWInteger`、`LoadImage`、`GrowMask`、`BlockifyMask`、`LayerMask: SegformerB2ClothesUltra`、`DrawMaskOnImage`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`WanVideoVAELoader`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`PixelPerfectResolution`、`ImageConcatMulti`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`WanVideoSampler`、`VHS_LoadVideo`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`Float`、`WanVideoTextEncodeCached`、`VHS_VideoInfo`、`WanVideoBlockSwap`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
