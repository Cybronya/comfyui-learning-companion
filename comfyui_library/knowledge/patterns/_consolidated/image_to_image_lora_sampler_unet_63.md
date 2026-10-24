---
name: image_to_image_lora_sampler_unet_63
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9204
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2003601727951675393.json, 图片生成/图生图/图片-人物提取衣服_1970397980127883265.json, 图片生成/图生图/图片去水印_2078417815333330946.json, 图片生成/图生图/图片去水印_优化版（速度不做高清放大）_2087830057820708866.json, 图片生成/图生图/图片快速转线稿_2087107562218016770.json, 图片生成/图生图/多角度打光，万能打光 qwen2511_2033554182464081922.json, 图片生成/图生图/自由打光，万能打光 Qwen_2033684576970739713.json, 图片生成/文生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2079820923355615233.json, 图片生成/文生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2079833773604171778.json, 图片生成/文生图/最新千问图像编辑_1970656696915927042.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2003601727951675393.json、图片生成/图生图/图片-人物提取衣服_1970397980127883265.json、图片生成/图生图/图片去水印_2078417815333330946.json、图片生成/图生图/图片去水印_优化版（速度不做高清放大）_2087830057820708866.json、图片生成/图生图/图片快速转线稿_2087107562218016770.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 8/10 个有
- `DWPreprocessor` —— 3/10 个有
- `InpaintModelConditioning` —— 3/10 个有
- `Mask Fill Holes` —— 3/10 个有
- `SDXLEmptyLatentSizePicker+` —— 3/10 个有
- `TextEncodeQwenImageEdit` —— 3/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/10 个有
- `QwenMultiangleLightningNode` —— 2/10 个有
- `ShowText` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 10 | 31% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 54% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 768x1280 (0.6) | - | 3 | 100% |
| 高度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，10 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 最常用 768x1280 (0.6)，3 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（18/10 个样本）：Steps较低可能导致细节不足
