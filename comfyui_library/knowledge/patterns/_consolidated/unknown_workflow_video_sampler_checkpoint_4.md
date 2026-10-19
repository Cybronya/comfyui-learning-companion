---
name: unknown_workflow_video_sampler_checkpoint_4
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91425
common_nodes: [ImageOnlyCheckpointLoader, ImpactSwitch, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, SaveAudio, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1924481030601043969.json, 视频生成/图生视频/1928741923505258497.json, 视频生成/图生视频/1932324749186072578.json, 视频生成/文生视频/1933029746223579138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1924481030601043969.json、视频生成/图生视频/1928741923505258497.json、视频生成/图生视频/1932324749186072578.json、视频生成/文生视频/1933029746223579138.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `ImpactSwitch`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SaveAudio`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Note _O` —— 3/4 个有
- `AnimateDiffCombine` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `IndexTTSNode` —— 2/4 个有
- `IndexTTSRun` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
