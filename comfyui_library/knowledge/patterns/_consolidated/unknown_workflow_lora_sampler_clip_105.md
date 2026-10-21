---
name: unknown_workflow_lora_sampler_clip_105
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.840333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [SDXLEmptyLatentSizePicker+, ttN imageREMBG]
members: [图片生成/文生图/1937517741597179906.json, 图片生成/文生图/1953439745546309634.json, 图片生成/文生图/蒜-对比2个大模型出图效果_1996919135156256770.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1937517741597179906.json、图片生成/文生图/1953439745546309634.json、图片生成/文生图/蒜-对比2个大模型出图效果_1996919135156256770.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisplayText` —— 2/3 个有
- `TextConcat` —— 2/3 个有
- `Textbox` —— 2/3 个有
- `FluxGuidance` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `ttN imageREMBG` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.72) | - | 3 | 33% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 832x1152 (0.72)，3 个样本，一致性 33%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、ttN imageREMBG
