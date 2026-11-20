---
key: 平台全量/抖音爆火武侠Animate wan2.2_1999710374268108801.json
name: 抖音爆火武侠Animate wan2.2_1999710374268108801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/抖音爆火武侠Animate wan2.2_1999710374268108801.json
hash: c5326c0f130ab11a
coverage: 0.939394
learned_at: 2026-11-14 02:05:54
nodes: [ImageCropByMaskAndResize, WanVideoSetLoRAs, WanVideoSetBlockSwap, JWInteger, JWInteger, WanVideoAnimateEmbeds, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoDecode, FaceMaskFromPoseKeypoints, VHS_VideoInfo, WanVideoModelLoader, ImageResizeKJv2, DWPreprocessor, WanVideoVAELoader, LayerUtility: PurgeVRAM, WanVideoTextEncodeCached, PixelPerfectResolution, WanVideoLoraSelectMulti, Note, LoadImage, VHS_LoadVideo, Text, CLIPVisionLoader, CLIPVisionLoader, VHS_VideoCombine, Reroute, easy cleanGpuUsed]
patterns: []
missing: []
---

# 平台全量/抖音爆火武侠Animate wan2.2_1999710374268108801.json

> 来源文件 `comfyui_library/workflows/平台全量/抖音爆火武侠Animate wan2.2_1999710374268108801.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `ImageCropByMaskAndResize`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `JWInteger`
- `JWInteger`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `FaceMaskFromPoseKeypoints`
- `VHS_VideoInfo`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncodeCached`
- `PixelPerfectResolution`
- `WanVideoLoraSelectMulti`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`
- `Text`
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `Reroute`
- `easy cleanGpuUsed`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`JWInteger`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`FaceMaskFromPoseKeypoints`、`VHS_VideoInfo`、`WanVideoModelLoader`、`ImageResizeKJv2`、`DWPreprocessor`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`PixelPerfectResolution`、`WanVideoLoraSelectMulti`、`LoadImage`、`VHS_LoadVideo`、`Text`、`CLIPVisionLoader`、`VHS_VideoCombine`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
