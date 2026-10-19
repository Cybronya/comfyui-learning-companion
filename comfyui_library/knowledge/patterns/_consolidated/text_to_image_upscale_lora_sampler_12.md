---
name: text_to_image_upscale_lora_sampler_12
type: Text To Image
frequency: 3
level: strong
coverage: 0.707333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GrowMask, Image Comparer (rgthree), ImageUpscaleWithModel, Int, InvertMask, JjkText, JoinImageWithAlpha, KSampler, KuwaharaBlur, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, SaveImage, UNETLoader, Upscale Model Loader, VAEDecode, VAELoader, easy boolean, easy ifElse, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerColor: Color of Shadow & Highlight, LayerColor: RGB, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: PurgeVRAM V2, easy boolean, easy cleanGpuUsed, easy imageColorMatch, Latent Noise Injection, Upscale Model Loader, ImageResize+]
members: [图片生成/反推提示词/通用放大终版改变较大 图片分辨率提升方案_2104996402978975745.json, 图片生成/图生图/2102172784855183362.json, 图片生成/图生图/2102175922328788993.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/通用放大终版改变较大 图片分辨率提升方案_2104996402978975745.json、图片生成/图生图/2102172784855183362.json、图片生成/图生图/2102175922328788993.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `Int`
- `InvertMask`
- `JjkText`
- `JoinImageWithAlpha`
- `KSampler`
- `KuwaharaBlur`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy ifElse`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `Latent Noise Injection` —— 2/3 个有
- `LayerColor: Color of Shadow & Highlight` —— 2/3 个有
- `LayerColor: RGB` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageColorMatch` —— 2/3 个有
- `DF_Integer` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `YUAN_TXTConvertAny` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerColor: Color of Shadow & Highlight、LayerColor: RGB、LayerMask: BiRefNetUltraV2、LayerMask: LoadBiRefNetModelV2
