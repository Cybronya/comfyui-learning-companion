---
name: text_to_image_sampler_clip_checkpoint_13
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7802
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, CR Text Concatenate]
members: [图片生成/文生图/1979416721058598913.json, 图片生成/文生图/1980214445693689857.json, 图片生成/文生图/1982645105960067073.json, 图片生成/文生图/1982665506299756546.json, 图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1979416721058598913.json、图片生成/文生图/1980214445693689857.json、图片生成/文生图/1982645105960067073.json、图片生成/文生图/1982665506299756546.json、图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | 784 - 1024 | 5 | 88% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 19 | 5 - 25 | 5 | 58% |
| Prompt 约束强度(CFG) | 7 | 2 - 8 | 5 | 63% |
| 采样算法 | dpmpp_2m_sde | - | 5 | 40% |
| 调度器 | karras | - | 5 | 60% |
| 重绘幅度 | 1 | 0.25 - 1 | 5 | 65% |
| LoRA 模型强度 | 0.75 | - | 2 | 67% |
| LoRA 文本强度 | 0.65 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 864，观测区间 784 - 1024，5 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 19，观测区间 5 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 2 - 8，5 个样本
- 采样算法 最常用 dpmpp_2m_sde，5 个样本，一致性 40%
- 调度器 最常用 karras，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，5 个样本
- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Text Concatenate
