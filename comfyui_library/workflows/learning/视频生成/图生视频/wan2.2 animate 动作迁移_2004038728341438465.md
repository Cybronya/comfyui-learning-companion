---
key: 视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json
name: wan2.2 animate 动作迁移_2004038728341438465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json
hash: c480b5bd95dc239b
coverage: 0.64
learned_at: 2026-10-15 22:33:52
nodes: [ttN float, SetNode, WanVideoVAELoader, WanVideoDecode, easy cleanGpuUsed, WanVideoClipVisionEncode, VHS_VideoCombine, ttN float, WanVideoSampler, GetNode, CLIPVisionLoader, WanVideoTextEncodeCached, Note, GetNode, GetNode, GetNode, SetNode, LoadImage, SetNode, JWInteger, ImageResizeKJv2, JWInteger, GetNode, SetNode, SetNode, GetNode, GetNode, Text, SetNode, ttN float, PrimitiveInt, SimpleMath+, PixelPerfectResolution, GetNode, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoAnimateEmbeds, DWPreprocessor, WanVideoModelLoader, GetNode, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004038728341438465.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `ttN float`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `ttN float`
- `WanVideoSampler` ★核心
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `JWInteger`
- `ImageResizeKJv2`
- `JWInteger`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Text`
- `SetNode`
- `ttN float`
- `PrimitiveInt`
- `SimpleMath+`
- `PixelPerfectResolution`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `WanVideoAnimateEmbeds`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VHS_LoadVideo`

## 知识

覆盖率 **64%**（32/50）

**有卡**：`ttN float`、`WanVideoVAELoader`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`LoadImage`、`JWInteger`、`ImageResizeKJv2`、`Text`、`SimpleMath+`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoAnimateEmbeds`、`DWPreprocessor`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
