---
key: 视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json
name: 人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json
hash: 00cb2772c8bc9bb7
coverage: 0.822222
learned_at: 2026-10-15 22:36:54
nodes: [CLIPVisionLoader, JWInteger, SetNode, GetNode, JWInteger, GetNode, ttN float, ttN float, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, ttN float, ImageCropByMaskAndResize, VHS_VideoInfo, PrimitiveInt, FaceMaskFromPoseKeypoints, PixelPerfectResolution, DWPreprocessor, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, WanVideoModelLoader, ImageResizeKJv2, CLIPVisionLoader, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSampler, SetNode, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, SimpleMath+, easy cleanGpuUsed, ImageFromBatch, GetNode, Note, VHS_LoadVideo, LoadImage, VHS_VideoCombine, Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046042390951108610.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `CLIPVisionLoader`
- `JWInteger`
- `SetNode`
- `GetNode`
- `JWInteger`
- `GetNode`
- `ttN float`
- `ttN float`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ttN float`
- `ImageCropByMaskAndResize`
- `VHS_VideoInfo`
- `PrimitiveInt`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoModelLoader`
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
- `GetNode`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `Text`
- `LoadImage`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`CLIPVisionLoader`、`JWInteger`、`ttN float`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageCropByMaskAndResize`、`VHS_VideoInfo`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`DWPreprocessor`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageFromBatch`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`、`Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
