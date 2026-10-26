---
key: 数字人/数字人/wan-2.2-人物替换-V3_2059239614648508418.json
name: wan-2.2-人物替换-V3_2059239614648508418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan-2.2-人物替换-V3_2059239614648508418.json
hash: b3cde14d940714c6
coverage: 0.523364
learned_at: 2026-10-26 01:59:24
nodes: [Primitive integer [Crystools], Primitive integer [Crystools], Int, easy sam3ModelLoader, SimpleMath+, VHS_VideoInfo, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation, WanVideoLoraSelectMulti, PreviewAny, PreviewAny, easy sam3GetObjectIds, VHS_VideoCombine, MaskToImage, easy sam3Visualization, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoAnimateEmbeds, GrowMaskWithBlur, WanVideoSetLoRAs, WanVideoContextOptions, WanVideoTextEncodeCached, BlockifyMask, WanVideoSampler, DrawMaskOnImage, WanVideoTeaCache, MemoryCleaner, OnnxDetectionModelLoader, MemoryCleaner, GetImageSizeAndCount, WanVideoDecode, ImageBlend, PoseAndFaceDetection, DrawViTPose, ZML_AnyTypeSwitchFive, PreviewImage, VHS_LoadVideo, ImageResizeKJv2, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, MemoryCleaner, SeedVR2ExtraArgs, SeedVR2BlockSwap, VHS_VideoCombine, PreviewImage, GetNode, GetNode, ImageResizeKJv2, SimpleMath+, Int, Int, Int, VHS_LoadVideo, LoadImage, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, SeedVR2]
patterns: []
missing: []
---

# 数字人/数字人/wan-2.2-人物替换-V3_2059239614648508418.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan-2.2-人物替换-V3_2059239614648508418.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（107 个）：
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Int`
- `easy sam3ModelLoader`
- `SimpleMath+`
- `VHS_VideoInfo`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`
- `WanVideoLoraSelectMulti`
- `PreviewAny`
- `PreviewAny`
- `easy sam3GetObjectIds`
- `VHS_VideoCombine`
- `MaskToImage`
- `easy sam3Visualization`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `GrowMaskWithBlur`
- `WanVideoSetLoRAs`
- `WanVideoContextOptions`
- `WanVideoTextEncodeCached`
- `BlockifyMask`
- `WanVideoSampler` ★核心
- `DrawMaskOnImage`
- `WanVideoTeaCache`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `MemoryCleaner`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageBlend`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ZML_AnyTypeSwitchFive`
- `PreviewImage`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `MemoryCleaner`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SimpleMath+`
- `Int`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SeedVR2`

## 知识

覆盖率 **52%**（56/107）

**有卡**：`Primitive integer [Crystools]`、`Int`、`easy sam3ModelLoader`、`SimpleMath+`、`VHS_VideoInfo`、`easy sam3VideoModelExtraConfig`、`easy sam3VideoSegmentation`、`WanVideoLoraSelectMulti`、`easy sam3GetObjectIds`、`VHS_VideoCombine`、`MaskToImage`、`easy sam3Visualization`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`GrowMaskWithBlur`、`WanVideoSetLoRAs`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`BlockifyMask`、`WanVideoSampler`、`DrawMaskOnImage`、`WanVideoTeaCache`、`MemoryCleaner`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageBlend`、`PoseAndFaceDetection`、`DrawViTPose`、`ZML_AnyTypeSwitchFive`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`CLIPVisionLoader`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`SeedVR2`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs、WanVideoSampler、WanVideoDecode、WanVideoVAELoader
