---
key: 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json
name: AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json
hash: e70833a4c9945221
coverage: 0.8
learned_at: 2026-10-15 22:31:48
nodes: [CLIPVisionLoader, Note, JWInteger, SetNode, GetNode, VHS_LoadVideo, JWInteger, GetNode, GetNode, VHS_VideoCombine, ttN float, ttN float, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, ttN float, ImageCropByMaskAndResize, VHS_VideoInfo, PrimitiveInt, FaceMaskFromPoseKeypoints, PixelPerfectResolution, DWPreprocessor, Note, LoadImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, WanVideoModelLoader, Text, ImageResizeKJv2, CLIPVisionLoader, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSampler, SetNode, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, SimpleMath+, easy cleanGpuUsed, ImageFromBatch]
patterns: []
missing: []
---

# 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969244065881595906.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `CLIPVisionLoader`
- `Note`
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
- `PrimitiveInt`
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

## 知识

覆盖率 **80%**（36/45）

**有卡**：`CLIPVisionLoader`、`JWInteger`、`VHS_LoadVideo`、`VHS_VideoCombine`、`ttN float`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageCropByMaskAndResize`、`VHS_VideoInfo`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`DWPreprocessor`、`LoadImage`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`Text`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageFromBatch`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
