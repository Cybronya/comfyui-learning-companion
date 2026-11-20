---
name: unknown_workflow_generic_769
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7875
common_nodes: [CR Text, JjkText, LayerUtility: TextJoin, Qwen3_VQA, SaveImage, Seedream4StreamingNode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/场景参考_1992762127528120322.json, 图片生成/图生图/物品增加_1992828377742594049.json, 图片生成/图生图/物品替换_1992805330686111746.json, 图片生成/文生图/单图编辑工作流_1992792485630111746.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_769

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/场景参考_1992762127528120322.json、图片生成/图生图/物品增加_1992828377742594049.json、图片生成/图生图/物品替换_1992805330686111746.json、图片生成/文生图/单图编辑工作流_1992792485630111746.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `JjkText`
- `LayerUtility: TextJoin`
- `Qwen3_VQA`
- `SaveImage`
- `Seedream4StreamingNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 3/4 个有
- `MultiplePathsInput` —— 3/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
