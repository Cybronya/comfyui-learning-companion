---
name: unknown_workflow_generic_745
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6155
common_nodes: [CR Text Concatenate, DeepTranslatorTextNode, Gemini_Flash_200_Exp, Google-Gemini-PL, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, Textbox, easy imageSize]
problems: []
missing: [CR Text Concatenate, Google-Gemini-PL, easy imageSize]
members: [图片生成/文生图/1902281640062640129.json, 图片生成/文生图/文改图 _ Gemini2.0_1902281640062640129.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_745

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1902281640062640129.json、图片生成/文生图/文改图 _ Gemini2.0_1902281640062640129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text Concatenate`
- `DeepTranslatorTextNode`
- `Gemini_Flash_200_Exp`
- `Google-Gemini-PL`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `Textbox`
- `easy imageSize`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Google-Gemini-PL、easy imageSize
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
