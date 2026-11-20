---
name: unknown_workflow_controlnet_lora_sampler_4
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5531
common_nodes: [AIO_Preprocessor, CLIPLoader, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Fast Groups Bypasser (rgthree), ImageCompositeMasked, ImageScaleToTotalPixels, Int, KSampler, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskFastGrow, MaskFillHoles, MaskToImage, PreviewImage, QwenEditConfigPreparer, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/⭐️⭐️⭐️⭐️⭐️一键换万物_2008472909521620993.json, 图片生成/图生图/模特换装_2032014065257680897.json, 图片生成/图生图/目前最强万物迁移工作流AIO-2511 林耀2.6_2019689052630421505.json, 平台全量/QwenimageEdit2509换万物手动版（精准版）_2002482375235911681.json, 平台全量/一键换万物_2008150165995130882.json, 平台全量/一键换万物_2008157881127936002.json, 平台全量/一键换万物手动版（精准版）One-Click Replace Everything (Manual Version_ Precision)_1991548793229418498.json, 平台全量/一键换万物自动版（快捷）One-Click Replace Everything（Automatic Version：Shortcut）_1991556560270925826.json, 平台全量/一键换万物自动版（快捷）_2056017989744504833.json, 平台全量/最强一键换万物替换_2033029075010326530.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/⭐️⭐️⭐️⭐️⭐️一键换万物_2008472909521620993.json、图片生成/图生图/模特换装_2032014065257680897.json、图片生成/图生图/目前最强万物迁移工作流AIO-2511 林耀2.6_2019689052630421505.json、平台全量/QwenimageEdit2509换万物手动版（精准版）_2002482375235911681.json、平台全量/一键换万物_2008150165995130882.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LayerMask: BiRefNetUltraV2` —— 9/10 个有
- `LayerMask: LoadBiRefNetModelV2` —— 9/10 个有
- `ConcatTextOfUtils` —— 8/10 个有
- `QwenEditAdaptiveLongestEdge` —— 8/10 个有
- `UNETLoader` —— 8/10 个有
- `VAELoader` —— 8/10 个有
- `LayerMask: MaskPreview` —— 5/10 个有
- `easy clearCacheAll` —— 5/10 个有
- `LayerMask: PersonMaskUltra V2` —— 4/10 个有
- `SeedVR2LoadDiTModel` —— 3/10 个有
- `SeedVR2LoadVAEModel` —— 3/10 个有
- `SeedVR2VideoUpscaler` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `CheckpointLoaderSimple` —— 2/10 个有
- `GetNode` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `LoadSAM3Model` —— 1/10 个有
- `MirroredImage` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `SAM3Segmentation` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `TextInput_` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | 2 - 2 | 10 | 100% |
| 采样步数 | 10 | 4 - 10 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | beta57 | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 2 - 2，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 4 - 10，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 beta57，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
