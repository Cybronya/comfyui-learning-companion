---
key: 视频生成/图生视频/wan-2.2-人物替换-V5_2067889293686820865.json
name: wan-2.2-人物替换-V5_2067889293686820865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067889293686820865.json
hash: e97a14ad3f935e45
coverage: 0.527778
learned_at: 2026-10-15 22:40:14
nodes: [Primitive integer [Crystools], Primitive integer [Crystools], Int, easy sam3ModelLoader, SimpleMath+, VHS_VideoInfo, easy sam3VideoModelExtraConfig, WanVideoLoraSelectMulti, PreviewAny, PreviewAny, easy sam3GetObjectIds, VHS_VideoCombine, MaskToImage, easy sam3Visualization, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoAnimateEmbeds, GrowMaskWithBlur, WanVideoSetLoRAs, WanVideoContextOptions, WanVideoTextEncodeCached, BlockifyMask, WanVideoSampler, DrawMaskOnImage, WanVideoTeaCache, MemoryCleaner, OnnxDetectionModelLoader, MemoryCleaner, GetImageSizeAndCount, WanVideoDecode, ImageBlend, PoseAndFaceDetection, DrawViTPose, PreviewImage, VHS_LoadVideo, ImageResizeKJv2, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, MemoryCleaner, VHS_VideoCombine, PreviewImage, GetNode, GetNode, ImageResizeKJv2, SimpleMath+, Int, Int, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, ZML_AnyTypeSwitchFive, ZML_AnyTypeSwitchFive, SeedVR2ExtraArgs, SeedVR2BlockSwap, SeedVR2, Int, easy sam3VideoSegmentation, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan-2.2-人物替换-V5_2067889293686820865.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067889293686820865.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（108 个）：
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Int`
- `easy sam3ModelLoader`
- `SimpleMath+`
- `VHS_VideoInfo`
- `easy sam3VideoModelExtraConfig`
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
- `VHS_VideoCombine`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SimpleMath+`
- `Int`
- `Int`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `ZML_AnyTypeSwitchFive`
- `ZML_AnyTypeSwitchFive`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `Int`
- `easy sam3VideoSegmentation`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **53%**（57/108）

**有卡**：`Primitive integer [Crystools]`、`Int`、`easy sam3ModelLoader`、`SimpleMath+`、`VHS_VideoInfo`、`easy sam3VideoModelExtraConfig`、`WanVideoLoraSelectMulti`、`easy sam3GetObjectIds`、`VHS_VideoCombine`、`MaskToImage`、`easy sam3Visualization`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`GrowMaskWithBlur`、`WanVideoSetLoRAs`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`BlockifyMask`、`WanVideoSampler`、`DrawMaskOnImage`、`WanVideoTeaCache`、`MemoryCleaner`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageBlend`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`ZML_AnyTypeSwitchFive`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SeedVR2`、`easy sam3VideoSegmentation`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs、WanVideoSampler、WanVideoDecode、WanVideoVAELoader
