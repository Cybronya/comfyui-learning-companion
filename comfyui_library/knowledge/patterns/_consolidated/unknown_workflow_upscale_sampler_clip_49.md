---
name: unknown_workflow_upscale_sampler_clip_49
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [APersonMaskGenerator, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningAverage, ConditioningZeroOut, DF_Image_scale_to_side, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageCompositeMasked, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, MaskPreview+, MuyeTextEditOutput, PreviewImage, RandomNoise, ReferenceLatent, ResizeMask, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/一站式工作流_2028044247143813122.json, 图片生成/图生图/高清_2021574160450854914.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一站式工作流_2028044247143813122.json、图片生成/图生图/高清_2021574160450854914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `APersonMaskGenerator`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningAverage`
- `ConditioningZeroOut`
- `DF_Image_scale_to_side`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MaskPreview+`
- `MuyeTextEditOutput`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeMask`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscaleNoUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
