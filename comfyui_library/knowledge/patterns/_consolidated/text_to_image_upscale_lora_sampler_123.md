---
name: text_to_image_upscale_lora_sampler_123
type: Text To Image
frequency: 2
level: weak
coverage: 0.912
common_nodes: [BasicScheduler, CFGNorm, CLIPLoader, CLIPTextEncode, ColorCorrect, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, FluxKontextMultiReferenceLatentMethod, GetImageSize, GetNode, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, MuyeTextEditOutput, PreviewImage, QwenEditConfigPreparer, QwenEditOutputExtractor_EditUtils, ReferenceLatent, SamplerCustom, SaveImage, Switch any [Crystools], TextEncodeBooguEdit, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, ZML_BooleanSwitch, easy cleanGpuUsed, easy imageSizeByLongerSide, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转真人——2509+Fire+Klein+2511+Boogu五合一_2077213496990855169.json, 图片生成/图生图/动漫转真人——2509+Fire+Klein+2511+Boogu五合一_2077217038237528066.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/动漫转真人——2509+Fire+Klein+2511+Boogu五合一_2077213496990855169.json、图片生成/图生图/动漫转真人——2509+Fire+Klein+2511+Boogu五合一_2077217038237528066.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorCorrect`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `MuyeTextEditOutput`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor_EditUtils`
- `ReferenceLatent`
- `SamplerCustom`
- `SaveImage`
- `Switch any [Crystools]`
- `TextEncodeBooguEdit`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `ZML_BooleanSwitch`
- `easy cleanGpuUsed`
- `easy imageSizeByLongerSide`
- `easy promptConcat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（10/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
