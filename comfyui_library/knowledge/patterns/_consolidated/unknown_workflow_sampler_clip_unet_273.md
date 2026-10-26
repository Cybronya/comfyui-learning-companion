---
name: unknown_workflow_sampler_clip_unet_273
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8956
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/4张 文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1972618798815698945.json, 图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json, 图片生成/文生图/FLUX 最强基础文生图 支持手_自动提示词_1922444657790484482.json, 图片生成/文生图/Flux文生图（中文提示词）+新版Jocaption反推_1930926287748313090.json, 图片生成/文生图/flux文生图-在线生图-可用lora-可反推图片（效果强悍）_1913109816590696449.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_273

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/4张 文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1972618798815698945.json、图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json、图片生成/文生图/FLUX 最强基础文生图 支持手_自动提示词_1922444657790484482.json、图片生成/文生图/Flux文生图（中文提示词）+新版Jocaption反推_1930926287748313090.json、图片生成/文生图/flux文生图-在线生图-可用lora-可反推图片（效果强悍）_1913109816590696449.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

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
- `LoadImage` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `ETN_Translate` —— 1/5 个有
- `JJC_JoyCaption` —— 1/5 个有
- `Joy_caption_two` —— 1/5 个有
- `Joy_caption_two_load` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `StringConstantMultiline` —— 1/5 个有
- `WD14Tagger|pysssss` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 4 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 896 | 400 - 1080 | 5 | 72% |
| 高度 | 1152 | 400 - 1920 | 5 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 400 - 1080，5 个样本
- 高度 中位数 1152，观测区间 400 - 1920，5 个样本
