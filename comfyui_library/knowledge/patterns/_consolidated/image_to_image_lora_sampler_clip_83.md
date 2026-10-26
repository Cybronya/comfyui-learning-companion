---
name: image_to_image_lora_sampler_clip_83
type: Image To Image
frequency: 3
level: strong
coverage: 0.788
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, ConstrainImage|pysssss, DualCLIPLoader, ImageScaleBy, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, LoraLoader, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/【简洁极速版】FLUX+人物一致性图生图+ joy自动反推提示词_1930172529862938626.json, 图片生成/图生图/FLUX 图生图_1866792898053259265.json, 图片生成/图生图/图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/【简洁极速版】FLUX+人物一致性图生图+ joy自动反推提示词_1930172529862938626.json、图片生成/图生图/FLUX 图生图_1866792898053259265.json、图片生成/图生图/图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `ImageScaleBy`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 2/3 个有
- `GetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.65 | 0.65 - 0.65 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 0.65，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
