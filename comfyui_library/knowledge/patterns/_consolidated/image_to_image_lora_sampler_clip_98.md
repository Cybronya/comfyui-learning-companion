---
name: image_to_image_lora_sampler_clip_98
type: Image To Image
frequency: 3
level: moderate
coverage: 0.919333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2-高低噪-洗图+放大_1960261741022228481.json, 图片生成/图生图/Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913.json, 图片生成/图生图/Wan2.2图生图-洗图-v2.0_1951114789902819329.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Wan2.2-高低噪-洗图+放大_1960261741022228481.json、图片生成/图生图/Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913.json、图片生成/图生图/Wan2.2图生图-洗图-v2.0_1951114789902819329.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 2/3 个有
- `PMRF` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Bjornulf_TextToStringAndSeed` —— 1/3 个有
- `Float` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Seed_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 3 | 19% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 19%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
