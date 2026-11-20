---
name: unknown_workflow_generic_1730
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [LoadImage, RH_YouchuanTextToImageV81, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/悠船 图生图（RH版）_2063999953286029313.json, 平台全量/RH 悠船 垫图+风格参考生图-v8.1_2054772949181321217.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1730

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/悠船 图生图（RH版）_2063999953286029313.json、平台全量/RH 悠船 垫图+风格参考生图-v8.1_2054772949181321217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_YouchuanTextToImageV81`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
