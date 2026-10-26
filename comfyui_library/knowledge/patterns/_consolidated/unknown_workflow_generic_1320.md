---
name: unknown_workflow_generic_1320
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6905
common_nodes: [LoadImage, RH_Captioner, RH_Translator, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/反推提示词/最强图片反推提示词_1910889734980468737.json, 图片生成/图生图/图片反推提示词基础工作流 RunningHub Captioner_1937827090836144129.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1320

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/最强图片反推提示词_1910889734980468737.json、图片生成/图生图/图片反推提示词基础工作流 RunningHub Captioner_1937827090836144129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_Captioner`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
