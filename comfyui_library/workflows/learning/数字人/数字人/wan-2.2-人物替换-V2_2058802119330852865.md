---
key: 数字人/数字人/wan-2.2-人物替换-V2_2058802119330852865.json
name: wan-2.2-人物替换-V2_2058802119330852865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan-2.2-人物替换-V2_2058802119330852865.json
hash: 8f49e39141072fe9
coverage: 0.504854
learned_at: 2026-10-26 01:59:23
nodes: [Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, Int, easy sam3ModelLoader, SimpleMath+, Int, VHS_VideoInfo, Int, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation, ImageResizeKJv2, PreviewImage, WanVideoLoraSelectMulti, PreviewAny, PreviewAny, WanVideoLoraSelectMulti, easy sam3GetObjectIds, VHS_VideoCombine, MaskToImage, CLIPVisionLoader, easy sam3Visualization, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoModelLoader, WanVideoVAELoader, GrowMaskWithBlur, MemoryCleaner, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoContextOptions, WanVideoTextEncodeCached, BlockifyMask, WanVideoSetBlockSwap, WanVideoSampler, DrawMaskOnImage, WanVideoTeaCache, MemoryCleaner, OnnxDetectionModelLoader, MemoryCleaner, GetImageSizeAndCount, WanVideoDecode, ImageBlend, PoseAndFaceDetection, VHS_VideoCombine, DrawViTPose, ZML_AnyTypeSwitchFive, PreviewImage, VHS_LoadVideo, ImageResizeKJv2, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/wan-2.2-人物替换-V2_2058802119330852865.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan-2.2-人物替换-V2_2058802119330852865.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（103 个）：
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `Int`
- `easy sam3ModelLoader`
- `SimpleMath+`
- `Int`
- `VHS_VideoInfo`
- `Int`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoLoraSelectMulti`
- `PreviewAny`
- `PreviewAny`
- `WanVideoLoraSelectMulti`
- `easy sam3GetObjectIds`
- `VHS_VideoCombine`
- `MaskToImage`
- `CLIPVisionLoader`
- `easy sam3Visualization`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `GrowMaskWithBlur`
- `MemoryCleaner`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoTextEncodeCached`
- `BlockifyMask`
- `WanVideoSetBlockSwap`
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
- `VHS_VideoCombine`
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
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **50%**（52/103）

**有卡**：`Primitive integer [Crystools]`、`SimpleMath+`、`Int`、`easy sam3ModelLoader`、`VHS_VideoInfo`、`easy sam3VideoModelExtraConfig`、`easy sam3VideoSegmentation`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`easy sam3GetObjectIds`、`VHS_VideoCombine`、`MaskToImage`、`CLIPVisionLoader`、`easy sam3Visualization`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`WanVideoVAELoader`、`GrowMaskWithBlur`、`MemoryCleaner`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`BlockifyMask`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`DrawMaskOnImage`、`WanVideoTeaCache`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageBlend`、`PoseAndFaceDetection`、`DrawViTPose`、`ZML_AnyTypeSwitchFive`、`VHS_LoadVideo`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
