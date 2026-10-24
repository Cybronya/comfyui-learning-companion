---
name: unknown_workflow_inpaint_lora_sampler_11
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.602125
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSize+, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageComposite+, ImageConcanate, ImageCrop, ImageResize+, ImageToMask, ImpactDecomposeSEGS, ImpactFrom_SEG_ELT, ImpactFrom_SEG_ELT_crop_region, ImpactSEGSOrderedFilter, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleRestore, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, RH_Captioner, SEGSPreview, SaveImage, SetNode, SimpleMath+, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/人物头像替换-图片换头v1.2_2016323601980461057.json, 图片生成/图生图/全能换脸（河南ai之神）_1959228923110436866.json, 图片生成/图生图/图片换头v1.1_2015961920523735041.json, 图片生成/图生图/手动万物迁移_1903762239432859650.json, 图片生成/图生图/精致换头V2版本_1914344981773938689.json, 图片生成/图生图/蜜蜂图片换头v1.1_2014226237119533058.json, 图片生成/图生图/蜜蜂图片换头v1.2_2012484878163513346.json, 图片生成/图生图/超真实换脸人物换头_2054200187630964738.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人物头像替换-图片换头v1.2_2016323601980461057.json、图片生成/图生图/全能换脸（河南ai之神）_1959228923110436866.json、图片生成/图生图/图片换头v1.1_2015961920523735041.json、图片生成/图生图/手动万物迁移_1903762239432859650.json、图片生成/图生图/精致换头V2版本_1914344981773938689.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageComposite+`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageToMask`
- `ImpactDecomposeSEGS`
- `ImpactFrom_SEG_ELT`
- `ImpactFrom_SEG_ELT_crop_region`
- `ImpactSEGSOrderedFilter`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleRestore`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `PreviewImage`
- `RH_Captioner`
- `SEGSPreview`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 7/8 个有
- `GrowMask` —— 7/8 个有
- `ImageTransformPaddingRelative` —— 7/8 个有
- `InvertMask` —— 7/8 个有
- `LG_ImageSender` —— 7/8 个有
- `LayerUtility: ColorImage` —— 7/8 个有
- `SubtractMask` —— 7/8 个有
- `easy ifElse` —— 7/8 个有
- `LayerMask: PersonMaskUltra V2` —— 6/8 个有
- `RHHiddenNodes` —— 6/8 个有
- `StringConstant` —— 6/8 个有
- `Text Concatenate (JPS)` —— 6/8 个有
- `TextInput_` —— 6/8 个有
- `easy int` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `CLIPVisionLoader` —— 2/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `ReduxAdvanced` —— 2/8 个有
- `StyleModelLoader` —— 2/8 个有
- `ControlNetApplyAdvanced` —— 1/8 个有
- `ControlNetLoader` —— 1/8 个有
- `DepthAnything_V2` —— 1/8 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/8 个有
- `ICLightApplyMaskGrey` —— 1/8 个有
- `Image To Mask` —— 1/8 个有
- `ImageRemoveAlpha+` —— 1/8 个有
- `InvertImageNode` —— 1/8 个有
- `LayerMask: CreateGradientMask` —— 1/8 个有
- `LayerMask: MaskPreview` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/8 个有
- `Mask Fill Holes` —— 1/8 个有
- `easy isMaskEmpty` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 8 | 100% |
| Prompt 约束强度(CFG) | 0.95 | 0.95 - 1 | 8 | 98% |
| 采样算法 | dpmpp_2m_sde | - | 8 | 62% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.95，观测区间 0.95 - 1，8 个样本，取值集中（一致性 98%）
- 采样算法 最常用 dpmpp_2m_sde，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.95，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
