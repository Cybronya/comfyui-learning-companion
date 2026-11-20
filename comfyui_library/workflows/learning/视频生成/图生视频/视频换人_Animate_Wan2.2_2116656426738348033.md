---
key: 视频生成/图生视频/视频换人_Animate_Wan2.2_2116656426738348033.json
name: 视频换人_Animate_Wan2.2_2116656426738348033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频换人_Animate_Wan2.2_2116656426738348033.json
hash: 09cc0a8a3fdf8a66
coverage: 0.566667
learned_at: 2026-11-02 19:19:56
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, DWPreprocessor, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, FaceMaskFromPoseKeypoints, SetNode, CLIPVisionLoader, Reroute, GetNode, GetNode, SetNode, easy cleanGpuUsed, VHS_VideoInfo, SetNode, ImageConcatMulti, ImageResizeKJv2, ImageConcatMulti, ImageResizeKJv2, BlockifyMask, DrawMaskOnImage, GetNode, GrowMask, LayerUtility: PurgeVRAM, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoModelLoader, LayerMask: SegformerB2ClothesUltra, SetNode, SetNode, SetNode, VHS_VideoCombine, GetNode, JWInteger, JWInteger, LoadImage, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/视频换人_Animate_Wan2.2_2116656426738348033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/视频换人_Animate_Wan2.2_2116656426738348033.json`

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
- `easy cleanGpuUsed`
- `VHS_VideoInfo`
- `SetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `LayerMask: SegformerB2ClothesUltra`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **57%**（34/60）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`FaceMaskFromPoseKeypoints`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`VHS_VideoInfo`、`ImageConcatMulti`、`ImageResizeKJv2`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`LayerMask: SegformerB2ClothesUltra`、`VHS_VideoCombine`、`JWInteger`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
