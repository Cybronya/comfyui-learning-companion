---
name: image_to_image_lora_sampler_unet_143
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8436
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image_字体直出_字体设计_书法字体_综艺字体_海报生成QwenEdit_1982996678984773634.json, 图片生成/文生图/最新千问图像编辑_1970656696915927042.json, 数字人/数字人/【老金驿站】Qwen2509肌肤改善器工作流_1985948966875537410.json, 数字人/数字人/替换物品，人物，让人物穿上你想要的衣服，鞋子_2032482079761502210.json, 视频生成/文生视频/QwenEdit 2511（FH修复油腻感模型）_2004948756900573185.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_143

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-Image_字体直出_字体设计_书法字体_综艺字体_海报生成QwenEdit_1982996678984773634.json、图片生成/文生图/最新千问图像编辑_1970656696915927042.json、数字人/数字人/【老金驿站】Qwen2509肌肤改善器工作流_1985948966875537410.json、数字人/数字人/替换物品，人物，让人物穿上你想要的衣服，鞋子_2032482079761502210.json、视频生成/文生视频/QwenEdit 2511（FH修复油腻感模型）_2004948756900573185.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `TextEncodeQwenImageEdit` —— 2/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `NunchakuQwenImageDiTLoader` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 5 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，5 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
