---
name: unknown_workflow_generic_212
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8122
common_nodes: [ImageScaleDownToSize, LoadImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: [CR Text, Text Multiline, easy batchAnything]
members: [图片生成/文生图/1961119103400480770.json, 图片生成/文生图/1962727003998797826.json, 图片生成/文生图/1964284032529874946.json, 图片生成/文生图/1964288162107412482.json, 图片生成/文生图/1981511127022608385.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_212

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1961119103400480770.json、图片生成/文生图/1962727003998797826.json、图片生成/文生图/1964284032529874946.json、图片生成/文生图/1964288162107412482.json、图片生成/文生图/1981511127022608385.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageScaleDownToSize`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `easy batchAnything` —— 4/5 个有
- `CR Text` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Text Multiline、easy batchAnything
