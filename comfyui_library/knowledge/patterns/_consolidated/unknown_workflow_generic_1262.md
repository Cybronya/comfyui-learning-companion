---
name: unknown_workflow_generic_1262
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [LoadImage, ReActorFaceBoost, ReActorFaceSwapOpt, ReActorOptions, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/ReActor换脸放置脸部阻挡版_2022179155944673282.json, 图片生成/图生图/ReActo简易换脸_2022177926304763906.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1262

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ReActor换脸放置脸部阻挡版_2022179155944673282.json、图片生成/图生图/ReActo简易换脸_2022177926304763906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `ReActorFaceBoost`
- `ReActorFaceSwapOpt`
- `ReActorOptions`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ReActorMaskHelper` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
