---
name: unknown_workflow_generic_192
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.791667
common_nodes: [QwenImageModelLoader, RH_QwenImageGenerator, SaveImage]
problems: []
missing: [CR Prompt Text]
members: [图片生成/文生图/1952532640446517249.json, 图片生成/文生图/1952536297061724162.json, 图片生成/文生图/1952542727718277122.json, 图片生成/文生图/1952546223993622529.json, 图片生成/文生图/1952554142764085249.json, 图片生成/文生图/1954741337885175809.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_192

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1952532640446517249.json、图片生成/文生图/1952536297061724162.json、图片生成/文生图/1952542727718277122.json、图片生成/文生图/1952546223993622529.json、图片生成/文生图/1952554142764085249.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `QwenImageModelLoader`
- `RH_QwenImageGenerator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
