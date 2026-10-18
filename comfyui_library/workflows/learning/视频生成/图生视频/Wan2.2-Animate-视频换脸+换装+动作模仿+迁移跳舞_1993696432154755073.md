---
key: 视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json
name: Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json
hash: 17e9c84a0a6863c6
coverage: 0.714286
learned_at: 2026-10-15 22:33:19
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, VHS_VideoCombine, WanVideoSampler, Note, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM, WanVideoTextEncodeCached, FaceMaskFromPoseKeypoints, ImageResizeKJv2, PixelPerfectResolution, DWPreprocessor, WanVideoClipVisionEncode, GrowMask, BlockifyMask, DrawMaskOnImage, ImageCropByMaskAndResize, PreviewImage, LayerMask: SegformerB2ClothesUltra, Reroute, Reroute, JWInteger, JWInteger, JWInteger, WanVideoBlockSwap, LayerUtility: PurgeVRAM, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, CLIPVisionLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993696432154755073.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoAnimateEmbeds`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncodeCached`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `WanVideoClipVisionEncode`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageCropByMaskAndResize`
- `PreviewImage`
- `LayerMask: SegformerB2ClothesUltra`
- `Reroute`
- `Reroute`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`LayerUtility: PurgeVRAM`、`WanVideoTextEncodeCached`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoClipVisionEncode`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageCropByMaskAndResize`、`LayerMask: SegformerB2ClothesUltra`、`JWInteger`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
