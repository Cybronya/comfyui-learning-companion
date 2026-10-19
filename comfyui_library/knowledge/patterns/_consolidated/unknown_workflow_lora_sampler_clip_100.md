---
name: unknown_workflow_lora_sampler_clip_100
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7965
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Concatenate, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text Concatenate, WD14Tagger|pysssss]
members: [图片生成/文生图/1913109816590696449.json, 图片生成/文生图/1922444657790484482.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_100

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1913109816590696449.json、图片生成/文生图/1922444657790484482.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `ETN_Translate` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `StringConstantMultiline` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 100% |
| 高度 | 1152 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、WD14Tagger|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
