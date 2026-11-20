---
name: unknown_workflow_generic_814
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8165
common_nodes: [LoadImage, SaveImage, ShellAgentPluginOutputText, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/DeepSeek Ocr光学识别_1987541405939773441.json, 图片生成/反推提示词/DeepSeek Ocr光学识别_1987828401920741377.json, 图片生成/反推提示词/Paddle Ocr光学识别V1_1987541336356229121.json, 平台全量/Paddle OCR光学识别V1_1988289821875593217.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_814

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/DeepSeek Ocr光学识别_1987541405939773441.json、图片生成/反推提示词/DeepSeek Ocr光学识别_1987828401920741377.json、图片生成/反推提示词/Paddle Ocr光学识别V1_1987541336356229121.json、平台全量/Paddle OCR光学识别V1_1988289821875593217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RunningHub DeepSeekOCR Infer` —— 2/4 个有
- `RunningHub PaddleOCR-VL Infer` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
