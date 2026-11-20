---
name: image_to_image_inpaint_lora_sampler_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.705
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyFlux2LatentImage, Fast Groups Muter (rgthree), Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, HAIGC_SaveImagesToZip, Image Comparer (rgthree), InpaintCrop, InpaintStitch, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, ReferenceLatent, SaveImage, SetNode, StringReplace, Switch any [Crystools], TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, ZML_BooleanSwitch, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/局部重绘+参考图生图超逼真超写实没有AI味道改图_2106984431608225793.json, 图片生成/文生图/局部重绘超逼真超写实没有AI味道改图_2055182043314704386.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/局部重绘+参考图生图超逼真超写实没有AI味道改图_2106984431608225793.json、图片生成/文生图/局部重绘超逼真超写实没有AI味道改图_2055182043314704386.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `EmptyFlux2LatentImage`
- `Fast Groups Muter (rgthree)`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `GetNode`
- `HAIGC_SaveImagesToZip`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintStitch`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `StringReplace`
- `Switch any [Crystools]`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `ZML_BooleanSwitch`
- `easy positive`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | - | 2 | 84% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
