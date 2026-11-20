---
name: text_to_image_sampler_clip_unet_165
type: Text To Image
frequency: 4
level: moderate
coverage: 0.61725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, ImageScaleBy, KSampler, PathchSageAttentionKJ, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-Boogu 文生图 + 双图像编辑工作流_2071601741841395714.json, 图片生成/文生图/krea2 Turbo 文生图 二级采样工作流_2070366019469795330.json, 图片生成/文生图/krea2 Turbo 文生图 二级采样工作流（自用）_2110705045959430146.json, 图片生成/文生图/krea2+Turbo+文生图+二级采样工作流_2087104857244262401.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-Boogu 文生图 + 双图像编辑工作流_2071601741841395714.json、图片生成/文生图/krea2 Turbo 文生图 二级采样工作流_2070366019469795330.json、图片生成/文生图/krea2 Turbo 文生图 二级采样工作流（自用）_2110705045959430146.json、图片生成/文生图/krea2+Turbo+文生图+二级采样工作流_2087104857244262401.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleBy`
- `KSampler`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `BasicScheduler` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `SamplerCustom` —— 1/4 个有
- `TextEncodeBooguEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.1 - 1 | 4 | 50% |
| 宽度 | 2560 | 1280 - 2560 | 4 | 75% |
| 高度 | 1440 | 720 - 1440 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，4 个样本，取值分散，一致性仅 50%
- 宽度 中位数 2560，观测区间 1280 - 2560，4 个样本
- 高度 中位数 1440，观测区间 720 - 1440，4 个样本
- 高发问题（9/4 个样本）：Steps较低可能导致细节不足
