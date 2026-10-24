---
name: unknown_workflow_lora_sampler_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ImageConcatMulti, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, NunchakuFluxDiTLoader, SaveImage, Stack_LoRA, Text Multiline, chx_Ksampler_Kontext, sum_load_adv]
problems: []
missing: []
members: [图片生成/图生图/Kontext效率节点-多次连续编辑_1947145920976969730.json, 图片生成/图生图/Kontext效率节点-连续编辑_1947894219659718658.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext效率节点-多次连续编辑_1947145920976969730.json、图片生成/图生图/Kontext效率节点-连续编辑_1947894219659718658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `Stack_LoRA`
- `Text Multiline`
- `chx_Ksampler_Kontext`
- `sum_load_adv`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
