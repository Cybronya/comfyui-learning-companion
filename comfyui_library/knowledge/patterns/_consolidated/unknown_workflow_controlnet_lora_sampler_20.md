---
name: unknown_workflow_controlnet_lora_sampler_20
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.603333
common_nodes: [AIO_Preprocessor, CLIPLoader, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Fast Groups Bypasser (rgthree), ImageCompositeMasked, ImageScaleToTotalPixels, Int, KSampler, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskFastGrow, MaskFillHoles, MaskToImage, PreviewImage, QwenEditConfigPreparer, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/⭐️⭐️⭐️⭐️⭐️一键换万物_2008472909521620993.json, 图片生成/图生图/模特换装_2032014065257680897.json, 图片生成/图生图/目前最强万物迁移工作流AIO-2511 林耀2.6_2019689052630421505.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/⭐️⭐️⭐️⭐️⭐️一键换万物_2008472909521620993.json、图片生成/图生图/模特换装_2032014065257680897.json、图片生成/图生图/目前最强万物迁移工作流AIO-2511 林耀2.6_2019689052630421505.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFastGrow`
- `MaskFillHoles`
- `MaskToImage`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 2/3 个有
- `LayerMask: BiRefNetUltraV2` —— 2/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/3 个有
- `QwenEditAdaptiveLongestEdge` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadSAM3Model` —— 1/3 个有
- `MirroredImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SAM3Segmentation` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | 2 - 2 | 3 | 100% |
| 采样步数 | 10 | 4 - 10 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
