---
name: image_to_image_sampler_clip_unet_164
type: Image To Image
frequency: 4
level: weak
coverage: 0.92575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSize, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/一键运行：Qwen-Image-Layered 分层工作流_2005185681511116802.json, 平台全量/千问分层 图片抠图分层编辑 Qwen Image Layered_2002895188135669762.json, 平台全量/千问分层模型-Qwen-Image-Layered_2002193425996890114.json, 平台全量/后期PS必备！图片自动分层qwen-image-layered-image2image_2006181248108077057.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/一键运行：Qwen-Image-Layered 分层工作流_2005185681511116802.json、平台全量/千问分层 图片抠图分层编辑 Qwen Image Layered_2002895188135669762.json、平台全量/千问分层模型-Qwen-Image-Layered_2002193425996890114.json、平台全量/后期PS必备！图片自动分层qwen-image-layered-image2image_2006181248108077057.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetImageSize`
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
- `ImageScaleToTotalPixels` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LatentFromBatch` —— 2/4 个有
- `ImageResize+` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `ZImageLoraModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 8 - 40 | 4 | 33% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 24，观测区间 8 - 40，4 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
