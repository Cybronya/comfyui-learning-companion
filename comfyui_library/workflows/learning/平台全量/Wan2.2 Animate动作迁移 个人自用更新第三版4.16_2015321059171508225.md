---
key: 平台全量/Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225.json
name: Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225.json
hash: 16fe19a715859825
coverage: 0.578947
learned_at: 2026-11-14 01:05:12
nodes: [WanVideoSetBlockSwap, SetNode, GetNode, WanVideoSetLoRAs, SetNode, GetNode, VHS_VideoInfo, SetNode, SetNode, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, SetNode, SetNode, WanVideoVAELoader, VHS_VideoCombine, MemoryCleaner, WanVideoBlockSwap, MemoryCleaner, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoDecode, SetNode, SetNode, SetNode, SetNode, PreviewImage, GetNode, MemoryCleaner, GetNode, GetNode, WanVideoContextOptions, WanVideoTeaCache, SetNode, LoadImage, Int, Int, ImageResizeKJv2, MuyeTextEditOutput, SetNode, SetNode, GetNode, GetNode, GetNode, SDPoseOODProcessor, GetNode, YOLOModelLoader, SDPoseOODLoader, GetImageSizeAndCount, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, SetNode, ImpactSwitch, ZML_AnyTypeSwitchFive, SetNode, SetNode, INTConstant, INTConstant, INTConstant, easy anythingIndexSwitch, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, easy anythingIndexSwitch, SetNode, SetNode, VHS_LoadVideo, easy float, Int, SimpleMath+, SimpleMath+, MuyeTextEditOutput, MuyeTextEditOutput, Primitive integer [Crystools], easy float, INTConstant, Primitive integer [Crystools], Int]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（95 个）：
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `MemoryCleaner`
- `WanVideoBlockSwap`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoTeaCache`
- `SetNode`
- `LoadImage`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `MuyeTextEditOutput`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseOODProcessor`
- `GetNode`
- `YOLOModelLoader`
- `SDPoseOODLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `ImpactSwitch`
- `ZML_AnyTypeSwitchFive`
- `SetNode`
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
- `easy anythingIndexSwitch`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `easy float`
- `Int`
- `SimpleMath+`
- `SimpleMath+`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `Primitive integer [Crystools]`
- `easy float`
- `INTConstant`
- `Primitive integer [Crystools]`
- `Int`

## 知识

覆盖率 **58%**（55/95）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`VHS_VideoInfo`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`VHS_VideoCombine`、`MemoryCleaner`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoContextOptions`、`WanVideoTeaCache`、`LoadImage`、`Int`、`ImageResizeKJv2`、`MuyeTextEditOutput`、`SDPoseOODProcessor`、`YOLOModelLoader`、`SDPoseOODLoader`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ZML_AnyTypeSwitchFive`、`INTConstant`、`easy anythingIndexSwitch`、`VHS_LoadVideo`、`easy float`、`SimpleMath+`、`Primitive integer [Crystools]`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
