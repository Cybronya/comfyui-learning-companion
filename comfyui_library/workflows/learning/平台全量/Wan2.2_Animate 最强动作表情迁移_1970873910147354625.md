---
key: 平台全量/Wan2.2_Animate 最强动作表情迁移_1970873910147354625.json
name: Wan2.2_Animate 最强动作表情迁移_1970873910147354625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2_Animate 最强动作表情迁移_1970873910147354625.json
hash: 643707b85d826f29
coverage: 0.463768
learned_at: 2026-11-14 01:06:13
nodes: [FaceMaskFromPoseKeypoints, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageCropByMaskAndResize, VHS_VideoInfo, WanVideoClipVisionEncode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, ImageConcatMulti, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, Note, WanVideoAnimateEmbeds, WanVideoSampler, PixelPerfectResolution, DWPreprocessor, LoadImage, VHS_LoadVideo, WanVideoModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, VHS_VideoCombine, JWInteger, JWInteger, VHS_VideoCombine, GetNode, GetNode, ImageResizeKJv2, WanVideoTextEncodeCached, Prompt_Text, ImageConcatMulti]
patterns: []
missing: []
---

# 平台全量/Wan2.2_Animate 最强动作表情迁移_1970873910147354625.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2_Animate 最强动作表情迁移_1970873910147354625.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（69 个）：
- `FaceMaskFromPoseKeypoints`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageCropByMaskAndResize`
- `VHS_VideoInfo`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `PixelPerfectResolution`
- `DWPreprocessor`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `Prompt_Text`
- `ImageConcatMulti`

## 知识

覆盖率 **46%**（32/69）

**有卡**：`FaceMaskFromPoseKeypoints`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageCropByMaskAndResize`、`VHS_VideoInfo`、`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`ImageConcatMulti`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`PixelPerfectResolution`、`DWPreprocessor`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`JWInteger`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`Prompt_Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
