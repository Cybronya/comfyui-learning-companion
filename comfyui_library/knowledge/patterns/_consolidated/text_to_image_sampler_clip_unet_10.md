---
name: text_to_image_sampler_clip_unet_10
type: Text To Image
frequency: 6
level: moderate
coverage: 0.895333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1907792965371371522.json, 图片生成/文生图/1910971389912805378.json, 图片生成/文生图/1911939065036636162.json, 图片生成/文生图/1951288817326215170.json, 图片生成/文生图/1953188609090326530.json, 图片生成/文生图/1982000492014379010.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1907792965371371522.json、图片生成/文生图/1910971389912805378.json、图片生成/文生图/1911939065036636162.json、图片生成/文生图/1951288817326215170.json、图片生成/文生图/1953188609090326530.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/6 个有
- `FluxGuidance` —— 2/6 个有
- `NunchakuFluxDiTLoader` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CFGZeroStarAndInit` —— 1/6 个有
- `LatentUpscale` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1536 | 6 | 71% |
| 高度 | 944 | 512 - 1280 | 6 | 73% |
| 采样步数 | 20 | 5 - 25 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1536，6 个样本
- 高度 中位数 944，观测区间 512 - 1280，6 个样本
- 采样步数 中位数 20，观测区间 5 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
