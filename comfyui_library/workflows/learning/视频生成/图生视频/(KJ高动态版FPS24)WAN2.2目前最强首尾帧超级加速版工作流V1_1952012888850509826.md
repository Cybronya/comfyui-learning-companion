---
key: 视频生成/图生视频/(KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json
name: (KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json
hash: 6291df5b929edbc9
coverage: 0.891304
learned_at: 2026-10-15 22:30:59
nodes: [ImageResize+, LoadWanVideoT5TextEncoder, LoadImage, EmptyImage, ImageConcatMulti, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, ImageConcatMulti, GetImageSizeAndCount, WanVideoSampler, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoSampler, LayerUtility: PurgeVRAM, JWInteger, JWInteger, Note, Note, WanVideoTextEncode, CR Prompt Text, Note, JWInteger, WanVideoVAELoader, INTConstant, WanVideoImageToVideoEncode, Note, VHS_VideoCombine, JWInteger, ImageResize+, AddLabel, AddLabel, VHS_VideoCombine, WanVideoDecode, LoadImage, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952012888850509826.json`

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
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
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
- `VHS_VideoCombine`
- `JWInteger`
- `ImageResize+`
- `AddLabel`
- `AddLabel`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **89%**（41/46）

**有卡**：`ImageResize+`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`EmptyImage`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`JWInteger`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoVAELoader`、`INTConstant`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`AddLabel`、`WanVideoDecode`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
