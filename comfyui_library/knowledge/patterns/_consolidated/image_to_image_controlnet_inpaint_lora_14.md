---
name: image_to_image_controlnet_inpaint_lora_14
type: Image To Image
frequency: 2
level: weak
coverage: 0.899
common_nodes: [AnimeLineArtPreprocessor, ArgosTranslateTextNode, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Overlay Text, CR Overlay Transparent Image, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Float, FluxGuidance, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_LoadFooocusInpaint, Image Comparer (rgthree), ImageCompositeMasked, ImageToMask, ImpactDilateMask, JanusImageUnderstanding, JanusModelLoader, KSampler, KSamplerSelect, LaMaInpainting, LayerUtility: ImageBlend, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, MaskToImage, MirroredImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAEEncodeForInpaint, VAELoader, WD14Tagger|pysssss, YC_LG_Redux]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/梦宛霖壁纸号洗图（动漫、二次元类）_1924330327504769025.json, 图片生成/图生图/壁纸号洗图（动漫、二次元类）_1917113243515420674.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/梦宛霖壁纸号洗图（动漫、二次元类）_1924330327504769025.json、图片生成/图生图/壁纸号洗图（动漫、二次元类）_1917113243515420674.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AnimeLineArtPreprocessor`
- `ArgosTranslateTextNode`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Overlay Text`
- `CR Overlay Transparent Image`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `FluxGuidance`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_LoadFooocusInpaint`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageToMask`
- `ImpactDilateMask`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LaMaInpainting`
- `LayerUtility: ImageBlend`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `MirroredImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeForInpaint`
- `VAELoader`
- `WD14Tagger|pysssss`
- `YC_LG_Redux`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 7 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.4 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.8 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
