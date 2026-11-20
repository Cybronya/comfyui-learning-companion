---
name: image_to_image_sampler_clip_unet_143
type: Image To Image
frequency: 3
level: moderate
coverage: 0.977667
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-风格重绘_1977744193269497858.json, 图片生成/图生图/图生图修复_1914984999924264962.json, 图片生成/文生图/图生图修复_1930828932625399809.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_143

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux-风格重绘_1977744193269497858.json、图片生成/图生图/图生图修复_1914984999924264962.json、图片生成/文生图/图生图修复_1930828932625399809.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RepeatLatentBatch` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `StyleModelApply` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 0.45 | 0.45 - 1 | 3 | 59% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 1，3 个样本
