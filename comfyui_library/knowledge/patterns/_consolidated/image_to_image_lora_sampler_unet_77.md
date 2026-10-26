---
name: image_to_image_lora_sampler_unet_77
type: Image To Image
frequency: 8
level: moderate
coverage: 0.904125
common_nodes: [CFGNorm, CLIPLoader, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Edit局部重绘_Qwen-Edit_1967961936698683393.json, 图片生成/图生图/千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754.json, 图片生成/图生图/千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826.json, 图片生成/图生图/转换视角-Qwen-Image-Edit图像编辑_1957970150108577793.json, 图片生成/图生图/转绘-Qwen-Image-Edit图像编辑_1957815011857068034.json, 图片生成/图生图/通义前文Qwen-Image-Edit图像编辑修复版（一致性大大增强）_1958671348539224065.json, 图片生成/图生图/通义千问图片编辑（qwen-edit）_1958158377425784833.json, 图片生成/图生图/🦖转绘-Qwen-Image_1958477176230277122.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_77

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/千问Edit局部重绘_Qwen-Edit_1967961936698683393.json、图片生成/图生图/千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754.json、图片生成/图生图/千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826.json、图片生成/图生图/转换视角-Qwen-Image-Edit图像编辑_1957970150108577793.json、图片生成/图生图/转绘-Qwen-Image-Edit图像编辑_1957815011857068034.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageAndMaskPreview` —— 6/8 个有
- `Text Multiline` —— 6/8 个有
- `ImageScaleDownToSize` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `TextEncodeQwenImageEditEnhanced` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `Mask Fill Holes` —— 1/8 个有
- `RepeatLatentBatch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 8 | 71% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 8 | 79% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
