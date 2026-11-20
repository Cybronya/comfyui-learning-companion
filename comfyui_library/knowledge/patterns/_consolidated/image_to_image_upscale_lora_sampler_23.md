---
name: image_to_image_upscale_lora_sampler_23
type: Image To Image
frequency: 8
level: moderate
coverage: 0.898625
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/溶图打光Kontext-V2_2023704917680070658.json, 图片生成/图生图/🦖产品精修_2011619538990796802.json, 平台全量/Kontext _ 极致细节局部改色_1997193162445754369.json, 平台全量/Kontext _ 渲染级珠宝首饰精修_2009864841212727297.json, 平台全量/Kontext位置不变溶图打光_1964854734442086402.json, 平台全量/Kontext渲染级光影重塑产品精修V3_1964194222322667522.json, 平台全量/【产品精修】Kontext _ 渲染级全类目 电商一键产品精修 高清放大+细节微调 修复_2009063784991694850.json, 平台全量/光影融合 电商产品 位置不变溶图打光 Kontext  产品精修+高清放大 超实用版_2009096099356741633.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/溶图打光Kontext-V2_2023704917680070658.json、图片生成/图生图/🦖产品精修_2011619538990796802.json、平台全量/Kontext _ 极致细节局部改色_1997193162445754369.json、平台全量/Kontext _ 渲染级珠宝首饰精修_2009864841212727297.json、平台全量/Kontext位置不变溶图打光_1964854734442086402.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 4/8 个有
- `Image Filter Adjustments` —— 4/8 个有
- `JoinStrings` —— 4/8 个有
- `LayerUtility: ImageMaskScaleAs` —— 4/8 个有
- `PixaromaLabel` —— 4/8 个有
- `String` —— 4/8 个有
- `ColorMatchImage` —— 3/8 个有
- `DF_Get_image_size` —— 3/8 个有
- `ImageComposite+` —— 3/8 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 3/8 个有
- `MaskFastGrow` —— 3/8 个有
- `RMBG` —— 3/8 个有
- `孤海图像缩放按像素` —— 3/8 个有
- `SimpleMathSlider+` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `GoogleTranslator` —— 1/8 个有
- `MaskToImage` —— 1/8 个有
- `Mix Images By Mask` —— 1/8 个有
- `easy imageColorMatch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 30 | 8 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 0.4 - 1 | 8 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，8 个样本
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
