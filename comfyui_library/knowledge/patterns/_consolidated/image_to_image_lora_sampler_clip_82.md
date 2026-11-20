---
name: image_to_image_lora_sampler_clip_82
type: Image To Image
frequency: 5
level: strong
coverage: 0.8664
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, ReferenceLatent, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageConcat, easy imageListToImageBatch, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2-klein电商神器超强一键换装多功能超强泛化版_2018495537082798082.json, 图片生成/图生图/flux2-klein电商神器超强一键换装多功能超强泛化版_2028167962842112001.json, 平台全量/flux2-klein服装提取+一键换装_2020497908436574209.json, 平台全量/【电商换装】人物不变一键换装 先提取白底图再换装_2052912722181931009.json, 平台全量/内衣内裤电商高清-flux2-klein电商神器一键换装（f2k板）_2082323825349447681.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux2-klein电商神器超强一键换装多功能超强泛化版_2018495537082798082.json、图片生成/图生图/flux2-klein电商神器超强一键换装多功能超强泛化版_2028167962842112001.json、平台全量/flux2-klein服装提取+一键换装_2020497908436574209.json、平台全量/【电商换装】人物不变一键换装 先提取白底图再换装_2052912722181931009.json、平台全量/内衣内裤电商高清-flux2-klein电商神器一键换装（f2k板）_2082323825349447681.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ReferenceLatent`
- `SaveImage`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageConcat`
- `easy imageListToImageBatch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/5 个有
- `ColorMatch` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ImageScale` —— 1/5 个有
- `ImpactNeg` —— 1/5 个有
- `InpaintCropImproved` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerColor: BrightnessContrastV2` —— 1/5 个有
- `LayerMask: MaskGrow` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有
- `MaskPreview` —— 1/5 个有
- `Preview from image [Crystools]` —— 1/5 个有
- `SmartColorMatch` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `easy isMaskEmpty` —— 1/5 个有
- `图像接缝` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（19/5 个样本）：Steps较低可能导致细节不足
