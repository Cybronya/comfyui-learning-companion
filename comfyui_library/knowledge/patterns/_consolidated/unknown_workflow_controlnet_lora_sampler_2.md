---
name: unknown_workflow_controlnet_lora_sampler_2
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.833125
common_nodes: [CLIPLoader, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, Int, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskFastGrow, MaskFillHoles, MaskToImage, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Edit2509模特生成-涂抹版_2015215444591906818.json, 图片生成/图生图/Qwen 2511 场景人物替换万物迁移手动遮罩_2007382936089272321.json, 图片生成/图生图/【CQ808】人物迁移终极版OLDX_2033445923782660097.json, 图片生成/图生图/人物和道具替换_2054470195934187522.json, 图片生成/图生图/替换人物终极版OLDX王改革_2001081264344006657.json, 图片生成/图生图/模特生成-涂抹模特版_2021108943363252225.json, 图片生成/图生图/自用换图_2001852012134297602.json, 视频生成/图生视频/人物替换_1994370592411426817.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Edit2509模特生成-涂抹版_2015215444591906818.json、图片生成/图生图/Qwen 2511 场景人物替换万物迁移手动遮罩_2007382936089272321.json、图片生成/图生图/【CQ808】人物迁移终极版OLDX_2033445923782660097.json、图片生成/图生图/人物和道具替换_2054470195934187522.json、图片生成/图生图/替换人物终极版OLDX王改革_2001081264344006657.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `Int`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFastGrow`
- `MaskFillHoles`
- `MaskToImage`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 7/8 个有
- `ImageCompositeMasked` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `LayerUtility: ImageReel` —— 6/8 个有
- `LayerUtility: ImageReelComposit` —— 6/8 个有
- `GetNode` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `GrowMaskWithBlur` —— 2/8 个有
- `LayerUtility: CropByMask V2` —— 2/8 个有
- `LayerUtility: ImageScaleRestore V2` —— 2/8 个有
- `LayerUtility: RestoreCropBox` —— 2/8 个有
- `SAM2Segment` —— 2/8 个有
- `easy boolean` —— 2/8 个有
- `easy ifElse` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `GrowMask` —— 1/8 个有
- `ImageCompositeMaskedOneByOne` —— 1/8 个有
- `MaskPreview+` —— 1/8 个有
- `Vignette` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 8 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| ControlNet 权重 | 2 | 2 - 2 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 2，观测区间 2 - 2，8 个样本，取值集中（一致性 100%）
