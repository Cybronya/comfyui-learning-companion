---
name: unknown_workflow_inpaint_sampler_clip_117
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.891
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, Display Any (rgthree), DualCLIPLoader, Fast Groups Bypasser (rgthree), GrowMask, GrowMaskWithBlur, ImageConcanate, ImageResizeKJ, ImageToMask, ImpactKSamplerBasicPipe, InpaintCrop, InpaintModelConditioning, InpaintStitch, LayerUtility: ColorImage V2, LayerUtility: ImageMaskScaleAs, LoadImage, Mask Fill Holes, MaskToImage, PreviewImage, SaveImage, StyleModelLoader, ToBasicPipe, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/05.服装模特换装工作流_2000793008729620482.json, 平台全量/08.服装商品换色工作流_2000793079114330114.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/05.服装模特换装工作流_2000793008729620482.json、平台全量/08.服装商品换色工作流_2000793079114330114.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GrowMask`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageToMask`
- `ImpactKSamplerBasicPipe`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelLoader`
- `ToBasicPipe`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Cut By Mask` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
