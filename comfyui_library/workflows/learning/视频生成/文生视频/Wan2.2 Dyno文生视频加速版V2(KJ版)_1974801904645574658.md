---
key: 视频生成/文生视频/Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658.json
name: Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658.json
hash: 2b9464bd8e0cc861
coverage: 0.820513
learned_at: 2026-10-10 23:06:50
nodes: [WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVAELoader, VHS_VideoCombine, Note, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoSampler, WanVideoSetLoRAs, CreateCFGScheduleFloatList, GetImageSizeAndCount, ImageFromBatch+, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoBlockSwap, PrimitiveNode, INTConstant, INTConstant, WanVideoTextEncode, CR Prompt Text, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: [ImageFromBatch+, CR Prompt Text]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `Note`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoTextEncode`

**缺卡**（2）：`ImageFromBatch+`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
