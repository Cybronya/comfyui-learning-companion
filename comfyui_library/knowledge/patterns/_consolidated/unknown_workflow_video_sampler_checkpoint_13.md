---
name: unknown_workflow_video_sampler_checkpoint_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.757
common_nodes: [ImageOnlyCheckpointLoader, ImageResize+, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, SimpleMath+, VHS_VideoCombine, easy float, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1922851551227035649.json, 视频生成/文生视频/1933419602271449089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1922851551227035649.json、视频生成/文生视频/1933419602271449089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `ImageResize+`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SimpleMath+`
- `VHS_VideoCombine`
- `easy float`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `String Literal` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
