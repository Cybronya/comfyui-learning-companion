---
key: 平台全量/视频换人 Animate Wan2.2_2001286004759724034.json
name: 视频换人 Animate Wan2.2_2001286004759724034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频换人 Animate Wan2.2_2001286004759724034.json
hash: 06bf0cf57cd7a9e4
coverage: 0.557377
learned_at: 2026-11-14 02:38:11
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, DWPreprocessor, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, FaceMaskFromPoseKeypoints, SetNode, CLIPVisionLoader, Reroute, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, VHS_VideoInfo, SetNode, ImageConcatMulti, ImageResizeKJv2, JWInteger, JWInteger, ImageConcatMulti, VHS_VideoCombine, ImageResizeKJv2, BlockifyMask, DrawMaskOnImage, GetNode, GrowMask, LayerUtility: PurgeVRAM, SetNode, GetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoVAELoader, WanVideoBlockSwap, VHS_VideoCombine, WanVideoLoraSelectMulti, WanVideoSampler, LayerMask: SegformerB2ClothesUltra, WanVideoAnimateEmbeds, Note, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/视频换人 Animate Wan2.2_2001286004759724034.json

> 来源文件 `comfyui_library/workflows/平台全量/视频换人 Animate Wan2.2_2001286004759724034.json`

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
- `DWPreprocessor`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `VHS_VideoInfo`
- `SetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `LayerMask: SegformerB2ClothesUltra`
- `WanVideoAnimateEmbeds`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **56%**（34/61）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`FaceMaskFromPoseKeypoints`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`VHS_VideoInfo`、`ImageConcatMulti`、`ImageResizeKJv2`、`JWInteger`、`VHS_VideoCombine`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`LayerMask: SegformerB2ClothesUltra`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
