---
name: text_to_image_upscale_lora_sampler_16
type: Text To Image
frequency: 3
level: moderate
coverage: 0.774333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate]
members: [图片生成/文生图/1957992470980210690.json, 图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json, 图片生成/文生图/绝区零风格文生图场景设计_2100441031195062274.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1957992470980210690.json、图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json、图片生成/文生图/绝区零风格文生图场景设计_2100441031195062274.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.25 - 1 | 3 | 53% |
| 宽度 | 1536 | 1280 - 1536 | 3 | 92% |
| 高度 | 768 | 768 - 960 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，3 个样本
- 宽度 中位数 1536，观测区间 1280 - 1536，3 个样本，取值集中（一致性 92%）
- 高度 中位数 768，观测区间 768 - 960，3 个样本，取值集中（一致性 89%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate
