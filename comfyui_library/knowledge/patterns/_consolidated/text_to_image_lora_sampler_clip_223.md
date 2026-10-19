---
name: text_to_image_lora_sampler_clip_223
type: Text To Image
frequency: 3
level: moderate
coverage: 0.914
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1950437362914516993.json, 图片生成/文生图/1988883409260916737.json, 图片生成/文生图/1989381394365378562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_223

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1950437362914516993.json、图片生成/文生图/1988883409260916737.json、图片生成/文生图/1989381394365378562.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `Int` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 30 | 3 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1080 | 3 | 71% |
| 高度 | 1368 | 512 - 1920 | 3 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 30，3 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1080，3 个样本
- 高度 中位数 1368，观测区间 512 - 1920，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
