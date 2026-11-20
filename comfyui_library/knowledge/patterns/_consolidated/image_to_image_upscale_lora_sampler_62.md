---
name: image_to_image_upscale_lora_sampler_62
type: Image To Image
frequency: 3
level: moderate
coverage: 0.67
common_nodes: [AILab_ImagePreview, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, GetImageSizeAndCount, Image Comparer (rgthree), ImageConcanate, ImageScaleToMaxDimension, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VRAMReserver, easy boolean, easy ifElse]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009.json, 图片生成/图生图/图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530.json, 图片生成/图生图/图片编辑：增加写实效果图像转写实，支持二次元、动漫_2068535263265124354.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动漫转写实_动漫转真人_QwenEdit或者Flux2Klein+Zimage去除AI感_2031737816035627009.json、图片生成/图生图/图片编辑_万物转写实_动漫转真人_QwenEdit+Flux2Klein+Zimage_2019093722901782530.json、图片生成/图生图/图片编辑：增加写实效果图像转写实，支持二次元、动漫_2068535263265124354.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_ImagePreview`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageScaleToMaxDimension`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VRAMReserver`
- `easy boolean`
- `easy ifElse`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
