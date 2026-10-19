---
name: text_to_image_sampler_clip_unet_13
type: Text To Image
frequency: 5
level: strong
coverage: 0.8846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, Text Multiline]
members: [图片生成/文生图/1950528087563948034.json, 图片生成/文生图/1950700991370973185.json, 图片生成/文生图/1950719208512491521.json, 图片生成/文生图/1950771546711351297.json, 图片生成/文生图/1955481041341485058.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1950528087563948034.json、图片生成/文生图/1950700991370973185.json、图片生成/文生图/1950719208512491521.json、图片生成/文生图/1950771546711351297.json、图片生成/文生图/1955481041341485058.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/5 个有
- `Bjornulf_TextToStringAndSeed` —— 3/5 个有
- `CR Text Concatenate` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelSamplingSD3` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `RH_LLMAPI_NODE` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `Wan_video_prompt_generator` —— 3/5 个有
- `CFGZeroStarAndInit` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PMRF` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | 512 - 720 | 5 | 85% |
| 高度 | 512 | 512 - 1280 | 5 | 54% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 0.4 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 720，5 个样本，取值集中（一致性 85%）
- 高度 中位数 512，观测区间 512 - 1280，5 个样本
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Text Multiline
