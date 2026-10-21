---
name: text_to_image_sampler_clip_unet_114
type: Text To Image
frequency: 4
level: moderate
coverage: 0.93
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/zimage红潮黑兽 AIO_2003262784529924098.json, 图片生成/文生图/墨沫深空krea2-RAW 工作流_2077060951261671426.json, 图片生成/文生图/文生图Krea2_2080302375230857217.json, 图片生成/文生图/造相 Z-image 文生图 Ultra_2073291168456200194.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_114

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/zimage红潮黑兽 AIO_2003262784529924098.json、图片生成/文生图/墨沫深空krea2-RAW 工作流_2077060951261671426.json、图片生成/文生图/文生图Krea2_2080302375230857217.json、图片生成/文生图/造相 Z-image 文生图 Ultra_2073291168456200194.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `LatentUpscaleBy` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageSharpen` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 6 - 30 | 4 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 0.75 - 1 | 4 | 88% |
| 宽度 | 1152 | 512 - 1328 | 4 | 69% |
| 高度 | 1432 | 512 - 1920 | 4 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 6 - 30，4 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.75 - 1，4 个样本，取值集中（一致性 88%）
- 宽度 中位数 1152，观测区间 512 - 1328，4 个样本
- 高度 中位数 1432，观测区间 512 - 1920，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
