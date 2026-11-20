---
name: image_to_image_sampler_clip_unet_153
type: Image To Image
frequency: 4
level: moderate
coverage: 0.957
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux-风格重绘_1977744193269497858.json, 图片生成/图生图/图生图修复_1914984999924264962.json, 图片生成/文生图/图生图修复_1930828932625399809.json, 平台全量/Redux智能风格迁移-原创无忧，风格自由_1928250396362588162.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux-风格重绘_1977744193269497858.json、图片生成/图生图/图生图修复_1914984999924264962.json、图片生成/文生图/图生图修复_1930828932625399809.json、平台全量/Redux智能风格迁移-原创无忧，风格自由_1928250396362588162.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `StyleModelApply` —— 2/4 个有
- `StyleModelLoader` —— 2/4 个有
- `DF_Image_scale_to_side` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 4 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 0.725 | 0.45 - 1 | 4 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 0.725，观测区间 0.45 - 1，4 个样本
