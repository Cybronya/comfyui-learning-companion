---
name: text_to_image_inpaint_lora_sampler_7
type: Text To Image
frequency: 2
level: weak
coverage: 0.7515
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, HAIGC_SaveImagesToZip, Image Comparer (rgthree), InpaintCrop, InpaintStitch, Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SetNode, Switch any [Crystools], UNETLoader, VAEDecode, VAELoader, ZML_BooleanSwitch, easy positive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部重绘擦除｜2511+Klein裁剪贴回图生图处理_2089804379699372033.json, 图片生成/文生图/局部重绘加参考图生图超逼真超写实没有AI味道改图，文生图图生图处理方案_2107621060131778562.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/局部重绘擦除｜2511+Klein裁剪贴回图生图处理_2089804379699372033.json、图片生成/文生图/局部重绘加参考图生图超逼真超写实没有AI味道改图，文生图图生图处理方案_2107621060131778562.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `GetNode`
- `HAIGC_SaveImagesToZip`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintStitch`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZML_BooleanSwitch`
- `easy positive`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `CropWithPadInfo` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `QwenEditConfigPreparer` —— 1/2 个有
- `QwenEditOutputExtractor` —— 1/2 个有
- `StringReplace` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/2 个有
- `TextGenerate` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
