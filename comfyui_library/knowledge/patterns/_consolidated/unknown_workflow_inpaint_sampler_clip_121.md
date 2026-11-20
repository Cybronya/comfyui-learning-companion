---
name: unknown_workflow_inpaint_sampler_clip_121
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DualCLIPLoader, Florence2Run, Florence2toCoordinates, FluxGuidance, GrowMask, Image Overlay, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LayerColor: Brightness & Contrast, LayerMask: MaskPreview, LoadImage, MaskToImage, PreviewImage, Sam2Segmentation, SaveImage, SimpleMath+, SolidMask, StyleModelApplyAdvanced, StyleModelLoader, SubtractMask, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/Virtual Try-on (redux + fill)_1863469676801228802.json, 平台全量/vitrual-tryon_1924699357713788929.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Virtual Try-on (redux + fill)_1863469676801228802.json、平台全量/vitrual-tryon_1924699357713788929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `Florence2toCoordinates`
- `FluxGuidance`
- `GrowMask`
- `Image Overlay`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LayerMask: MaskPreview`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `Sam2Segmentation`
- `SaveImage`
- `SimpleMath+`
- `SolidMask`
- `StyleModelApplyAdvanced`
- `StyleModelLoader`
- `SubtractMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AutoCropFaces` —— 1/2 个有
- `Image Paste Face` —— 1/2 个有
- `LayerMask: HumanPartsUltra` —— 1/2 个有
- `RMBG` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
