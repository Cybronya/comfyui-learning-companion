---
name: text_to_image_lora_sampler_clip_196
type: Text To Image
frequency: 6
level: moderate
coverage: 0.883833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, CR SDXL Aspect Ratio, CR Latent Batch Size]
members: [图片生成/文生图/1916516546913435650.json, 图片生成/文生图/1938456564812414977.json, 图片生成/文生图/1953006122934407170.json, 图片生成/文生图/1953340351912312834.json, 图片生成/文生图/1954055995188236290.json, 图片生成/文生图/1977747366285561858.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_196

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1916516546913435650.json、图片生成/文生图/1938456564812414977.json、图片生成/文生图/1953006122934407170.json、图片生成/文生图/1953340351912312834.json、图片生成/文生图/1954055995188236290.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/6 个有
- `Anything Everywhere3` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Anything Everywhere` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CR Latent Batch Size` —— 1/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `DF_Text_Box` —— 1/6 个有
- `Int` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 6 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 976 | 768 - 1080 | 6 | 87% |
| 高度 | 1536 | 1024 - 1720 | 6 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 59/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，6 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 768 - 1080，6 个样本，取值集中（一致性 87%）
- 高度 中位数 1536，观测区间 1024 - 1720，6 个样本
- 高发问题（59/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、CR SDXL Aspect Ratio、CR Latent Batch Size
