---
name: text_to_image_sampler_clip_unet_138
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9546
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json, 图片生成/文生图/FLUX文生图_1953188609090326530.json, 图片生成/文生图/Flux SRPO真实感文生图_1968285554058113025.json, 图片生成/文生图/Krea 二次采样对比_1982000492014379010.json, 图片生成/文生图/【阡陌】FLUX krea 文生图工作流_1951489939009646593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json、图片生成/文生图/FLUX文生图_1953188609090326530.json、图片生成/文生图/Flux SRPO真实感文生图_1968285554058113025.json、图片生成/文生图/Krea 二次采样对比_1982000492014379010.json、图片生成/文生图/【阡陌】FLUX krea 文生图工作流_1951489939009646593.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoadImage` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ApplyIPAdapterFlux` —— 1/5 个有
- `IPAdapterFluxLoader` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LatentUpscale` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 5 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.76 | 5 | 74% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 512 - 1536 | 5 | 61% |
| 高度 | 864 | 512 - 1024 | 5 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.76，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1536，5 个样本
- 高度 中位数 864，观测区间 512 - 1024，5 个样本
