---
name: unknown_workflow_generic_1170
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.661
common_nodes: [LoadImage, PreviewImage, PrimitiveString, RH_RhartImageG2ImageToImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/亿薪海报_2102278162146222081.json, 图片生成/文生图/全能图片G-单图模式-支持PS插件_2047191235810562049.json, 平台全量/一键生成短剧海报_2076951550546759682.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1170

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/亿薪海报_2102278162146222081.json、图片生成/文生图/全能图片G-单图模式-支持PS插件_2047191235810562049.json、平台全量/一键生成短剧海报_2076951550546759682.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `PrimitiveString`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RHSettingsNode` —— 2/3 个有
- `StringReplace` —— 2/3 个有
- `PrimitiveInt` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
