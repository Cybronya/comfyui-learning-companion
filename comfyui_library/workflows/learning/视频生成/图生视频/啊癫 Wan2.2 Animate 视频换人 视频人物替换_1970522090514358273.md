---
key: 视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json
name: 啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1970522090514358273.json
hash: 0e76206dcfaf49ed
coverage: 0.566667
learned_at: 2026-10-15 22:31:53
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, DWPreprocessor, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, FaceMaskFromPoseKeypoints, SetNode, CLIPVisionLoader, Reroute, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, easy cleanGpuUsed, SetNode, ImageConcatMulti, ImageResizeKJv2, JWInteger, JWInteger, ImageConcatMulti, VHS_VideoCombine, ImageResizeKJv2, BlockifyMask, DrawMaskOnImage, LayerMask: SegformerB2ClothesUltra, GetNode, GrowMask, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoSampler, SetNode, GetNode, VHS_VideoCombine, WanVideoModelLoader, SetNode, SetNode, WanVideoSetLoRAs, WanVideoVAELoader, VHS_LoadVideo, LoadImage, VHS_VideoInfo]
patterns: []
missing: []
---

# 视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970522090514358273.json`

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
- `WanVideoLoraSelectMulti`
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
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
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
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `GrowMask`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoInfo`

## 知识

覆盖率 **57%**（34/60）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`FaceMaskFromPoseKeypoints`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`ImageConcatMulti`、`ImageResizeKJv2`、`JWInteger`、`VHS_VideoCombine`、`BlockifyMask`、`DrawMaskOnImage`、`LayerMask: SegformerB2ClothesUltra`、`GrowMask`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
