---
name: unknown_workflow_inpaint_upscale_sampler_11
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.838
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CM_IntBinaryCondition, CR Upscale Image, ColorMatch, ConditioningZeroOut, Florence2ModelLoader, Florence2Run, GetImageSize+, GetNode, GrowMask, Image Comparer (rgthree), ImageComposite+, ImpactInt, ImpactSwitch, InpaintModelConditioning, InvertMask, JoinImageWithAlpha, KSamplerSelect, LayerFilter: AddGrain, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: If , LoadImage, MaskBlur+, ModelSamplingAuraFlow, PathchSageAttentionKJ, RandomNoise, ResizeImageMixlab, SamplerCustomAdvanced, SaveImage, SetNode, SimpleMath+, SplitImageWithAlpha, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/04放大3K增加细节 (ZIMG) (自动遮罩)_2012858553723260929.json, 图片生成/图生图/超分3K (ZIMG) (自用)_2059942451997143041.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/04放大3K增加细节 (ZIMG) (自动遮罩)_2012858553723260929.json、图片生成/图生图/超分3K (ZIMG) (自用)_2059942451997143041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntBinaryCondition`
- `CR Upscale Image`
- `ColorMatch`
- `ConditioningZeroOut`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSize+`
- `GetNode`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImpactInt`
- `ImpactSwitch`
- `InpaintModelConditioning`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSamplerSelect`
- `LayerFilter: AddGrain`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: If `
- `LoadImage`
- `MaskBlur+`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImageMixlab`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `SplitImageWithAlpha`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
