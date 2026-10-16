---
key: 视频生成/图生视频/最强视频换装+Animate+Wan2.2_1985660962449629185.json
name: 最强视频换装+Animate+Wan2.2_1985660962449629185.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985660962449629185.json
hash: 7f38a5ac2a6ec973
coverage: 0.566667
learned_at: 2026-10-15 22:32:52
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, SetNode, ImageCropByMaskAndResize, LayerUtility: PurgeVRAM, FaceMaskFromPoseKeypoints, Reroute, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, easy cleanGpuUsed, JWInteger, JWInteger, SetNode, VHS_LoadVideo, GetNode, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadImage, SetNode, ImageResizeKJv2, VHS_VideoInfo, DrawMaskOnImage, SetNode, SetNode, ImageConcatMulti, VHS_VideoCombine, SetNode, GetNode, DWPreprocessor, LayerUtility: PurgeVRAM, WanVideoBlockSwap, BlockifyMask, CLIPVisionLoader, LayerMask: SegformerB2ClothesUltra, GrowMask, GetNode, WanVideoVAELoader, VHS_VideoCombine, WanVideoSampler, WanVideoModelLoader, ImageConcatMulti, SetNode, ImageResizeKJv2, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/最强视频换装+Animate+Wan2.2_1985660962449629185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985660962449629185.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
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
- `easy cleanGpuUsed`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `VHS_LoadVideo`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadImage`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_VideoInfo`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `DWPreprocessor`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `BlockifyMask`
- `CLIPVisionLoader`
- `LayerMask: SegformerB2ClothesUltra`
- `GrowMask`
- `GetNode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `ImageConcatMulti`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **57%**（34/60）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`FaceMaskFromPoseKeypoints`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`JWInteger`、`VHS_LoadVideo`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`ImageResizeKJv2`、`VHS_VideoInfo`、`DrawMaskOnImage`、`ImageConcatMulti`、`VHS_VideoCombine`、`DWPreprocessor`、`WanVideoBlockSwap`、`BlockifyMask`、`CLIPVisionLoader`、`LayerMask: SegformerB2ClothesUltra`、`GrowMask`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
