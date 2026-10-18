---
key: 视频生成/图生视频/(KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json
name: (KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json
hash: 5ddbdc566ed4deeb
coverage: 0.891304
learned_at: 2026-10-15 22:31:14
nodes: [ImageResize+, LoadWanVideoT5TextEncoder, EmptyImage, ImageConcatMulti, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, ImageConcatMulti, GetImageSizeAndCount, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoSampler, LayerUtility: PurgeVRAM, JWInteger, Note, Note, WanVideoTextEncode, Note, JWInteger, WanVideoVAELoader, INTConstant, WanVideoImageToVideoEncode, Note, ImageResize+, AddLabel, AddLabel, WanVideoDecode, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoModelLoader, LoadImage, LoadImage, PrimitiveNode, JWInteger, CR Prompt Text, VHS_VideoCombine, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956601025757151233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（46 个）：
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `Note`
- `JWInteger`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `Note`
- `ImageResize+`
- `AddLabel`
- `AddLabel`
- `WanVideoDecode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `JWInteger`
- `VHS_VideoCombine`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`ImageResize+`、`LoadWanVideoT5TextEncoder`、`EmptyImage`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`JWInteger`、`WanVideoTextEncode`、`WanVideoVAELoader`、`INTConstant`、`WanVideoImageToVideoEncode`、`AddLabel`、`WanVideoDecode`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`LoadImage`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
