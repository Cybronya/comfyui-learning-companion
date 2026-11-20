---
name: unknown_workflow_inpaint_lora_sampler_39
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.488
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, CM_IntToBool, CR Text, CR Text Concatenate, DWPreprocessor, Display Any (rgthree), Fast Groups Bypasser (rgthree), GetNode, GrowMask, INPAINT_MaskedBlur, Image Comparer (rgthree), ImageToMask, Int, KSampler, LayerMask: MaskPreview, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskColorize, MaskFillHoles, ModelSamplingAuraFlow, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PainterQwenImageEditPlus, PlaySound|pysssss, PreviewImage, RMBG, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageSize, easy imageSizeByLongerSide, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2511 角色替换  超强一致性_2020319634725015554.json, 图片生成/图生图/QwenEdit2511 角色替换 、保留前景物品_2027637931527118850.json, 图片生成/图生图/QwenEdit2511 角色替换 保持手持、前景物品  超强一致性_2011974227439656962.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QwenEdit2511 角色替换  超强一致性_2020319634725015554.json、图片生成/图生图/QwenEdit2511 角色替换 、保留前景物品_2027637931527118850.json、图片生成/图生图/QwenEdit2511 角色替换 保持手持、前景物品  超强一致性_2011974227439656962.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CM_IntToBool`
- `CR Text`
- `CR Text Concatenate`
- `DWPreprocessor`
- `Display Any (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedBlur`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `Int`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskColorize`
- `MaskFillHoles`
- `ModelSamplingAuraFlow`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PainterQwenImageEditPlus`
- `PlaySound|pysssss`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy imageSizeByLongerSide`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `CR Overlay Transparent Image` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `ImageAddMulti` —— 2/3 个有
- `LayerUtility: ColorImage` —— 2/3 个有
- `LayerUtility: RestoreCropBox` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `Switch` —— 2/3 个有
- `ThresholdMask` —— 2/3 个有
- `To Device (mtb)` —— 2/3 个有
- `VHS_SelectMasks` —— 2/3 个有
- `VRAM_Debug` —— 2/3 个有
- `ZML_MaskCropNode` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `easy sam3ImageSegmentation` —— 2/3 个有
- `easy sam3ModelLoader` —— 2/3 个有
- `type_Mask_Batch2List` —— 2/3 个有
- `FeatherMask` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
