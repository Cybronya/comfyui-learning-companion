---
key: 视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json
name: AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json
hash: 87532c481510b7e3
coverage: 0.818182
learned_at: 2026-10-17 00:02:03
nodes: [CLIPVisionLoader, JWInteger, SetNode, GetNode, VHS_LoadVideo, JWInteger, GetNode, GetNode, VHS_VideoCombine, ttN float, ttN float, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, ttN float, ImageCropByMaskAndResize, VHS_VideoInfo, FaceMaskFromPoseKeypoints, PixelPerfectResolution, DWPreprocessor, Note, LoadImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, WanVideoModelLoader, Text, ImageResizeKJv2, CLIPVisionLoader, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSampler, SetNode, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, SimpleMath+, easy cleanGpuUsed, ImageFromBatch, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `CLIPVisionLoader`
- `JWInteger`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `JWInteger`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ttN float`
- `ttN float`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ttN float`
- `ImageCropByMaskAndResize`
- `VHS_VideoInfo`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `Note`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoModelLoader`
- `Text`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `PrimitiveInt`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`CLIPVisionLoader`、`JWInteger`、`VHS_LoadVideo`、`VHS_VideoCombine`、`ttN float`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageCropByMaskAndResize`、`VHS_VideoInfo`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`DWPreprocessor`、`LoadImage`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`Text`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageFromBatch`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
