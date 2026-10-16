---
key: 视频生成/图生视频/(KJ版高动态FPS24)WAN2.2 INP最强自动预测首尾帧极速版V1_1956583088841261058.json
name: (KJ版高动态FPS24)WAN2.2 INP最强自动预测首尾帧极速版V1_1956583088841261058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956583088841261058.json
hash: a8b7e4215e770aa4
coverage: 0.891304
learned_at: 2026-10-15 22:31:14
nodes: [ImageResize+, LoadWanVideoT5TextEncoder, LoadImage, EmptyImage, ImageConcatMulti, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, ImageConcatMulti, GetImageSizeAndCount, WanVideoSampler, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoSampler, LayerUtility: PurgeVRAM, JWInteger, JWInteger, Note, Note, WanVideoTextEncode, CR Prompt Text, Note, JWInteger, WanVideoVAELoader, INTConstant, WanVideoImageToVideoEncode, Note, JWInteger, ImageResize+, AddLabel, AddLabel, VHS_VideoCombine, WanVideoDecode, LoadImage, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版高动态FPS24)WAN2.2 INP最强自动预测首尾帧极速版V1_1956583088841261058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956583088841261058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（46 个）：
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `EmptyImage`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `Note`
- `JWInteger`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `Note`
- `JWInteger`
- `ImageResize+`
- `AddLabel`
- `AddLabel`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`ImageResize+`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`EmptyImage`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`JWInteger`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoVAELoader`、`INTConstant`、`WanVideoImageToVideoEncode`、`AddLabel`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
