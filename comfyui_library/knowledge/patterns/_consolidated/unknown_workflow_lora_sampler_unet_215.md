---
name: unknown_workflow_lora_sampler_unet_215
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88475
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConcatTextOfUtils, ConditioningZeroOut, DWPreprocessor, Get resolution [Crystools], Image Comparer (rgthree), ImageCompositeMasked, ImagePadForOutpaint, ImpactCompare, Int, JWStringConcat, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, SaveImage, SimpleMath+, SimpleMathCondition+, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_edit_2511人物置换_姿势迁移_光影无缝融合_2079035212511666178.json, 平台全量/Qwen-2511-角色替换（动作一致性）工作流_2012847368357552129.json, 平台全量/Qwen_edit_2509+人物置换工作流(动作迁移+++光影无缝融合)简化版_2074026241958699009.json, 平台全量/Qwen_edit_2511+人物替换工作流(保持场景+++人物替换)简化版_2074022575965032450.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_215

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen_edit_2511人物置换_姿势迁移_光影无缝融合_2079035212511666178.json、平台全量/Qwen-2511-角色替换（动作一致性）工作流_2012847368357552129.json、平台全量/Qwen_edit_2509+人物置换工作流(动作迁移+++光影无缝融合)简化版_2074026241958699009.json、平台全量/Qwen_edit_2511+人物替换工作流(保持场景+++人物替换)简化版_2074022575965032450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConcatTextOfUtils`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `Get resolution [Crystools]`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImagePadForOutpaint`
- `ImpactCompare`
- `Int`
- `JWStringConcat`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SimpleMath+`
- `SimpleMathCondition+`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `MaskFastGrow` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `SDPoseOODLoader` —— 2/4 个有
- `SDPoseOODProcessor` —— 2/4 个有
- `easy imageSwitch` —— 2/4 个有
- `Fast Bypasser (rgthree)` —— 1/4 个有
- `LayerColor: BrightnessContrastV2` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy imageScaleDownToSize` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
