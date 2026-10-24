---
name: image_to_image_sampler_clip_unet_18
type: Image To Image
frequency: 12
level: strong
coverage: 0.902917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSize, HAIGC_SavePSD, ImageScaleToTotalPixels, Int, KSampler, LatentCutToBatch, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键详情页，ai详情页，小白一秒变大神，一张图15分钟一个详情页，可出psd分层_2020862036552458241.json, 图片生成/图生图/全品类电商视觉・主图详情页定制_2045548588943548418.json, 图片生成/图生图/全品类详情页定制_2046485204256165890.json, 图片生成/图生图/全能图片V1 Pro详情页生成PSD分层保存_2008049758597812226.json, 图片生成/图生图/分层工作流_2092101423088619522.json, 图片生成/图生图/千问Layered图像分层psd格式保存（图生图）_2002283462897856513.json, 图片生成/图生图/图像分层保存为psd_2007698589761409025.json, 图片生成/图生图/图片拆分PSD_2013458625578147841.json, 图片生成/图生图/梨梨AI-图片拆分PSD_2026603437491757058.json, 图片生成/图生图/电商详情页生成PSD分层_2019521290964574209.json, 图片生成/文生图/国内商品详情页生成（PSD分层保存）_2008783090499461121.json, 视频生成/图生视频/全能图片V1 Pro详情页生成PSD分层保存_2011639539646865410.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/一键详情页，ai详情页，小白一秒变大神，一张图15分钟一个详情页，可出psd分层_2020862036552458241.json、图片生成/图生图/全品类电商视觉・主图详情页定制_2045548588943548418.json、图片生成/图生图/全品类详情页定制_2046485204256165890.json、图片生成/图生图/全能图片V1 Pro详情页生成PSD分层保存_2008049758597812226.json、图片生成/图生图/分层工作流_2092101423088619522.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetImageSize`
- `HAIGC_SavePSD`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LatentCutToBatch`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `HAIGC_Layer` —— 11/12 个有
- `HAIGC_CombineUnits` —— 10/12 个有
- `CR Text` —— 7/12 个有
- `PromptBatchQueue` —— 7/12 个有
- `RH_LLMAPI_Pro_Node` —— 7/12 个有
- `RH_Nano_Banana2_Image2Image` —— 7/12 个有
- `easy showAnything` —— 7/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 55% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
