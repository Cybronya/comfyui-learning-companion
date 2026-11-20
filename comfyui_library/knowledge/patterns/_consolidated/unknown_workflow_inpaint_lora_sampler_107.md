---
name: unknown_workflow_inpaint_lora_sampler_107
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.92
common_nodes: [AddMask, BOOLConstant, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_FloatBinaryOperation, CM_FloatToInt, CM_IntToFloat, CR Text Concatenate, CachePreviewBridge, ConditioningZeroOut, CutForInpaint, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyImage, Florence2Run, FluxGuidance, ImageAndMaskPreview, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LayerUtility: ColorImage V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LazySwitch1way, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, RHHiddenNodes, SaveImage, String Literal, StyleModelApply, StyleModelLoader, SubtractMask, VAEDecode, VAELoader, VHS_DuplicateLatents, easy imageSize, easy int, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/顶级换装流V3_1986295179470655489.json, 平台全量/顶级换装流V3 2025年11月5日更新_1912445006827978754.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/顶级换装流V3_1986295179470655489.json、平台全量/顶级换装流V3 2025年11月5日更新_1912445006827978754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `BOOLConstant`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_FloatBinaryOperation`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Text Concatenate`
- `CachePreviewBridge`
- `ConditioningZeroOut`
- `CutForInpaint`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `Florence2Run`
- `FluxGuidance`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LazySwitch1way`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `String Literal`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `VAEDecode`
- `VAELoader`
- `VHS_DuplicateLatents`
- `easy imageSize`
- `easy int`
- `easy mathInt`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
