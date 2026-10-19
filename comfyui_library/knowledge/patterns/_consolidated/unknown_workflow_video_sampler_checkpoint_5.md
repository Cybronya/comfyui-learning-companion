---
name: unknown_workflow_video_sampler_checkpoint_5
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8385
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1893677979124338689.json, 视频生成/图生视频/1930219583813357570.json, 视频生成/图生视频/1894944054985752577.json, 视频生成/图生视频/1929379921658023937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1893677979124338689.json、视频生成/图生视频/1930219583813357570.json、视频生成/图生视频/1894944054985752577.json、视频生成/图生视频/1929379921658023937.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `ImageResizeAndCropNode` —— 1/4 个有
- `IndexTTSNode` —— 1/4 个有
- `IndexTTSRun` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
