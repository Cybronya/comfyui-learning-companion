---
name: unknown_workflow_generic_1376
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.775
common_nodes: [FaceRestoreCFWithModel, FaceRestoreModelLoader, Image Comparer (rgthree), LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Inswapper换脸_1901526201146425345.json, 图片生成/图生图/一键去油光、修复瑕疵、消除AI脸_2035585105992884225.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1376

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Inswapper换脸_1901526201146425345.json、图片生成/图生图/一键去油光、修复瑕疵、消除AI脸_2035585105992884225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `ReActorFaceSwap` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
