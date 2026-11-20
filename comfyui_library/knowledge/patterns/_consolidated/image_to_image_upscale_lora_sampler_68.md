---
name: image_to_image_upscale_lora_sampler_68
type: Image To Image
frequency: 3
level: strong
coverage: 0.92
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ConstrainImage|pysssss, DisableNoise, DualCLIPLoader, Fast Groups Bypasser (rgthree), FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, Image Comparer (rgthree), ImageUpscaleWithModel, InFluxModelSamplingPred, Joy_caption_two, Joy_caption_two_load, KSampler, LayerColor: Exposure, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ColorPicker, LayerUtility: ImageCombineAlpha, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoader, OutFluxModelSamplingPred, PreviewImage, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/电商产品精修丨_1902158654961770497.json, 图片生成/图生图/电商产品精修丨一键生图系列_1909487858250620930.json, 图片生成/图生图/电商产品精修物品精修_1929119337175531522.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商产品精修丨_1902158654961770497.json、图片生成/图生图/电商产品精修丨一键生图系列_1909487858250620930.json、图片生成/图生图/电商产品精修物品精修_1929119337175531522.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `DisableNoise`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `InFluxModelSamplingPred`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerColor: Exposure`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoader`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | exponential | - | 3 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 exponential，3 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
