---
name: text_to_image_sampler_clip_unet_148
type: Text To Image
frequency: 4
level: moderate
coverage: 0.964
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json, 图片生成/文生图/FLUX文生图_1953188609090326530.json, 图片生成/文生图/Flux SRPO真实感文生图_1968285554058113025.json, 图片生成/文生图/Krea 二次采样对比_1982000492014379010.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json、图片生成/文生图/FLUX文生图_1953188609090326530.json、图片生成/文生图/Flux SRPO真实感文生图_1968285554058113025.json、图片生成/文生图/Krea 二次采样对比_1982000492014379010.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ApplyIPAdapterFlux` —— 1/4 个有
- `IPAdapterFluxLoader` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LatentUpscale` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 5 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.76 | 4 | 72% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 512 - 1536 | 4 | 60% |
| 高度 | 792 | 512 - 1024 | 4 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 5 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.76，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1536，4 个样本
- 高度 中位数 792，观测区间 512 - 1024，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
