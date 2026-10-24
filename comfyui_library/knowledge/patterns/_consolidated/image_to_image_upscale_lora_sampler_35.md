---
name: image_to_image_upscale_lora_sampler_35
type: Image To Image
frequency: 5
level: strong
coverage: 0.906
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageConcanate, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最强图片去水印无痕-图片编辑P图qwen_Edit_2511_2083134406503526402.json, 图片生成/图生图/最强老照片修复-真实自然-Qwen_Image_Edit_2511_2005878268911906818.json, 图片生成/文生图/最强图片去水印无痕-图片编辑P图qwen_Edit_2511_2072192443851821057.json, 图片生成/文生图/解说漫-人物拼接-2人_2057418782854967297.json, 图片生成/文生图/解说漫-人物拼接-3人_2058559683757170689.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/最强图片去水印无痕-图片编辑P图qwen_Edit_2511_2083134406503526402.json、图片生成/图生图/最强老照片修复-真实自然-Qwen_Image_Edit_2511_2005878268911906818.json、图片生成/文生图/最强图片去水印无痕-图片编辑P图qwen_Edit_2511_2072192443851821057.json、图片生成/文生图/解说漫-人物拼接-2人_2057418782854967297.json、图片生成/文生图/解说漫-人物拼接-3人_2058559683757170689.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageConcanate`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImpactMinMax` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `easy saveText` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
