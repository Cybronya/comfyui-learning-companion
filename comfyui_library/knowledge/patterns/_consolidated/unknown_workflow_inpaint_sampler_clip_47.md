---
name: unknown_workflow_inpaint_sampler_clip_47
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.629333
common_nodes: [Any Switch (rgthree), Anything Everywhere, Bookmark (rgthree), CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, EmptyImage, Fast Groups Muter (rgthree), FluxGuidance, GetImageSize+, GetMaskSizeAndCount, GetNode, GrowMask, GrowMaskWithBlur, ImageCompositeMasked, ImageConcanate, ImageCrop+, ImageResize+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, JoinStrings, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageRemoveAlpha, LoadImage, Mask Fill Holes, MaskPreview+, MaskToImage, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, PreviewImage, SaveImage, SetNode, String Literal, StyleModelApplySimple, StyleModelLoader, VAEDecode, VAELoader, easy imageSize, easy int, easy seed]
problems: []
missing: []
members: [图片生成/图生图/万物迁移 全功能工作流 换啥都行_1911150259995901953.json, 图片生成/图生图/万物迁移+全功能工作流+换啥都行_1999439413467901953.json, 图片生成/图生图/全能万物迁移 工作流_1989300632014254081.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物迁移 全功能工作流 换啥都行_1911150259995901953.json、图片生成/图生图/万物迁移+全功能工作流+换啥都行_1999439413467901953.json、图片生成/图生图/全能万物迁移 工作流_1989300632014254081.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `Bookmark (rgthree)`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `GetMaskSizeAndCount`
- `GetNode`
- `GrowMask`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `JoinStrings`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `String Literal`
- `StyleModelApplySimple`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
