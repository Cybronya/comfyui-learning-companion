---
name: unknown_workflow_inpaint_lora_sampler_33
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.877
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImageCrop+, InpaintModelConditioning, KSampler, LayerMask: MaskPreview, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/最强迁移PLUS版小件物品也能迁移FLUX的Redux+ACE_2097867409247002625.json, 图片生成/图生图/最强迁移PLUS版小件物品也能迁移FLUX的Redux+ACE_2099406881738551298.json, 平台全量/flux Fill OneReward 万物迁移增强版（附引导式指引）_1988527902402723842.json, 平台全量/局部替换(极速版+一致性增强)_2052635416070762497.json, 平台全量/最强迁移PLUS版（小件物品也能迁移）FLUX的Redux+ACE_1906720377211604993.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/最强迁移PLUS版小件物品也能迁移FLUX的Redux+ACE_2097867409247002625.json、图片生成/图生图/最强迁移PLUS版小件物品也能迁移FLUX的Redux+ACE_2099406881738551298.json、平台全量/flux Fill OneReward 万物迁移增强版（附引导式指引）_1988527902402723842.json、平台全量/局部替换(极速版+一致性增强)_2052635416070762497.json、平台全量/最强迁移PLUS版（小件物品也能迁移）FLUX的Redux+ACE_1906720377211604993.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageCrop+`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `InpaintCrop` —— 4/5 个有
- `InpaintStitch` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `AutoDownloadBiRefNetModel` —— 3/5 个有
- `RH_Captioner` —— 3/5 个有
- `RembgByBiRefNet` —— 3/5 个有
- `BiRefNet_ModelLoader_Zho` —— 1/5 个有
- `BiRefNet_Zho` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `InpaintCropImproved` —— 1/5 个有
- `InpaintStitchImproved` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有
- `llama_cpp_parameters` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 25 - 28 | 5 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 25 - 28，5 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
