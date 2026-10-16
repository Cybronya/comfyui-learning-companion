---
key: 视频生成/图生视频/WAN2.2 INP最强自动预测首尾帧极速版V1 浮云（次用）_1996851492734869506.json
name: WAN2.2 INP最强自动预测首尾帧极速版V1 浮云（次用）_1996851492734869506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1996851492734869506.json
hash: 4b1c0c88e19f2fa5
coverage: 0.891304
learned_at: 2026-10-15 22:33:27
nodes: [ImageResize+, LoadWanVideoT5TextEncoder, EmptyImage, ImageConcatMulti, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, ImageConcatMulti, GetImageSizeAndCount, WanVideoSampler, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoSampler, LayerUtility: PurgeVRAM, JWInteger, WanVideoVAELoader, INTConstant, WanVideoImageToVideoEncode, ImageResize+, AddLabel, AddLabel, WanVideoDecode, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoModelLoader, Note, WanVideoTextEncode, VHS_VideoCombine, JWInteger, Note, JWInteger, Note, VHS_VideoCombine, Note, LoadImage, LoadImage, JWInteger, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2 INP最强自动预测首尾帧极速版V1 浮云（次用）_1996851492734869506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996851492734869506.json`

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
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `ImageResize+`
- `AddLabel`
- `AddLabel`
- `WanVideoDecode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `JWInteger`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `CR Prompt Text`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`ImageResize+`、`LoadWanVideoT5TextEncoder`、`EmptyImage`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`JWInteger`、`WanVideoVAELoader`、`INTConstant`、`WanVideoImageToVideoEncode`、`AddLabel`、`WanVideoDecode`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
