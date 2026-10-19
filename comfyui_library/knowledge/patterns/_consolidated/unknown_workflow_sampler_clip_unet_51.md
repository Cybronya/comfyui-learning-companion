---
name: unknown_workflow_sampler_clip_unet_51
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7708
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Concatenate, Text Multiline, CR Text Concatenate, Text Concatenate (JPS)]
members: [图片生成/文生图/1904702749529845761.json, 图片生成/文生图/1905062711074689026.json, 图片生成/文生图/1909542088999116801.json, 图片生成/文生图/1909546503734763521.json, 图片生成/文生图/1920491097255251969.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1904702749529845761.json、图片生成/文生图/1905062711074689026.json、图片生成/文生图/1909542088999116801.json、图片生成/文生图/1909546503734763521.json、图片生成/文生图/1920491097255251969.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 4/5 个有
- `CR Text Concatenate` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `Text Concatenate` —— 2/5 个有
- `Text Concatenate (JPS)` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1536 | 1024 - 1536 | 5 | 86% |
| LoRA 模型强度 | 0.9 | 0.6 - 1 | 4 | 80% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，5 个样本，取值集中（一致性 86%）
- LoRA 模型强度 中位数 0.9，观测区间 0.6 - 1，4 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Concatenate、Text Multiline、CR Text Concatenate、Text Concatenate (JPS)
