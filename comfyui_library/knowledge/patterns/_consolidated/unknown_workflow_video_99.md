---
name: unknown_workflow_video_99
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6145
common_nodes: [CubeRotationNode, Int, LoadImage, PrimitiveFloat, Reroute (rgthree), VHS_VideoCombine, 孤海-取色器]
problems: []
missing: []
members: [视频生成/图生视频/1978743150502105089.json, 视频生成/图生视频/1979076576564383745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_99

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1978743150502105089.json、视频生成/图生视频/1979076576564383745.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CubeRotationNode`
- `Int`
- `LoadImage`
- `PrimitiveFloat`
- `Reroute (rgthree)`
- `VHS_VideoCombine`
- `孤海-取色器`

**可变部分**（部分 workflow 才有）：
- `CR Image Size` —— 1/2 个有
- `ImageCombine` —— 1/2 个有
- `ImageScale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
