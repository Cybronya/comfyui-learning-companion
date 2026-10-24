---
name: unknown_workflow_inpaint_lora_sampler_56
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6215
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionLoader, CR Latent Batch Size, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageCrop+, ImpactImageBatchToImageList, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerMask: MaskStroke, LayerUtility: CropByMask V2, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, ReduxAdvanced, Replace Text _O, SaveImage, SetNode, String Literal, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/⭐️-万物迁移集合--------换装换物换模特_1961679739511619586.json, 图片生成/图生图/换装稳定版_1951545753758060546.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/⭐️-万物迁移集合--------换装换物换模特_1961679739511619586.json、图片生成/图生图/换装稳定版_1951545753758060546.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCrop+`
- `ImpactImageBatchToImageList`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerMask: MaskStroke`
- `LayerUtility: CropByMask V2`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `Replace Text _O`
- `SaveImage`
- `SetNode`
- `String Literal`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `Get resolution [Crystools]` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ReduxPromptStyler` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy imageInsetCrop` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
