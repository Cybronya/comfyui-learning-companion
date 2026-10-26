---
name: unknown_workflow_generic_1440
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [InvertMask, JoinImageWithAlpha, LoadImage, MaskPreview, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键抠图（LOGO专用）_2074311869149569026.json, 图片生成/图生图/一键移除白底_2074312821139140609.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1440

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键抠图（LOGO专用）_2074311869149569026.json、图片生成/图生图/一键移除白底_2074312821139140609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `InvertMask`
- `JoinImageWithAlpha`
- `LoadImage`
- `MaskPreview`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PDtools_Filter_GodenPNG_v1` —— 1/2 个有
- `PDtools_Filter_WPNG_v1` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
