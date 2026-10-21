---
name: unknown_workflow_video_lora_sampler_676
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.788667
common_nodes: [CreateCFGScheduleFloatList, GetNode, ImpactInt, LoadWanVideoT5TextEncoder, SetNode, SimpleMath+, Text, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: [SimpleMath+, easy cleanGpuUsed]
members: [视频生成/图生视频/1988338285892255745.json, 视频生成/图生视频/1972327481543946241.json, 视频生成/文生视频/1972296106514313217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_676

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1988338285892255745.json、视频生成/图生视频/1972327481543946241.json、视频生成/文生视频/1972296106514313217.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetNode`
- `ImpactInt`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、easy cleanGpuUsed
