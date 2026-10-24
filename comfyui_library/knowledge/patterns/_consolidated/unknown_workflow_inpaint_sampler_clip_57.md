---
name: unknown_workflow_inpaint_sampler_clip_57
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8065
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, DifferentialDiffusion, Fast Groups Muter (rgthree), Flux2Scheduler, FluxKontextImageScale, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageConcatMulti, InpaintModelConditioning, KOOK_SaveJPGImage, KSamplerSelect, LayerMask: MaskPreview, LayerUtility: ExtendCanvasV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SolidMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-klein扩图工作流_2012416157290074114.json, 图片生成/图生图/【🛫书墨】FLUX2-klein极限扩图工作流_2012079808972328961.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX2-klein扩图工作流_2012416157290074114.json、图片生成/图生图/【🛫书墨】FLUX2-klein极限扩图工作流_2012079808972328961.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `Fast Groups Muter (rgthree)`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `InpaintModelConditioning`
- `KOOK_SaveJPGImage`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LayerUtility: ExtendCanvasV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
