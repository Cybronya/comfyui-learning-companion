---
name: unknown_workflow_generic_681
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8
common_nodes: [Florence2ModelLoader, Florence2Run, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/反推提示词/01.反推提示词_1992192542441623553.json, 图片生成/反推提示词/Florence2反推模型_1920878173808951298.json, 图片生成/反推提示词/提示词反推  图片内容提取 文本生图_1920656499440553986.json, 图片生成/文生图/提示词反推  图片提取 文本生图_1930817149471010818.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_681

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/01.反推提示词_1992192542441623553.json、图片生成/反推提示词/Florence2反推模型_1920878173808951298.json、图片生成/反推提示词/提示词反推  图片内容提取 文本生图_1920656499440553986.json、图片生成/文生图/提示词反推  图片提取 文本生图_1930817149471010818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `Florence2ModelLoader`
- `Florence2Run`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 3/4 个有
- `PreviewAny` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
