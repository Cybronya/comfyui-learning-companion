---
name: image_to_image_sampler_clip_unet_192
type: Image To Image
frequency: 3
level: weak
coverage: 0.876667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSize, ImageScaleToTotalPixels, KSampler, LatentCutToBatch, LatentFromBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/图像分层极速版 图生分层 文生分层 一键切换_2002200260816564226.json, 图片生成/文生图/图生图层 文生图层 极速版_2002553833609916418.json, 平台全量/Qwen Image Layered千问——图层分层_2002388774589984770.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/图像分层极速版 图生分层 文生分层 一键切换_2002200260816564226.json、图片生成/文生图/图生图层 文生图层 极速版_2002553833609916418.json、平台全量/Qwen Image Layered千问——图层分层_2002388774589984770.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LatentCutToBatch`
- `LatentFromBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `Int` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `TwoWaySwitch` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 40 | 3 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 40，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
