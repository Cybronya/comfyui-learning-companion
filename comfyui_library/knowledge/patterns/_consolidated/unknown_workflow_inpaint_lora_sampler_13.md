---
name: unknown_workflow_inpaint_lora_sampler_13
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.600818
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSize+, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageComposite+, ImageConcanate, ImageCrop, ImageResize+, ImageToMask, ImpactDecomposeSEGS, ImpactFrom_SEG_ELT, ImpactFrom_SEG_ELT_crop_region, ImpactSEGSOrderedFilter, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleRestore, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, RH_Captioner, SEGSPreview, SaveImage, SetNode, SimpleMath+, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/人物头像替换-图片换头v1.2_2016323601980461057.json, 图片生成/图生图/全能换脸（河南ai之神）_1959228923110436866.json, 图片生成/图生图/图片换头v1.1_2015961920523735041.json, 图片生成/图生图/手动万物迁移_1903762239432859650.json, 图片生成/图生图/精致换头V2版本_1914344981773938689.json, 图片生成/图生图/蜜蜂图片换头v1.1_2014226237119533058.json, 图片生成/图生图/蜜蜂图片换头v1.2_2012484878163513346.json, 图片生成/图生图/超真实换脸人物换头_2054200187630964738.json, 平台全量/HT头_1926593056223469569.json, 平台全量/一键图片换头术快速换头其他部位不改变_1977961132893896705.json, 平台全量/换脸_2042218967099514882.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/人物头像替换-图片换头v1.2_2016323601980461057.json、图片生成/图生图/全能换脸（河南ai之神）_1959228923110436866.json、图片生成/图生图/图片换头v1.1_2015961920523735041.json、图片生成/图生图/手动万物迁移_1903762239432859650.json、图片生成/图生图/精致换头V2版本_1914344981773938689.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 11 个 workflow 都包含：
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
- `FloatConstant` —— 10/11 个有
- `GrowMask` —— 10/11 个有
- `ImageTransformPaddingRelative` —— 10/11 个有
- `InvertMask` —— 10/11 个有
- `LG_ImageSender` —— 10/11 个有
- `LayerUtility: ColorImage` —— 10/11 个有
- `SubtractMask` —— 10/11 个有
- `easy ifElse` —— 10/11 个有
- `LayerMask: PersonMaskUltra V2` —— 9/11 个有
- `RHHiddenNodes` —— 9/11 个有
- `StringConstant` —— 9/11 个有
- `Text Concatenate (JPS)` —— 9/11 个有
- `TextInput_` —— 9/11 个有
- `easy int` —— 9/11 个有
- `easy showAnything` —— 9/11 个有
- `Note Plus (mtb)` —— 3/11 个有
- `CLIPVisionLoader` —— 2/11 个有
- `ReduxAdvanced` —— 2/11 个有
- `StyleModelLoader` —— 2/11 个有
- `Bookmark (rgthree)` —— 1/11 个有
- `ControlNetApplyAdvanced` —— 1/11 个有
- `ControlNetLoader` —— 1/11 个有
- `DepthAnything_V2` —— 1/11 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/11 个有
- `ICLightApplyMaskGrey` —— 1/11 个有
- `Image To Mask` —— 1/11 个有
- `ImageRemoveAlpha+` —— 1/11 个有
- `InvertImageNode` —— 1/11 个有
- `LayerMask: CreateGradientMask` —— 1/11 个有
- `LayerMask: MaskPreview` —— 1/11 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/11 个有
- `Mask Fill Holes` —— 1/11 个有
- `easy isMaskEmpty` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.95 - 1 | 11 | 97% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.95 - 1，11 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.95，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
