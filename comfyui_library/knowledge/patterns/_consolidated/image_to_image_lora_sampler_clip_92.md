---
name: image_to_image_lora_sampler_clip_92
type: Image To Image
frequency: 3
level: strong
coverage: 0.924
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein精修产品_2032304129116217345.json, 图片生成/图生图/影视创作资产创建（自用）_2040024681272578049.json, 图片生成/图生图/极致细节局部改色改材质——Klein+Kontext_2019653894099443714.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Klein精修产品_2032304129116217345.json、图片生成/图生图/影视创作资产创建（自用）_2040024681272578049.json、图片生成/图生图/极致细节局部改色改材质——Klein+Kontext_2019653894099443714.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ConstrainImage|pysssss` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `RH_Nano_Banana2_Image2Image` —— 2/3 个有
- `String` —— 2/3 个有
- `Easy_QwenEdit2509` —— 1/3 个有
- `FL_ColorPicker` —— 1/3 个有
- `GoogleTranslator` —— 1/3 个有
- `Image Filter Adjustments` —— 1/3 个有
- `Qwen3TTSModelLoader` —— 1/3 个有
- `Qwen3TTSVoiceDesign` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SimpleMathSlider+` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `ttN text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 3 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
