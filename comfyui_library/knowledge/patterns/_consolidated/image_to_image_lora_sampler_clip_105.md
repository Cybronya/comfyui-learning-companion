---
name: image_to_image_lora_sampler_clip_105
type: Image To Image
frequency: 3
level: strong
coverage: 0.840667
common_nodes: [Anything Everywhere3, CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImpactSwitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, RH_Translator, ReferenceLatent, SaveImage, Text Find and Replace, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/光影-梦幻光影-工作流_1955142308644601858.json, 图片生成/图生图/光影-梦幻光影-工作流_1965767182925893633.json, 图片生成/图生图/梦幻光影-多彩打光-图生图_2031907252721946625.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/光影-梦幻光影-工作流_1955142308644601858.json、图片生成/图生图/光影-梦幻光影-工作流_1965767182925893633.json、图片生成/图生图/梦幻光影-多彩打光-图生图_2031907252721946625.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `Text Find and Replace`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
