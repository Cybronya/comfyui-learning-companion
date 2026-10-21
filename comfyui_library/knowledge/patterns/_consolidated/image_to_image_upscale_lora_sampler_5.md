---
name: image_to_image_upscale_lora_sampler_5
type: Image To Image
frequency: 4
level: strong
coverage: 0.93525
common_nodes: [CFGNorm, CLIPLoader, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/最强图片去水印无痕-图片编辑P图qwen_Edit_2511_2072192443851821057.json, 图片生成/文生图/解说漫-人物拼接-2人_2057418782854967297.json, 图片生成/文生图/解说漫-人物拼接-3人_2058559683757170689.json, 视频生成/图生视频/2058721719896076290.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/最强图片去水印无痕-图片编辑P图qwen_Edit_2511_2072192443851821057.json、图片生成/文生图/解说漫-人物拼接-2人_2057418782854967297.json、图片生成/文生图/解说漫-人物拼接-3人_2058559683757170689.json、视频生成/图生视频/2058721719896076290.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `FluxKontextMultiReferenceLatentMethod` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `easy saveText` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImpactMinMax` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
