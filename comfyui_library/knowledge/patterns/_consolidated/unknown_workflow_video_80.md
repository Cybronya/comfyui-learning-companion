---
name: unknown_workflow_video_80
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8845
common_nodes: [CR Prompt Text, Float, ImageConcanate, JWImageResizeByLongerSide, JWInteger, LoadImage, RunningHub_FramePack_F1, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1919298489241501697.json, 视频生成/图生视频/1932622744146092033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1919298489241501697.json、视频生成/图生视频/1932622744146092033.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `JWInteger`
- `LoadImage`
- `RunningHub_FramePack_F1`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
