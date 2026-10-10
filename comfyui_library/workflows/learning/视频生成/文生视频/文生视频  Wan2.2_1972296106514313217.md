---
key: 视频生成/文生视频/文生视频  Wan2.2_1972296106514313217.json
name: 文生视频  Wan2.2_1972296106514313217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频  Wan2.2_1972296106514313217.json
hash: a7b35748cf2245e2
coverage: 0.633333
learned_at: 2026-10-10 23:13:04
nodes: [LoadWanVideoT5TextEncoder, ImpactInt, easy cleanGpuUsed, GetNode, WanVideoTextEncode, SetNode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoLoraSelectMulti, ImpactInt, GetNode, SimpleMath+, GetNode, ImpactInt, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoDecode, SetNode, easy cleanGpuUsed, ImpactInt, WanVideoEmptyEmbeds, VHS_VideoCombine, CreateCFGScheduleFloatList, SimpleMath+, WanVideoSampler, WanVideoSampler, SetNode, Text, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: [SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/文生视频  Wan2.2_1972296106514313217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频  Wan2.2_1972296106514313217.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（30 个）：
- `LoadWanVideoT5TextEncoder`
- `ImpactInt`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `ImpactInt`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `ImpactInt`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `SetNode`
- `easy cleanGpuUsed`
- `ImpactInt`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `SetNode`
- `Text`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **63%**（19/30）

**有卡**：`LoadWanVideoT5TextEncoder`、`ImpactInt`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`Text`、`WanVideoModelLoader`

**缺卡**（5）：`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、ImpactInt

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
