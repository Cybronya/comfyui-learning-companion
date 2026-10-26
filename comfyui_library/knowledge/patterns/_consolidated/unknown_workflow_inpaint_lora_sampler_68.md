---
name: unknown_workflow_inpaint_lora_sampler_68
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.87
common_nodes: [AdvancedVisionLoader, CLIPTextEncode, CLIPVisionEncode, CR Text, ConditioningZeroOut, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, GrowMaskWithBlur, ImageFromBatch+, ImageScaleToTotalPixels, InpaintCrop, InpaintModelConditioning, InpaintStitch, InvertMask, KSampler (Efficient), LayerMask: MaskPreview, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LayerUtility: If , LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, PrimitiveInt, Replace Text _O, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, TTP_Expand_And_Mask, UNETLoader, VAELoader, easy imageSplitGrid, easy isMaskEmpty, easy seed, image_concat_mask(rh)]
problems: []
missing: []
members: [图片生成/图生图/局部重绘--终极换装_1933849823336685570.json, 图片生成/图生图/清凉一夏--换装_1933864747597258753.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/局部重绘--终极换装_1933849823336685570.json、图片生成/图生图/清凉一夏--换装_1933864747597258753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AdvancedVisionLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageFromBatch+`
- `ImageScaleToTotalPixels`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InvertMask`
- `KSampler (Efficient)`
- `LayerMask: MaskPreview`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LayerUtility: If `
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `PrimitiveInt`
- `Replace Text _O`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `TTP_Expand_And_Mask`
- `UNETLoader`
- `VAELoader`
- `easy imageSplitGrid`
- `easy isMaskEmpty`
- `easy seed`
- `image_concat_mask(rh)`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
