---
key: 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2030816272992178178.json
name: AI动作模仿+跳舞+剑舞=Animate wan2.2_2030816272992178178.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030816272992178178.json
hash: aa55a1e104f113c1
coverage: 0.818182
learned_at: 2026-10-15 22:35:27
nodes: [CLIPVisionLoader, FaceMaskFromPoseKeypoints, LayerUtility: PurgeVRAM, WanVideoDecode, LayerUtility: PurgeVRAM, PixelPerfectResolution, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoClipVisionEncode, ImageCropByMaskAndResize, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, SetNode, JWInteger, WanVideoVAELoader, ImageResizeKJv2, SetNode, LayerUtility: PurgeVRAM, easy cleanGpuUsed, WanVideoSampler, WanVideoBlockSwap, GetNode, VHS_VideoInfo, DWPreprocessor, VHS_LoadVideo, JWInteger, GetNode, GetNode, VHS_VideoCombine, ttN float, ttN float, LoadImage, SimpleMath+, SetNode, ttN float, PrimitiveInt, WanVideoAnimateEmbeds, WanVideoModelLoader, Text, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2030816272992178178.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030816272992178178.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
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
- `Note`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`CLIPVisionLoader`、`FaceMaskFromPoseKeypoints`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`PixelPerfectResolution`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`JWInteger`、`WanVideoVAELoader`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`DWPreprocessor`、`VHS_LoadVideo`、`VHS_VideoCombine`、`ttN float`、`LoadImage`、`SimpleMath+`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`Text`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
