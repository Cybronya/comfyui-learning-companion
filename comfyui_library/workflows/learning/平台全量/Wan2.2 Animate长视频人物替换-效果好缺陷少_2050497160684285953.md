---
key: 平台全量/Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953.json
name: Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953.json
hash: 062bf6feebde89a5
coverage: 0.522523
learned_at: 2026-11-14 01:05:26
nodes: [WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, SetNode, WanVideoBlockSwap, WanVideoSampler, WanVideoModelLoader, GetNode, GetNode, WanVideoTeaCache, WanVideoContextOptions, PreviewImage, SetNode, GetNode, CLIPVisionLoader, GetNode, ImageResizeKJv2, WanVideoLoraSelectMulti, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, MaskToImage, easy sam3GetObjectIds, PreviewAny, PreviewAny, MemoryCleaner, WanVideoAnimateEmbeds, SetNode, GetNode, SetNode, BlockifyMask, DrawMaskOnImage, GrowMaskWithBlur, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, GetNode, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, Int, ImpactSwitch, GetNode, easy sam3VideoSegmentation, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, GetNode, easy sam3Visualization, YOLOModelLoader, SDPoseOODLoader, ZML_AnyTypeSwitchFive, SetNode, Int, GetNode, SetNode, SetNode, SimpleMath+, SimpleMath+, Primitive integer [Crystools], Primitive integer [Crystools], GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, OnnxDetectionModelLoader, PoseAndFaceDetection, WanVideoTextEncodeCached, MemoryCleaner, SetNode, MemoryCleaner, SetNode, GetNode, DrawViTPose, PreviewImage, Int, Int, Int, Int, SDPoseOODProcessor, PreviewImage, WanVideoLoraSelectMulti, WanVideoVAELoader, LoadImage, GetNode, ImageBlend, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（111 个）：
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `WanVideoContextOptions`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `easy sam3ModelLoader`
- `easy sam3VideoModelExtraConfig`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `MaskToImage`
- `easy sam3GetObjectIds`
- `PreviewAny`
- `PreviewAny`
- `MemoryCleaner`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `GetNode`
- `SetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `ImpactSwitch`
- `GetNode`
- `easy sam3VideoSegmentation`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `easy sam3Visualization`
- `YOLOModelLoader`
- `SDPoseOODLoader`
- `ZML_AnyTypeSwitchFive`
- `SetNode`
- `Int`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `WanVideoTextEncodeCached`
- `MemoryCleaner`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `GetNode`
- `DrawViTPose`
- `PreviewImage`
- `Int`
- `Int`
- `Int`
- `Int`
- `SDPoseOODProcessor`
- `PreviewImage`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `LoadImage`
- `GetNode`
- `ImageBlend`
- `VHS_LoadVideo`

## 知识

覆盖率 **52%**（58/111）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoContextOptions`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`easy sam3ModelLoader`、`easy sam3VideoModelExtraConfig`、`WanVideoDecode`、`MaskToImage`、`easy sam3GetObjectIds`、`MemoryCleaner`、`WanVideoAnimateEmbeds`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMaskWithBlur`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`VHS_LoadVideo`、`VHS_VideoCombine`、`Int`、`easy sam3VideoSegmentation`、`easy sam3Visualization`、`YOLOModelLoader`、`SDPoseOODLoader`、`ZML_AnyTypeSwitchFive`、`SimpleMath+`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`VHS_VideoInfo`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoTextEncodeCached`、`DrawViTPose`、`SDPoseOODProcessor`、`WanVideoVAELoader`、`LoadImage`、`ImageBlend`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
