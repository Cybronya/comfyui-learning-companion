---
name: unknown_workflow_generic_1291
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [LoadImage, PrimitiveStringMultiline, RH_Captioner_Pro, SaveImage, StringConcatenate]
problems: []
missing: []
members: [图片生成/反推提示词/LLM 反推提示词工作流｜Gemini 3 参考图反推提示词 一键重绘复刻_2099630333841989634.json, 图片生成/图生图/反推提示词工作流｜Gemini 3 参考图反推提示词 一键重绘复刻_2099304187879313410.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1291

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/LLM 反推提示词工作流｜Gemini 3 参考图反推提示词 一键重绘复刻_2099630333841989634.json、图片生成/图生图/反推提示词工作流｜Gemini 3 参考图反推提示词 一键重绘复刻_2099304187879313410.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PrimitiveStringMultiline`
- `RH_Captioner_Pro`
- `SaveImage`
- `StringConcatenate`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 1/2 个有
- `RH_SeedreamV5ProImageToImage` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
