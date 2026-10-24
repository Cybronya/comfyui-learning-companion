---
name: text_to_image_upscale_lora_sampler_85
type: Text To Image
frequency: 3
level: moderate
coverage: 0.914
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToMaxDimension, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键24角度图 2511_2082246214036320258.json, 图片生成/图生图/人物洗图专用-klein_2069362494073827330.json, 图片生成/图生图/洗图 2511_2071383993899110402.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键24角度图 2511_2082246214036320258.json、图片生成/图生图/人物洗图专用-klein_2069362494073827330.json、图片生成/图生图/洗图 2511_2071383993899110402.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToMaxDimension`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `HAIGC_SaveImagesToZip` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 9 | 3 | 0% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 928 | 928 - 1200 | 3 | 87% |
| 高度 | 1664 | 1664 - 1792 | 3 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 9，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 928，观测区间 928 - 1200，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1664，观测区间 1664 - 1792，3 个样本，取值集中（一致性 96%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
