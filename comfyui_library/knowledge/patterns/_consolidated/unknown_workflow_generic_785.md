---
name: unknown_workflow_generic_785
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.667
common_nodes: [JjkText, LayerUtility: TextJoin, LoadImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, ShowAnything|Mie, easy promptList]
problems: []
missing: []
members: [图片生成/文生图/Share Widget_2086637164250619906.json, 图片生成/文生图/check-in share image_2095684493167390722.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_785

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Share Widget_2086637164250619906.json、图片生成/文生图/check-in share image_2095684493167390722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `JjkText`
- `LayerUtility: TextJoin`
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `ShowAnything|Mie`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `ImageScale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
