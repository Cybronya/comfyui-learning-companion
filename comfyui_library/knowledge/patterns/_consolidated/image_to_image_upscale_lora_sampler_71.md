---
name: image_to_image_upscale_lora_sampler_71
type: Image To Image
frequency: 3
level: moderate
coverage: 0.694
common_nodes: [CLIPLoader, CLIPTextEncode, DeepTranslatorTextNode, EmptySD3LatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, JWImageResizeByLongerSide, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen_Image_2512文生图、图生图工作流合集_2021495595986325505.json, 图片生成/文生图/Qwen_Image_2512文生图、图生图工作流合集_2062004710315487234.json, 图片生成/文生图/工作流千问篇8-Qwen千问-Image_2512文生图-图生图工作流合集_2026210359081701377.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen_Image_2512文生图、图生图工作流合集_2021495595986325505.json、图片生成/文生图/Qwen_Image_2512文生图、图生图工作流合集_2062004710315487234.json、图片生成/文生图/工作流千问篇8-Qwen千问-Image_2512文生图-图生图工作流合集_2026210359081701377.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 3 | 80% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
