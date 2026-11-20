---
name: image_to_image_lora_sampler_unet_142
type: Image To Image
frequency: 6
level: strong
coverage: 0.669
common_nodes: [Anything Everywhere3, CFGNorm, CLIPLoader, CM_IntToBool, CM_NumberToInt, CR Integer To String, CR Text, FluxKontextMultiReferenceLatentMethod, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageComposite+, Int, IsMaskEmpty, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SetLatentNoiseMask, SetNode, ShowText|pysssss, Switch image [Crystools], Switch latent [Crystools], TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/局部重绘服装迁移 Qwen-Edit  万能迁移无偏移  局部重绘 极速版 真实自然无痕_2017126574084067330.json, 平台全量/服装迁移无偏移局部重绘Qwen-Edit-2511_2016110993646030850.json, 平台全量/精准局部重绘 万物迁移 精准编辑无偏移 局部重绘Qwen-Edit-2511细节保真_2017777567150907394.json, 平台全量/精准编辑无偏移 _ 局部重绘Qwen-Edit-2511_2016106682320949250.json, 平台全量/精准重绘换装 零偏移局部重绘+单_双图编辑+精准重绘编辑无偏移++局部重绘Qwen-Edit-251_2069290779671093249.json, 平台全量/零偏移局部重绘 单_双图编辑 精准重绘编辑无偏移  局部重绘Qwen-Edit-2511_2066350042012803073.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_142

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/局部重绘服装迁移 Qwen-Edit  万能迁移无偏移  局部重绘 极速版 真实自然无痕_2017126574084067330.json、平台全量/服装迁移无偏移局部重绘Qwen-Edit-2511_2016110993646030850.json、平台全量/精准局部重绘 万物迁移 精准编辑无偏移 局部重绘Qwen-Edit-2511细节保真_2017777567150907394.json、平台全量/精准编辑无偏移 _ 局部重绘Qwen-Edit-2511_2016106682320949250.json、平台全量/精准重绘换装 零偏移局部重绘+单_双图编辑+精准重绘编辑无偏移++局部重绘Qwen-Edit-251_2069290779671093249.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `CM_IntToBool`
- `CM_NumberToInt`
- `CR Integer To String`
- `CR Text`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `Int`
- `IsMaskEmpty`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `ShowText|pysssss`
- `Switch image [Crystools]`
- `Switch latent [Crystools]`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
