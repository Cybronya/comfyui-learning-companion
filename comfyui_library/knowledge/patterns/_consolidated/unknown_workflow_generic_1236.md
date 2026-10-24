---
name: unknown_workflow_generic_1236
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.596
common_nodes: [Image Comparer (rgthree), LoadImage, RH_Captioner_Pro, RH_RhartImageG2TextToImage, SaveImage, Text, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305.json, 图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1236

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305.json、图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `RH_Captioner_Pro`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `Text`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageReceiver` —— 1/2 个有
- `ImageSender` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
