---
name: unknown_workflow_generic_1300
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.749
common_nodes: [PreviewAny, RHBatchImages:, RHExtractImage, RHUploadZip, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageCount, easy saveText, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3 VL批量自动打标_2026894908874821633.json, 数字人/数字人/图片批量打标反推_1997013031525761026.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1300

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Qwen3 VL批量自动打标_2026894908874821633.json、数字人/数字人/图片批量打标反推_1997013031525761026.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `PreviewAny`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `Bjornulf_ShowInt` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
