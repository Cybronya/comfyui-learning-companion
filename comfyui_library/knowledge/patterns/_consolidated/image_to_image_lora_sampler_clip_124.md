---
name: image_to_image_lora_sampler_clip_124
type: Image To Image
frequency: 4
level: strong
coverage: 0.78225
common_nodes: [AnyBooleanSwitch, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, GetNode, If ANY execute A else B, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJv2, ImpactImageBatchToImageList, KSampler, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PresetGroupEditor, PresetSwitch, PreviewImage, ReferenceLatent, SZ_KleinTiledKSamplerColorFix, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, ZML_BooleanSwitch, easy imageColorMatch, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/终极产品精修2-场景版_2088698214701682690.json, 平台全量/终极产品精修——（白底+场景二合一7.21）.app_2079463999317561346.json, 平台全量/终极高清放大1——一致性版+高清+zimage质感_2082647540767477762.json, 平台全量/终极高清放大2——洗图版+高清+zimage质感_2081917946275913730.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/终极产品精修2-场景版_2088698214701682690.json、平台全量/终极产品精修——（白底+场景二合一7.21）.app_2079463999317561346.json、平台全量/终极高清放大1——一致性版+高清+zimage质感_2082647540767477762.json、平台全量/终极高清放大2——洗图版+高清+zimage质感_2081917946275913730.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `AnyBooleanSwitch`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `GetNode`
- `If ANY execute A else B`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJv2`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PresetGroupEditor`
- `PresetSwitch`
- `PreviewImage`
- `ReferenceLatent`
- `SZ_KleinTiledKSamplerColorFix`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `ZML_BooleanSwitch`
- `easy imageColorMatch`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `KSamplerWithNAG` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `Text` —— 2/4 个有
- `TextConcatenate` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `easy float` —— 2/4 个有
- `easy imageSizeByLongerSide` —— 2/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.35 - 1 | 4 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
