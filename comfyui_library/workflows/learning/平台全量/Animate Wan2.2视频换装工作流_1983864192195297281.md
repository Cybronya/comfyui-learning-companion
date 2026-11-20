---
key: 平台全量/Animate Wan2.2视频换装工作流_1983864192195297281.json
name: Animate Wan2.2视频换装工作流_1983864192195297281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Animate Wan2.2视频换装工作流_1983864192195297281.json
hash: 9c8243f92c78e377
coverage: 0.566667
learned_at: 2026-11-14 00:18:05
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, GetNode, GetNode, GetNode, Reroute, easy cleanGpuUsed, GetNode, SetNode, GrowMask, DrawMaskOnImage, LayerUtility: PurgeVRAM, GetNode, GetNode, SetNode, BlockifyMask, WanVideoBlockSwap, WanVideoModelLoader, SetNode, ImageResizeKJv2, DWPreprocessor, SetNode, WanVideoVAELoader, WanVideoLoraSelectMulti, SetNode, SetNode, LayerUtility: PurgeVRAM, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, CLIPVisionLoader, ImageResizeKJv2, GetNode, JWInteger, JWInteger, SetNode, SetNode, SetNode, SetNode, LoadImage, LayerMask: SegformerB2ClothesUltra, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoClipVisionEncode, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoSampler, GetNode, WanVideoDecode, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Animate Wan2.2视频换装工作流_1983864192195297281.json

> 来源文件 `comfyui_library/workflows/平台全量/Animate Wan2.2视频换装工作流_1983864192195297281.json`

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
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `GrowMask`
- `DrawMaskOnImage`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `SetNode`
- `BlockifyMask`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LayerMask: SegformerB2ClothesUltra`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `VHS_LoadVideo`

## 知识

覆盖率 **57%**（34/60）

**有卡**：`PixelPerfectResolution`、`easy cleanGpuUsed`、`GrowMask`、`DrawMaskOnImage`、`LayerUtility: PurgeVRAM`、`BlockifyMask`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`ImageResizeKJv2`、`DWPreprocessor`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`JWInteger`、`LoadImage`、`LayerMask: SegformerB2ClothesUltra`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
