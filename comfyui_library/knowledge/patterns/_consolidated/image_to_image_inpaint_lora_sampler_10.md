---
name: image_to_image_inpaint_lora_sampler_10
type: Image To Image
frequency: 3
level: moderate
coverage: 0.713667
common_nodes: [AddMask, Bjornulf_ShowInt, BlockifyMask, CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CR Aspect Ratio, CR Prompt Text, ConditioningZeroOut, CropByBBoxes, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GrowMaskWithBlur, INPAINT_MaskBoundingBox, ImageResizeKJv2, InvertMask, JoinStringMulti, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask To Image (mtb), MaskToImage, ModelSamplingAuraFlow, PreviewAny, PreviewImage, PrimitiveBoundingBox, PrimitiveStringMultiline, Qwen3VLProcessor, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, RandomNoise, ReferenceLatent, Sa2VANodeTpl, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/抱枕与挂布处理_2100949927345086466.json, 图片生成/图生图/抱枕与挂布处理_2101208834231590914.json, 图片生成/图生图/抱枕与挂布处理_2101664155941036034.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/抱枕与挂布处理_2100949927345086466.json、图片生成/图生图/抱枕与挂布处理_2101208834231590914.json、图片生成/图生图/抱枕与挂布处理_2101664155941036034.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `AddMask`
- `Bjornulf_ShowInt`
- `BlockifyMask`
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Aspect Ratio`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `CropByBBoxes`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `INPAINT_MaskBoundingBox`
- `ImageResizeKJv2`
- `InvertMask`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask To Image (mtb)`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveBoundingBox`
- `PrimitiveStringMultiline`
- `Qwen3VLProcessor`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `RandomNoise`
- `ReferenceLatent`
- `Sa2VANodeTpl`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowFloat` —— 2/3 个有
- `Boolean To Int [Dream]` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `Image Blank` —— 2/3 个有
- `Int` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `easy convertAnything` —— 2/3 个有
- `math_calculate` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Image Rembg (Remove Background)` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PromptEnhancerPreset` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `TTP_Expand_And_Mask` —— 1/3 个有
- `XB_llamaPromptEnhancer` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
