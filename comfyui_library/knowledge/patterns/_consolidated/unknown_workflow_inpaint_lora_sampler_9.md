---
name: unknown_workflow_inpaint_lora_sampler_9
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.59275
common_nodes: [CLIPTextEncode, ColorCorrect, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageComposite+, ImpactInt, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: BooleanOperatorV2, LayerUtility: ColorImage, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, PreviewImage, RH_Translator, SaveImage, SetNode, Simple String, StringLength, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy boolean, easy ifElse, 孤海-图像添加水印, 孤海图像缩放按像素, 孤海外补画板按方向]
problems: []
missing: []
members: [图片生成/图生图/Fill OneReward 移除、扩图、重绘一体化4K直出_2070100010657734657.json, 图片生成/图生图/Fill OneReward 移除、扩图、重绘一体化4K直出_2084332499492237313.json, 图片生成/图生图/Fill OneReward 移除、扩图、重绘一体化（记得画遮罩）4K直出_2046766124548755458.json, 图片生成/图生图/Fill+OneReward+移除、扩图、重绘一体化4K直出_1999797223351255041.json, 图片生成/图生图/Fill+OneReward+移除、扩图、重绘一体化4K直出_2026929107174428673.json, 图片生成/图生图/图片 移除  扩图 重绘 一体化 4K直出_1993127030715858946.json, 图片生成/图生图/移除、扩图、重绘一体化4K直出_1982729090350366722.json, 图片生成/图生图/老孙AI 移除、扩图、重绘一体4K_2085915793509928961.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Fill OneReward 移除、扩图、重绘一体化4K直出_2070100010657734657.json、图片生成/图生图/Fill OneReward 移除、扩图、重绘一体化4K直出_2084332499492237313.json、图片生成/图生图/Fill OneReward 移除、扩图、重绘一体化（记得画遮罩）4K直出_2046766124548755458.json、图片生成/图生图/Fill+OneReward+移除、扩图、重绘一体化4K直出_1999797223351255041.json、图片生成/图生图/Fill+OneReward+移除、扩图、重绘一体化4K直出_2026929107174428673.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorCorrect`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImpactInt`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: ColorImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `SetNode`
- `Simple String`
- `StringLength`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy ifElse`
- `孤海-图像添加水印`
- `孤海图像缩放按像素`
- `孤海外补画板按方向`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 6/8 个有
- `LayerMask: MaskPreview` —— 1/8 个有
- `Preview from image [Crystools]` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
