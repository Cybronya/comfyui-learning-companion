---
name: text_to_image_inpaint_lora_sampler_4
type: Text To Image
frequency: 3
level: strong
coverage: 0.781
common_nodes: [AddMask, Bjornulf_ShowInt, BlockifyMask, CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CR Aspect Ratio, CR Prompt Text, ConditioningZeroOut, CropByBBoxes, DrawMaskOnImage, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GrowMaskWithBlur, INPAINT_MaskBoundingBox, ImageResizeKJv2, InvertMask, JjkText, JoinStringMulti, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask To Image (mtb), MaskToImage, ModelSamplingAuraFlow, PreviewAny, PreviewImage, PrimitiveBoundingBox, PrimitiveStringMultiline, Qwen3VLProcessor, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, RandomNoise, ReferenceLatent, Sa2VANodeTpl, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/抱枕与挂布处理优化版｜图生图电商家居素材一键出图_2101866062852747265.json, 图片生成/图生图/抱枕与挂布处理工作流｜图生图电商素材批量处理更省心_2101854700705509377.json, 图片生成/图生图/抱枕挂布素材处理｜图生图抠图去水印实用工具_2101134943521955842.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/抱枕与挂布处理优化版｜图生图电商家居素材一键出图_2101866062852747265.json、图片生成/图生图/抱枕与挂布处理工作流｜图生图电商素材批量处理更省心_2101854700705509377.json、图片生成/图生图/抱枕挂布素材处理｜图生图抠图去水印实用工具_2101134943521955842.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

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
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `INPAINT_MaskBoundingBox`
- `ImageResizeKJv2`
- `InvertMask`
- `JjkText`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

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
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
