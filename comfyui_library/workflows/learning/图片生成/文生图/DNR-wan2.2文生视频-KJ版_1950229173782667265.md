---
key: 图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json
name: DNR-wan2.2文生视频-KJ版_1950229173782667265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json
hash: d0bee1a73211d0fc
coverage: 0.657895
learned_at: 2026-10-10 21:27:05
nodes: [WanVideoEasyCache, SetNode, GetNode, GetNode, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoDecode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTextEncode, GetNode, WanVideoSampler, WanVideoSampler, JWInteger, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_VideoCombine, WanVideoEmptyEmbeds, INTConstant, INTConstant, WanVideoEasyCache, JWInteger, JWInteger, SetNode, CR Prompt Text, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json`

## 结构

**节点**（38 个）：
- `WanVideoEasyCache`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoSampler`
- `WanVideoSampler`
- `JWInteger`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `INTConstant`
- `INTConstant`
- `WanVideoEasyCache`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `CR Prompt Text`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`WanVideoEasyCache`、`SetNode`、`GetNode`、`PrimitiveNode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`WanVideoSampler`、`JWInteger`、`WanVideoBlockSwap`

**缺卡**（1）：`CR Prompt Text`

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
