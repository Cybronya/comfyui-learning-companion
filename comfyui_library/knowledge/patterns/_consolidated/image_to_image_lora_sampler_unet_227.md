---
name: image_to_image_lora_sampler_unet_227
type: Image To Image
frequency: 3
level: strong
coverage: 0.952667
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, GetImageSizeAndCount, ImageAndMaskPreview, ImageConcanate, ImageResizeKJ, ImageScaleToTotalPixels, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/生图-图换装手动遮罩-qwen-Edit-2509-8步_1983500012187492353.json, 图片生成/图生图/生图-图换装自动遮罩-qwen-Edit-2509-8步_1983510280296669186.json, 平台全量/-qwenEdit自动换装，细节一致_1985889027666653185.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_227

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/生图-图换装手动遮罩-qwen-Edit-2509-8步_1983500012187492353.json、图片生成/图生图/生图-图换装自动遮罩-qwen-Edit-2509-8步_1983510280296669186.json、平台全量/-qwenEdit自动换装，细节一致_1985889027666653185.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `GetImageSizeAndCount`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
