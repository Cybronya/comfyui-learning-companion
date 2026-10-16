---
key: 视频生成/文生视频/Wan2.2 Animate美女图片跳舞 视频动作迁移_1970282441866964994.json
name: Wan2.2 Animate美女图片跳舞 视频动作迁移_1970282441866964994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1970282441866964994.json
hash: 0572ad9a7bea58b1
coverage: 0.833333
learned_at: 2026-10-15 22:43:47
nodes: [CLIPVisionLoader, FaceMaskFromPoseKeypoints, DWPreprocessor, LayerUtility: PurgeVRAM, WanVideoDecode, LayerUtility: PurgeVRAM, PixelPerfectResolution, CLIPVisionLoader, ImageResizeKJv2, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoTextEncodeCached, ImageCropByMaskAndResize, WanVideoBlockSwap, VHS_VideoInfo, SetNode, SetNode, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoAnimateEmbeds, SetNode, GetNode, GetNode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, ImageResizeKJv2, ImageConcatMulti, WanVideoSampler, ImageConcatMulti, JWInteger, JWInteger, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, Text, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Animate美女图片跳舞 视频动作迁移_1970282441866964994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1970282441866964994.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `CLIPVisionLoader`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `PixelPerfectResolution`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `ImageCropByMaskAndResize`
- `WanVideoBlockSwap`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Text`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`CLIPVisionLoader`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`PixelPerfectResolution`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`ImageCropByMaskAndResize`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`ImageConcatMulti`、`WanVideoSampler`、`JWInteger`、`VHS_VideoCombine`、`Text`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
