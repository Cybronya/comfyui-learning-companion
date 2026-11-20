---
name: unknown_workflow_lora_sampler_clip_223
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.981333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-base加速lora文生图_2017613550671372290.json, 图片生成/文生图/Z-image-base基础文生图+高清放大_2029451837371326465.json, 图片生成/文生图/anima2 lora 高清放大Q版卡通画风_2036789720553889793.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_223

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-base加速lora文生图_2017613550671372290.json、图片生成/文生图/Z-image-base基础文生图+高清放大_2029451837371326465.json、图片生成/文生图/anima2 lora 高清放大Q版卡通画风_2036789720553889793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `CFGZeroStar` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 28 | 3 | 51% |
| Prompt 约束强度(CFG) | 2 | 1 - 5 | 3 | 36% |
| 采样算法 | euler_ancestral | - | 3 | 33% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 28，3 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 33%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
