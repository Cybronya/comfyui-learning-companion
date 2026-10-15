---
key: 图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json
name: DNR-wan2.2文生视频-KJ版_1950229173782667265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json
hash: d0bee1a73211d0fc
coverage: 0.684211
learned_at: 2026-10-15 22:26:14
nodes: [WanVideoEasyCache, SetNode, GetNode, GetNode, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoDecode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTextEncode, GetNode, WanVideoSampler, WanVideoSampler, JWInteger, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_VideoCombine, WanVideoEmptyEmbeds, INTConstant, INTConstant, WanVideoEasyCache, JWInteger, JWInteger, SetNode, CR Prompt Text, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: []
---

# 图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json`

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

覆盖率 **68%**（26/38）

**有卡**：`WanVideoEasyCache`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`WanVideoSampler`、`JWInteger`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`INTConstant`、`CR Prompt Text`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
