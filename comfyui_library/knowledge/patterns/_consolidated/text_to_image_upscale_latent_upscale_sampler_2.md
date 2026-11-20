---
name: text_to_image_upscale_latent_upscale_sampler_2
type: Text To Image
frequency: 3
level: weak
coverage: 0.962333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LatentUpscaleBy, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/zimage红潮黑兽 AIO_2003262784529924098.json, 图片生成/文生图/【开箱即用】Anima base 原版基础工作流_2055002507641933826.json, 图片生成/文生图/压缩_2046649589238861825.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/zimage红潮黑兽 AIO_2003262784529924098.json、图片生成/文生图/【开箱即用】Anima base 原版基础工作流_2055002507641933826.json、图片生成/文生图/压缩_2046649589238861825.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LatentUpscaleBy`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `CR Prompt Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `CompressImages` —— 1/3 个有
- `IfInnerExecute` —— 1/3 个有
- `ImageListToBatch_` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 30 | 3 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 33% |
| 重绘幅度 | 0.75 | 0.75 - 1 | 3 | 86% |
| 宽度 | 1024 | 896 - 1280 | 3 | 85% |
| 高度 | 1536 | 1152 - 1920 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 30，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 33%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 1，3 个样本，取值集中（一致性 86%）
- 宽度 中位数 1024，观测区间 896 - 1280，3 个样本，取值集中（一致性 85%）
- 高度 中位数 1536，观测区间 1152 - 1920，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
