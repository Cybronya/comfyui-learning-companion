---
key: 视频生成/文生视频/最新WAN2.2 KJ版 T2V 文生视频加速版工作流_1977042886363631618.json
name: 最新WAN2.2 KJ版 T2V 文生视频加速版工作流_1977042886363631618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最新WAN2.2 KJ版 T2V 文生视频加速版工作流_1977042886363631618.json
hash: eb8186466c68287e
coverage: 0.657895
learned_at: 2026-10-10 23:13:23
nodes: [WanVideoEasyCache, SetNode, GetNode, GetNode, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoDecode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTextEncode, GetNode, WanVideoSampler, WanVideoSampler, JWInteger, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoEmptyEmbeds, INTConstant, INTConstant, WanVideoEasyCache, SetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, JWInteger, JWInteger, VHS_VideoCombine, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/最新WAN2.2 KJ版 T2V 文生视频加速版工作流_1977042886363631618.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/最新WAN2.2 KJ版 T2V 文生视频加速版工作流_1977042886363631618.json`

## 结构

**生成流程**：Model → Sampling → Other

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
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoEmptyEmbeds`
- `INTConstant`
- `INTConstant`
- `WanVideoEasyCache`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `CR Prompt Text`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`WanVideoEasyCache`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`WanVideoSampler`、`JWInteger`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`VHS_VideoCombine`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
