---
name: unknown_workflow_controlnet_upscale_latent_upscale_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.696333
common_nodes: [Any Switch (rgthree), Anything Everywhere, CFGNorm, CLIPLoader, CR Image Input Switch, CR Image Input Switch (4 way), CR Prompt Text, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CropWithPadInfo, DrawMaskOnImage, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetImageSize, GetNode, GrowMaskWithBlur, INTConstant, Image Comparer (rgthree), ImageCompositeMasked, ImageScaleBy, ImageStitch, InvertMask, KSampler, LatentUpscale, LayerUtility: ColorImage V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: SaveImagePlus, LoadImage, LoadRembgByBiRefNetModel, LoraLoaderModelOnly, MaskPreview+, MemoryCleaner, ModelSamplingAuraFlow, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, ReferenceLatent, RembgByBiRefNetAdvanced, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, SolidMask, Switch mask [Crystools], TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, YOLOModelLoader, ZML_SelectTextV3, ZML_SwitchOutput, easy cleanGpuUsed, easy ifElse, easy imageSwitch, easy isMaskEmpty, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, mxSlider, mxSlider2D]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图像编辑_QwenEdit2511_&_Flux2_Klein_9B_2074049643352256513.json, 图片生成/图生图/全能图像编辑_QwenEdit2511_&_Flux2_Klein_9B_2074058856480722945.json, 图片生成/文生图/全能图像编辑_QwenEdit2511 & Flux2 Klein 9B_2044630852038037506.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全能图像编辑_QwenEdit2511_&_Flux2_Klein_9B_2074049643352256513.json、图片生成/图生图/全能图像编辑_QwenEdit2511_&_Flux2_Klein_9B_2074058856480722945.json、图片生成/文生图/全能图像编辑_QwenEdit2511 & Flux2 Klein 9B_2044630852038037506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CR Image Input Switch`
- `CR Image Input Switch (4 way)`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropWithPadInfo`
- `DrawMaskOnImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImageSize`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageScaleBy`
- `ImageStitch`
- `InvertMask`
- `KSampler`
- `LatentUpscale`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: SaveImagePlus`
- `LoadImage`
- `LoadRembgByBiRefNetModel`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MemoryCleaner`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `ReferenceLatent`
- `RembgByBiRefNetAdvanced`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `SolidMask`
- `Switch mask [Crystools]`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YOLOModelLoader`
- `ZML_SelectTextV3`
- `ZML_SwitchOutput`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageSwitch`
- `easy isMaskEmpty`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `mxSlider`
- `mxSlider2D`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 2 | 2 - 2 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
