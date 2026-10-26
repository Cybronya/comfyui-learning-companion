---
name: unknown_workflow_upscale_latent_upscale_lora_66
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6935
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GH_MaskCropV2, GetNode, GuHai_IDPhotoCrop, GulfSeaImageMergeMask, Image Comparer (rgthree), ImageCrop+, ImageScaleBy, ImpactSEGSToMaskBatch, KSamplerSelect, LatentUpscaleBy, LayerMask: SegformerB2ClothesUltra, LayerUtility: BooleanOperatorV2, LayerUtility: ColorImage, LoadImage, LoraLoaderModelOnly, MaskToSEGS_for_AnimateDiff, PreviewImage, RandomNoise, ReferenceLatent, SZ_KleinTiledKSampler, SamplerCustomAdvanced, SaveImageJPG_GH, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, Simple String, Text Concatenate, TextInput_, ToBinaryMask, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, VHS_GetMaskCount, easy humanSegmentation, easy ifElse, easy imageColorMatch, easy seed, 图像缩放V2_孤海, 图像缩放范围孤海, 孤海Seg次序过滤, 孤海注释, 忽略多组孤海, 结婚登记照服装_孤海]
problems: []
missing: []
members: [图片生成/图生图/结婚登记照一键合成+精修+换装_2111995599418650625.json, 图片生成/图生图/结婚登记照一键合成+精修+换装_2113461247940317185.json, 图片生成/图生图/老孙AI - 结婚登记照一键合成+精修+换装_2087367504355225602.json, 图片生成/图生图/老孙AI- 结婚登记照一键合成+精修+换装_2085563777428312065.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_66

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/结婚登记照一键合成+精修+换装_2111995599418650625.json、图片生成/图生图/结婚登记照一键合成+精修+换装_2113461247940317185.json、图片生成/图生图/老孙AI - 结婚登记照一键合成+精修+换装_2087367504355225602.json、图片生成/图生图/老孙AI- 结婚登记照一键合成+精修+换装_2085563777428312065.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GH_MaskCropV2`
- `GetNode`
- `GuHai_IDPhotoCrop`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `ImageCrop+`
- `ImageScaleBy`
- `ImpactSEGSToMaskBatch`
- `KSamplerSelect`
- `LatentUpscaleBy`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: ColorImage`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS_for_AnimateDiff`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SZ_KleinTiledKSampler`
- `SamplerCustomAdvanced`
- `SaveImageJPG_GH`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `Simple String`
- `Text Concatenate`
- `TextInput_`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_GetMaskCount`
- `easy humanSegmentation`
- `easy ifElse`
- `easy imageColorMatch`
- `easy seed`
- `图像缩放V2_孤海`
- `图像缩放范围孤海`
- `孤海Seg次序过滤`
- `孤海注释`
- `忽略多组孤海`
- `结婚登记照服装_孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
