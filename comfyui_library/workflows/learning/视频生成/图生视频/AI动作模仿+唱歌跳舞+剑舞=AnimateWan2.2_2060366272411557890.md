---
key: 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2060366272411557890.json
name: AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2060366272411557890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2060366272411557890.json
hash: 7f4b80717c8acf91
coverage: 0.818182
learned_at: 2026-10-15 22:38:48
nodes: [CLIPVisionLoader, JWInteger, SetNode, GetNode, VHS_LoadVideo, JWInteger, GetNode, GetNode, VHS_VideoCombine, ttN float, ttN float, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, ttN float, ImageCropByMaskAndResize, VHS_VideoInfo, FaceMaskFromPoseKeypoints, PixelPerfectResolution, DWPreprocessor, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, WanVideoModelLoader, Text, ImageResizeKJv2, CLIPVisionLoader, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSampler, SetNode, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, SimpleMath+, easy cleanGpuUsed, ImageFromBatch, LoadImage, Note, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2060366272411557890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060366272411557890.json`

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
- `LoadImage`
- `Note`
- `PrimitiveInt`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`CLIPVisionLoader`、`JWInteger`、`VHS_LoadVideo`、`VHS_VideoCombine`、`ttN float`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageCropByMaskAndResize`、`VHS_VideoInfo`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`DWPreprocessor`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`Text`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageFromBatch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
