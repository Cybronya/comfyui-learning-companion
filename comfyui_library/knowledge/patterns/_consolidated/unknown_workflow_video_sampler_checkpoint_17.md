---
name: unknown_workflow_video_sampler_checkpoint_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.916
common_nodes: [ImageOnlyCheckpointLoader, ImageScale, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/SONIC-数字人_1927236443775651842.json, 视频生成/图生视频/Sonic对口型数字人_1922467727339094018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SONIC-数字人_1927236443775651842.json、视频生成/图生视频/Sonic对口型数字人_1922467727339094018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `ImageScale`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SparkTTSClone` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
