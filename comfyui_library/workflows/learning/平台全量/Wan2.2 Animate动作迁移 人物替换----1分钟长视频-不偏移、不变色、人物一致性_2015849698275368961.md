---
key: 平台全量/Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961.json
name: Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961.json
hash: 483ed701f65d36df
coverage: 0.558333
learned_at: 2026-11-14 01:05:13
nodes: [WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, LoadImage, SetNode, WanVideoBlockSwap, WanVideoSampler, WanVideoModelLoader, GetNode, GetNode, WanVideoTeaCache, WanVideoContextOptions, PreviewImage, SetNode, GetNode, CLIPVisionLoader, GetNode, ImageResizeKJv2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, SetNode, MemoryCleaner, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, MaskToImage, easy sam3GetObjectIds, PreviewAny, PreviewAny, MemoryCleaner, WanVideoAnimateEmbeds, SetNode, GetNode, SetNode, BlockifyMask, DrawMaskOnImage, GrowMaskWithBlur, WanVideoTextEncodeCached, MemoryCleaner, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, GetNode, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, SetNode, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, Int, Int, SDPoseOODProcessor, GetImageSizeAndCount, PoseAndFaceDetection, DrawViTPose, ImpactSwitch, SetNode, GetNode, GetNode, easy sam3VideoSegmentation, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, GetNode, easy sam3Visualization, YOLOModelLoader, SDPoseOODLoader, OnnxDetectionModelLoader, GetNode, ImageBlend, ZML_AnyTypeSwitchFive, SetNode, INTConstant, INTConstant, INTConstant, easy anythingIndexSwitch, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, SetNode, SetNode, Int, Int, easy anythingIndexSwitch, INTConstant, GetNode, SetNode, SetNode, SetNode, SimpleMath+, SimpleMath+, Primitive integer [Crystools], Primitive integer [Crystools], GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, VHS_VideoInfo, SetNode, SetNode, SetNode, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（120 个）：
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
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
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `SetNode`
- `MemoryCleaner`
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
- `WanVideoTextEncodeCached`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `SDPoseOODProcessor`
- `GetImageSizeAndCount`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ImpactSwitch`
- `SetNode`
- `GetNode`
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
- `OnnxDetectionModelLoader`
- `GetNode`
- `ImageBlend`
- `ZML_AnyTypeSwitchFive`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `easy anythingIndexSwitch`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `easy anythingIndexSwitch`
- `INTConstant`
- `GetNode`
- `SetNode`
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
- `VHS_LoadVideo`

## 知识

覆盖率 **56%**（67/120）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoContextOptions`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`MemoryCleaner`、`easy sam3ModelLoader`、`easy sam3VideoModelExtraConfig`、`WanVideoDecode`、`MaskToImage`、`easy sam3GetObjectIds`、`WanVideoAnimateEmbeds`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMaskWithBlur`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`VHS_LoadVideo`、`VHS_VideoCombine`、`Int`、`SDPoseOODProcessor`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`DrawViTPose`、`easy sam3VideoSegmentation`、`easy sam3Visualization`、`YOLOModelLoader`、`SDPoseOODLoader`、`OnnxDetectionModelLoader`、`ImageBlend`、`ZML_AnyTypeSwitchFive`、`INTConstant`、`easy anythingIndexSwitch`、`SimpleMath+`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`VHS_VideoInfo`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
