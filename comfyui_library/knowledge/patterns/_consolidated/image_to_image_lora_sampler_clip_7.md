---
name: image_to_image_lora_sampler_clip_7
type: Image To Image
frequency: 14
level: strong
coverage: 0.798214
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, LoraLoaderModelOnly, PrimitiveInt, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/4K高清放大-kontext_hires_1965049280929087489.json, 图片生成/图生图/AI绘画_葫芦娃Kontext模型+汤团猪TTP高清放大工作流V1_1963594370137280514.json, 图片生成/图生图/Kontext__hires高清放大_1965035145029931010.json, 图片生成/图生图/Kontext_超分辨率_hires_1965724218900021250.json, 图片生成/图生图/Kontext高清放大_1977933593064472577.json, 图片生成/图生图/Kontext，葫芦娃极致放大_1963623455676780546.json, 图片生成/图生图/kontext_hires try_1963899464674267137.json, 图片生成/图生图/kontext_hires+TTP 4K高清放大_1965317062409244673.json, 图片生成/图生图/kontext_hires放大_2073049969321406465.json, 图片生成/图生图/kontext使用hires lora高清修复细节放大_1964562881654177794.json, 图片生成/图生图/kontext服装工作流_1963869080980901890.json, 图片生成/图生图/香蕉， Kontext，葫芦娃极致放大_1963615168336056321.json, 图片生成/图生图/高清放大 kontext 葫芦娃lora_1964938211141275650.json, 图片生成/图生图/高清放大Kontext（商用级）_1989122752181317633.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/4K高清放大-kontext_hires_1965049280929087489.json、图片生成/图生图/AI绘画_葫芦娃Kontext模型+汤团猪TTP高清放大工作流V1_1963594370137280514.json、图片生成/图生图/Kontext__hires高清放大_1965035145029931010.json、图片生成/图生图/Kontext_超分辨率_hires_1965724218900021250.json、图片生成/图生图/Kontext高清放大_1977933593064472577.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageListToBatch+` —— 13/14 个有
- `TeaCache` —— 13/14 个有
- `LayerUtility: Seed` —— 12/14 个有
- `ImpactImageBatchToImageList` —— 8/14 个有
- `LayerUtility: ImageMaskScaleAs` —— 7/14 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 7/14 个有
- `ImageBatchToList+` —— 6/14 个有
- `PreviewImage` —— 4/14 个有
- `EasyCache` —— 1/14 个有
- `EmptySD3LatentImage` —— 1/14 个有
- `FluxKontextImageScale` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `ImageListToImageBatch` —— 1/14 个有
- `ImageStitch` —— 1/14 个有
- `ImpactMinMax` —— 1/14 个有
- `LayerUtility: GetImageSize` —— 1/14 个有
- `MathExpression_UTK` —— 1/14 个有
- `RepeatLatentBatch` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有
- `easy imageSize` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
