---
name: unknown_workflow_lora_sampler_unet_234
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.823333
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换装新_2048517500643577857.json, 图片生成/图生图/服装批量改颜色（FK2一致性）_2073328215275425794.json, 图片生成/图生图/汽车轮轮胎轮毂整体替换方案v2_2056270200219201538.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_234

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/换装新_2048517500643577857.json、图片生成/图生图/服装批量改颜色（FK2一致性）_2073328215275425794.json、图片生成/图生图/汽车轮轮胎轮毂整体替换方案v2_2056270200219201538.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AdaptiveLongestEdge_EditUtils` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `InpaintCropImproved` —— 1/3 个有
- `InpaintStitchImproved` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerColor: ColorAdapter` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
