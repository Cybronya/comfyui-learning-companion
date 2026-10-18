---
key: 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json
name: 图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json
hash: fd21014634dbd3ff
coverage: 0.837209
learned_at: 2026-10-15 22:37:01
nodes: [CLIPVisionLoader, FaceMaskFromPoseKeypoints, LayerUtility: PurgeVRAM, WanVideoDecode, LayerUtility: PurgeVRAM, PixelPerfectResolution, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoClipVisionEncode, ImageCropByMaskAndResize, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, SetNode, JWInteger, WanVideoVAELoader, ImageResizeKJv2, SetNode, LayerUtility: PurgeVRAM, easy cleanGpuUsed, WanVideoSampler, WanVideoBlockSwap, GetNode, VHS_VideoInfo, DWPreprocessor, VHS_LoadVideo, JWInteger, GetNode, GetNode, VHS_VideoCombine, ttN float, ttN float, LoadImage, SimpleMath+, SetNode, ttN float, PrimitiveInt, WanVideoAnimateEmbeds, WanVideoModelLoader, Text, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046830049172656129.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `CLIPVisionLoader`
- `FaceMaskFromPoseKeypoints`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `PixelPerfectResolution`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `ImageCropByMaskAndResize`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `JWInteger`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `GetNode`
- `VHS_VideoInfo`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `JWInteger`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ttN float`
- `ttN float`
- `LoadImage`
- `SimpleMath+`
- `SetNode`
- `ttN float`
- `PrimitiveInt`
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `Text`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`CLIPVisionLoader`、`FaceMaskFromPoseKeypoints`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`PixelPerfectResolution`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`JWInteger`、`WanVideoVAELoader`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`DWPreprocessor`、`VHS_LoadVideo`、`VHS_VideoCombine`、`ttN float`、`LoadImage`、`SimpleMath+`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`Text`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
