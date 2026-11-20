---
name: unknown_workflow_lora_sampler_unet_184
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8334
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), ImageCompositeMasked, ImageScale, ImageScaleBy, ImageToMask, KSampler, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoaderModelOnly, MaskPreview, ModelSamplingAuraFlow, PreviewBridge, SaveImage, Seed (rgthree), TextEncodeQwenImageEditPlusAdvance_lrzjason, UnetLoaderGGUF, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/qwen-edit-拼图融合-换脸及换头-人物一致性完美_1988806823639658498.json, 平台全量/qwen-edit-鞋子迁移-鞋子试穿-产品一致性完美_1987710561871966209.json, 平台全量/qwen-image-edit-帽子迁移-帽子试戴-产品一致性完美_1988074104886595585.json, 平台全量/qwen-image-edit-珠宝首饰迁移-产品一致性完美-融合度完美-小批量处理_1988038397937823746.json, 平台全量/qwen-image-edit-面部迁移-换脸或换头-v2_1994740633816403969.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_184

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/qwen-edit-拼图融合-换脸及换头-人物一致性完美_1988806823639658498.json、平台全量/qwen-edit-鞋子迁移-鞋子试穿-产品一致性完美_1987710561871966209.json、平台全量/qwen-image-edit-帽子迁移-帽子试戴-产品一致性完美_1988074104886595585.json、平台全量/qwen-image-edit-珠宝首饰迁移-产品一致性完美-融合度完美-小批量处理_1988038397937823746.json、平台全量/qwen-image-edit-面部迁移-换脸或换头-v2_1994740633816403969.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `ModelSamplingAuraFlow`
- `PreviewBridge`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 4/5 个有
- `LayerColor: BrightnessContrastV2` —— 4/5 个有
- `LayerColor: ColorAdapter` —— 4/5 个有
- `LayerUtility: ImageBlend` —— 4/5 个有
- `LayerUtility: LayerImageTransform` —— 4/5 个有
- `easy imageSizeBySide` —— 4/5 个有
- `easy positive` —— 4/5 个有
- `AILab_MaskCombiner` —— 3/5 个有
- `BasicScheduler` —— 3/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `DetailDaemonSamplerNode` —— 3/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `ImageUpscaleWithModel` —— 3/5 个有
- `InpaintModelConditioning` —— 3/5 个有
- `KSamplerSelect` —— 3/5 个有
- `LayerMask: LoadSegmentAnythingModels` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra V3` —— 3/5 个有
- `LayerUtility: ColorImage` —— 3/5 个有
- `SamplerCustom` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `UpscaleModelLoader` —— 3/5 个有
- `MaskToImage` —— 2/5 个有
- `AILab_MaskEnhancer` —— 1/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `BlockifyMask` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImpactMakeAnyList` —— 1/5 个有
- `LayerMask: PersonMaskUltra V2` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `SplitSigmas` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `easy isMaskEmpty` —— 1/5 个有
- `easy promptReplace` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
