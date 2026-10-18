---
key: 视频生成/图生视频/首尾帧变身+丝滑转场-wan2.1_1987510145859129345.json
name: 首尾帧变身+丝滑转场-wan2.1_1987510145859129345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧变身+丝滑转场-wan2.1_1987510145859129345.json
hash: 9b3a9c45b1f3d60d
coverage: 0.689655
learned_at: 2026-10-15 22:32:58
nodes: [easy showAnything, StringToInt, Int, easy showAnything, easy showAnything, SimpleMath+, easy cleanGpuUsed, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, SetNode, SimpleMath+, easy showAnything, CR Text Concatenate, RH_Captioner, LoadImage, easy showAnything, WanVideoSampler, GetNode, WanVideoDecode, MaskBatch+, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncode, MaskPreview+, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoModelLoader, SetNode, CR Text, LoadImage, MaskFromBatch+, SimpleMath+, easy showAnything, MaskPreview+, MaskPreview+, PreviewImage, SetNode, Int, Int, easy anythingIndexSwitch, easy anythingIndexSwitch, Int, Int, WanVideoBlockSwap, WanVideoVACEEncode, LoadImage, MarkdownNote, ImageResizeKJ, ImageResizeKJ, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧变身+丝滑转场-wan2.1_1987510145859129345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987510145859129345.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `easy showAnything`
- `StringToInt`
- `Int`
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `SetNode`
- `SimpleMath+`
- `easy showAnything`
- `CR Text Concatenate`
- `RH_Captioner`
- `LoadImage`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `MaskBatch+`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `MaskPreview+`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `SetNode`
- `CR Text`
- `LoadImage`
- `MaskFromBatch+`
- `SimpleMath+`
- `easy showAnything`
- `MaskPreview+`
- `MaskPreview+`
- `PreviewImage`
- `SetNode`
- `Int`
- `Int`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `Int`
- `Int`
- `WanVideoBlockSwap`
- `WanVideoVACEEncode`
- `LoadImage`
- `MarkdownNote`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `VHS_VideoCombine`

## 知识

覆盖率 **69%**（40/58）

**有卡**：`StringToInt`、`Int`、`SimpleMath+`、`easy cleanGpuUsed`、`WanVideoVACEStartToEndFrame`、`CR Text Concatenate`、`RH_Captioner`、`LoadImage`、`WanVideoSampler`、`WanVideoDecode`、`MaskBatch+`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`MaskPreview+`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`CR Text`、`MaskFromBatch+`、`easy anythingIndexSwitch`、`WanVideoBlockSwap`、`WanVideoVACEEncode`、`ImageResizeKJ`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
