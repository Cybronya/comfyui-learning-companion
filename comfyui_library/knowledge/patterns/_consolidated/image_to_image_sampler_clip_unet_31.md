---
name: image_to_image_sampler_clip_unet_31
type: Image To Image
frequency: 12
level: moderate
coverage: 0.92025
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSize, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Layered千问分层模型图生图｜可保存psd格式_2009193920273584130.json, 图片生成/图生图/Layered图像分层保存PSD_2003684455141261314.json, 图片生成/图生图/Layered图像分层保存PSD_2003695445341839362.json, 图片生成/图生图/Qwen Image Layered 千问分层图_2003086755085582337.json, 图片生成/图生图/Qwen Image Layered千问分层模型-八步_2003987627701379074.json, 图片生成/图生图/Qwen Image Layered千问分层模型_2002955308945293313.json, 图片生成/图生图/Qwen Image Layered千问分层模型_2028670546195521538.json, 图片生成/图生图/Qwen Image Layered千问分层模型_2049685445046444033.json, 图片生成/图生图/Qwen图像分层_2003684024012947457.json, 图片生成/图生图/Qwen图像自动分层(带alpha通道）ImageLayered千问分层模型_2002183316642119681.json, 图片生成/图生图/千问图层分解（Qwen Layered）_2004093169174257665.json, 平台全量/Qwen Layered：千问拆解图像、png图层_2003022952759193602.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Layered千问分层模型图生图｜可保存psd格式_2009193920273584130.json、图片生成/图生图/Layered图像分层保存PSD_2003684455141261314.json、图片生成/图生图/Layered图像分层保存PSD_2003695445341839362.json、图片生成/图生图/Qwen Image Layered 千问分层图_2003086755085582337.json、图片生成/图生图/Qwen Image Layered千问分层模型-八步_2003987627701379074.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LatentFromBatch` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 7/12 个有
- `ImageScaleToTotalPixels` —— 7/12 个有
- `Int` —— 7/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `MathExpression|pysssss` —— 4/12 个有
- `HAIGC_SavePSD` —— 3/12 个有
- `ImageScaleBy` —— 3/12 个有
- `Text Multiline` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `ConstrainImage|pysssss` —— 2/12 个有
- `LayerUtility: PurgeVRAM` —— 2/12 个有
- `SimpleMath+` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `Float` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 12 | 49% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 12 | 57% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，12 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
