---
name: unknown_workflow_sampler_clip_unet_144
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85275
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text Concatenate, WD14Tagger|pysssss]
members: [图片生成/文生图/1913109816590696449.json, 图片生成/文生图/1917149291704418305.json, 图片生成/文生图/1922444657790484482.json, 图片生成/文生图/1930926287748313090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_144

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1913109816590696449.json、图片生成/文生图/1917149291704418305.json、图片生成/文生图/1922444657790484482.json、图片生成/文生图/1930926287748313090.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LoadImage` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `ETN_Translate` —— 1/4 个有
- `JJC_JoyCaption` —— 1/4 个有
- `Joy_caption_two` —— 1/4 个有
- `Joy_caption_two_load` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `StringConstantMultiline` —— 1/4 个有
- `WD14Tagger|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 600 - 1024 | 4 | 82% |
| 高度 | 1088 | 800 - 1152 | 4 | 86% |
| LoRA 模型强度 | 1 | 0.6 - 1 | 3 | 78% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 600 - 1024，4 个样本，取值集中（一致性 82%）
- 高度 中位数 1088，观测区间 800 - 1152，4 个样本，取值集中（一致性 86%）
- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、WD14Tagger|pysssss
