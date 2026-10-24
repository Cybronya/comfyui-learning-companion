---
name: image_to_image_sampler_clip_unet_146
type: Image To Image
frequency: 3
level: moderate
coverage: 0.921333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问 Image Layered 分层助手，美工的好帮手!_2037626157163614210.json, 图片生成/图生图/千问分层 Image Layered_2002530524985999361.json, 图片生成/图生图/生图-图像分层-Qwen Image Layered_2004025316857290754.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问 Image Layered 分层助手，美工的好帮手!_2037626157163614210.json、图片生成/图生图/千问分层 Image Layered_2002530524985999361.json、图片生成/图生图/生图-图像分层-Qwen Image Layered_2004025316857290754.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy int` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy positive` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 3 | 49% |
| Prompt 约束强度(CFG) | 4 | 2 - 4 | 3 | 72% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 4，观测区间 2 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
