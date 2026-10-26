---
name: image_to_image_sampler_unet_vae_38
type: Image To Image
frequency: 4
level: strong
coverage: 0.818
common_nodes: [CLIPLoader, CR SDXL Aspect Ratio, CR Text, ConditioningZeroOut, CropWithPadInfo, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageResizeKJv2, ImageScaleBy, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, RHHiddenNodes, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 人物 穿着 服装提取 与 模特试穿_2069713515883089921.json, 图片生成/图生图/Qwen Edit 人物 穿着 服装提取 与 模特试穿_2069717854013976578.json, 图片生成/图生图/Qwen Edit 人物穿着服装提取与模特试穿工作流（官方与小志节点）_2067273546103091202.json, 图片生成/图生图/人物穿着服装提取与模特试穿工作流自用_2069933697402494977.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 人物 穿着 服装提取 与 模特试穿_2069713515883089921.json、图片生成/图生图/Qwen Edit 人物 穿着 服装提取 与 模特试穿_2069717854013976578.json、图片生成/图生图/Qwen Edit 人物穿着服装提取与模特试穿工作流（官方与小志节点）_2067273546103091202.json、图片生成/图生图/人物穿着服装提取与模特试穿工作流自用_2069933697402494977.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（16/4 个样本）：Steps较低可能导致细节不足
