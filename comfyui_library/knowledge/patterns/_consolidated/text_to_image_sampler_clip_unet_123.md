---
name: text_to_image_sampler_clip_unet_123
type: Text To Image
frequency: 3
level: strong
coverage: 0.635667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, ImageScaleBy, KSampler, PathchSageAttentionKJ, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-Boogu 文生图 + 双图像编辑工作流_2071601741841395714.json, 图片生成/文生图/krea2 Turbo 文生图 二级采样工作流_2070366019469795330.json, 图片生成/文生图/krea2+Turbo+文生图+二级采样工作流_2087104857244262401.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2-Boogu 文生图 + 双图像编辑工作流_2071601741841395714.json、图片生成/文生图/krea2 Turbo 文生图 二级采样工作流_2070366019469795330.json、图片生成/文生图/krea2+Turbo+文生图+二级采样工作流_2087104857244262401.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `SamplerCustom` —— 1/3 个有
- `TextEncodeBooguEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 2560 | 1280 - 2560 | 3 | 72% |
| 高度 | 1440 | 720 - 1440 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 2560，观测区间 1280 - 2560，3 个样本
- 高度 中位数 1440，观测区间 720 - 1440，3 个样本
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
