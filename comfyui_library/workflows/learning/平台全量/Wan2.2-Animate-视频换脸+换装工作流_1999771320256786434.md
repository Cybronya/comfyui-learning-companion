---
key: 平台全量/Wan2.2-Animate-视频换脸+换装工作流_1999771320256786434.json
name: Wan2.2-Animate-视频换脸+换装工作流_1999771320256786434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate-视频换脸+换装工作流_1999771320256786434.json
hash: 1c51f858e6cce529
coverage: 0.697674
learned_at: 2026-11-14 01:05:55
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, Note, LayerUtility: PurgeVRAM, WanVideoTextEncodeCached, FaceMaskFromPoseKeypoints, ImageResizeKJv2, DWPreprocessor, WanVideoClipVisionEncode, GrowMask, BlockifyMask, DrawMaskOnImage, ImageCropByMaskAndResize, LayerMask: SegformerB2ClothesUltra, Note, Reroute, Reroute, JWInteger, WanVideoBlockSwap, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoLoraSelect, GetNode, GetNode, JWInteger, WanVideoAnimateEmbeds, VHS_VideoCombine, VHS_LoadVideo, WanVideoSampler, SetNode, JWInteger, PixelPerfectResolution, PreviewImage, CLIPVisionLoader, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Animate-视频换脸+换装工作流_1999771320256786434.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate-视频换脸+换装工作流_1999771320256786434.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `Note`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncodeCached`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `WanVideoClipVisionEncode`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageCropByMaskAndResize`
- `LayerMask: SegformerB2ClothesUltra`
- `Note`
- `Reroute`
- `Reroute`
- `JWInteger`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `JWInteger`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `SetNode`
- `JWInteger`
- `PixelPerfectResolution`
- `PreviewImage`
- `CLIPVisionLoader`
- `LoadImage`

## 知识

覆盖率 **70%**（30/43）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoTextEncodeCached`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`DWPreprocessor`、`WanVideoClipVisionEncode`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageCropByMaskAndResize`、`LayerMask: SegformerB2ClothesUltra`、`JWInteger`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoSampler`、`PixelPerfectResolution`、`CLIPVisionLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
