---
name: image_to_image_lora_sampler_unet_60
type: Image To Image
frequency: 11
level: strong
coverage: 0.830909
common_nodes: [Any Switch (rgthree), CLIPLoader, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json, 图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029367604804067329.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049.json, 图片生成/图生图/小红书全能编辑模型FireRed-Image-edit1.0_2026605916237336577.json, 图片生成/文生图/2029537706899935234.json, 平台全量/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029545976440037377.json, 平台全量/小红书FireRed-Image-edit1.1_编辑模型_2029372203904540674.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json、图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json、图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json、图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029367604804067329.json、图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 10/11 个有
- `AddLabel` —— 9/11 个有
- `CFGNorm` —— 9/11 个有
- `CR Image Grid Panel` —— 9/11 个有
- `Image Batch` —— 9/11 个有
- `KOOK_SaveJPGImage` —— 9/11 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 9/11 个有
- `ModelSamplingAuraFlow` —— 9/11 个有
- `CR Prompt Text` —— 7/11 个有
- `CheckpointLoaderSimple` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `CR SDXL Aspect Ratio` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 11 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | beta | - | 11 | 45% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，11 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 beta，11 个样本，一致性 45%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
