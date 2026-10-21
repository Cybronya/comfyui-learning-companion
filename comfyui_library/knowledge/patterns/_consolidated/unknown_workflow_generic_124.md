---
name: unknown_workflow_generic_124
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.902125
common_nodes: [LoadImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: [easy imageConcat]
members: [图片生成/文生图/1960512200576331778.json, 图片生成/文生图/1960889396658679810.json, 图片生成/文生图/1962744108026605569.json, 图片生成/文生图/1963068703426457602.json, 图片生成/文生图/1963085084205232130.json, 图片生成/文生图/1972914844137623554.json, 图片生成/文生图/1987793454732390401.json, 图片生成/文生图/1988565227136532481.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_124

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1960512200576331778.json、图片生成/文生图/1960889396658679810.json、图片生成/文生图/1962744108026605569.json、图片生成/文生图/1963068703426457602.json、图片生成/文生图/1963085084205232130.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 4/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `easy imageConcat` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy imageConcat
