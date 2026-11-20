---
key: 平台全量/神气科技-视频换装 Animate Wan2.2_1991356413186277377.json
name: 神气科技-视频换装 Animate Wan2.2_1991356413186277377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/神气科技-视频换装 Animate Wan2.2_1991356413186277377.json
hash: 225fcde66ca34964
coverage: 0.557377
learned_at: 2026-11-14 02:27:19
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, SetNode, ImageCropByMaskAndResize, LayerUtility: PurgeVRAM, FaceMaskFromPoseKeypoints, Reroute, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, Note, easy cleanGpuUsed, JWInteger, JWInteger, SetNode, GetNode, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, ImageResizeKJv2, DrawMaskOnImage, SetNode, SetNode, ImageConcatMulti, SetNode, DWPreprocessor, LayerUtility: PurgeVRAM, WanVideoBlockSwap, BlockifyMask, CLIPVisionLoader, LayerMask: SegformerB2ClothesUltra, GrowMask, GetNode, WanVideoVAELoader, WanVideoSampler, WanVideoModelLoader, ImageConcatMulti, SetNode, ImageResizeKJv2, WanVideoLoraSelectMulti, VHS_VideoInfo, VHS_VideoCombine, VHS_VideoCombine, GetNode, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/神气科技-视频换装 Animate Wan2.2_1991356413186277377.json

> 来源文件 `comfyui_library/workflows/平台全量/神气科技-视频换装 Animate Wan2.2_1991356413186277377.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（61 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `LayerUtility: PurgeVRAM`
- `FaceMaskFromPoseKeypoints`
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `Note`
- `easy cleanGpuUsed`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `ImageResizeKJv2`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `ImageConcatMulti`
- `SetNode`
- `DWPreprocessor`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `BlockifyMask`
- `CLIPVisionLoader`
- `LayerMask: SegformerB2ClothesUltra`
- `GrowMask`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `ImageConcatMulti`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **56%**（34/61）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`FaceMaskFromPoseKeypoints`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`JWInteger`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`ImageConcatMulti`、`DWPreprocessor`、`WanVideoBlockSwap`、`BlockifyMask`、`CLIPVisionLoader`、`LayerMask: SegformerB2ClothesUltra`、`GrowMask`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoInfo`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
