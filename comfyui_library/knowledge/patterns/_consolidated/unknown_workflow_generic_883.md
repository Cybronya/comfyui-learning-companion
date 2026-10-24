---
name: unknown_workflow_generic_883
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.878667
common_nodes: [LoadImage, QwenImageModelLoader, RH_Captioner, RH_QwenImageGenerator, SaveImage, Textbox]
problems: []
missing: []
members: [图片生成/图生图/Qwen-lmage 图生图+放大_1952709588815704065.json, 图片生成/图生图/Qwen-lmage 图生图洗图｜图中文字保持_1952683016248299522.json, 图片生成/文生图/Qwen-lmage 文生图-满血版RH专供版节点_1952559689714348033.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_883

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-lmage 图生图+放大_1952709588815704065.json、图片生成/图生图/Qwen-lmage 图生图洗图｜图中文字保持_1952683016248299522.json、图片生成/文生图/Qwen-lmage 文生图-满血版RH专供版节点_1952559689714348033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `QwenImageModelLoader`
- `RH_Captioner`
- `RH_QwenImageGenerator`
- `SaveImage`
- `Textbox`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `PMRF` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
