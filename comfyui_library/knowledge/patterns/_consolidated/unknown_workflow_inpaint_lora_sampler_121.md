---
name: unknown_workflow_inpaint_lora_sampler_121
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9395
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, GetImageSize+, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerMask: PersonMaskUltra, LayerStyle: ColorOverlay V2, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, SaveImage, SimpleMath+, StyleModelLoader, Switch any [Crystools], UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/一键换头换脸（FILL+ACE方案）_1948622803544211457.json, 平台全量/王炸！FLUX+ACE++换头_1930479706833895425.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键换头换脸（FILL+ACE方案）_1948622803544211457.json、平台全量/王炸！FLUX+ACE++换头_1930479706833895425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra`
- `LayerStyle: ColorOverlay V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SimpleMath+`
- `StyleModelLoader`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerMask: ObjectDetectorYOLO8` —— 1/2 个有
- `LayerMask: SAM2Ultra` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `Simple String` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `TeaCache` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
