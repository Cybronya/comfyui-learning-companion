---
name: unknown_workflow_generic_1085
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.727
common_nodes: [PreviewAny, RHUploadPdf, RunningHub DeepSeekOCR Infer(Pdf), SaveImage, easy saveText]
problems: []
missing: []
members: [图片生成/反推提示词/PDF+DeepSeekOCR V1_1998839826889760769.json, 平台全量/PDF上传+DeepSeekOCR 演示工作流_1998740905962131458.json, 视频生成/图生视频/PDF上传+DeepSeekOCR 在线识别_1998752851130208257.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1085

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/PDF+DeepSeekOCR V1_1998839826889760769.json、平台全量/PDF上传+DeepSeekOCR 演示工作流_1998740905962131458.json、视频生成/图生视频/PDF上传+DeepSeekOCR 在线识别_1998752851130208257.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `PreviewAny`
- `RHUploadPdf`
- `RunningHub DeepSeekOCR Infer(Pdf)`
- `SaveImage`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
