---
name: unknown_workflow_controlnet_inpaint_sampler_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [AddMask, ApplyInstantID, BlendInpaint, CLIPTextEncode, ControlNetLoader, CutForInpaint, GrowMaskWithBlur, ImageAndMaskPreview, ImageConcatMulti, ImageToMask, ImpactMakeImageBatch, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWMaskResize, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, MaskToImage, PreviewBridge, PreviewImage, RHHiddenNodes, SaveImage, SubtractMask, VAEDecode, easy imageSizeByLongerSide, easy int, easy mathInt, workflow>123]
problems: []
missing: []
members: [图片生成/图生图/InstandID换脸工作流V5_1967512021887541250.json, 平台全量/InstandID换脸工作流V5_1911062848762773506.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/InstandID换脸工作流V5_1967512021887541250.json、平台全量/InstandID换脸工作流V5_1911062848762773506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `ApplyInstantID`
- `BlendInpaint`
- `CLIPTextEncode`
- `ControlNetLoader`
- `CutForInpaint`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageConcatMulti`
- `ImageToMask`
- `ImpactMakeImageBatch`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWMaskResize`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SubtractMask`
- `VAEDecode`
- `easy imageSizeByLongerSide`
- `easy int`
- `easy mathInt`
- `workflow>123`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.2 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
