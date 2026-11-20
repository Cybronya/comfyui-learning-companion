---
name: unknown_workflow_lora_sampler_6
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.916333
common_nodes: [AddLabel, CR String To Combo, ImageResizeKJv2, Int2String, LoadImage, Primitive integer [Crystools], RH_Captioner, RunningHub OmniConsistency LoraLoader, RunningHub OmniConsistency Sampler, SaveImage, Text Concatenate, TextSwitchCase, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/OmniConsistencyz风格选择器+提示词_1930538835334320130.json, 图片生成/图生图/OmniConsistencyz风格选择器-全网最精简_1928834484957822977.json, 图片生成/图生图/稳定转绘22种风格_1929376093126692865.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/OmniConsistencyz风格选择器+提示词_1930538835334320130.json、图片生成/图生图/OmniConsistencyz风格选择器-全网最精简_1928834484957822977.json、图片生成/图生图/稳定转绘22种风格_1929376093126692865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CR String To Combo`
- `ImageResizeKJv2`
- `Int2String`
- `LoadImage`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `RunningHub OmniConsistency LoraLoader`
- `RunningHub OmniConsistency Sampler`
- `SaveImage`
- `Text Concatenate`
- `TextSwitchCase`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `String` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
