---
name: unknown_workflow_video_sampler_checkpoint_11
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5635
common_nodes: [GetNode, ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, SetNode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1891727710027206657.json, 视频生成/图生视频/1907741322999177217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1891727710027206657.json、视频生成/图生视频/1907741322999177217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SetNode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
