---
name: unknown_workflow_inpaint_upscale_sampler_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7935
common_nodes: [AILab_QwenVL, BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, DetailDaemonSamplerNode, Florence2ModelLoader, Florence2Run, FluxKontextMultiReferenceLatentMethod, GetNode, Image Comparer (rgthree), ImageColorMatch+, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, InpaintCropImproved, InpaintStitchImproved, KSamplerSelect, LayerUtility: ImageMaskScaleAs, LoadImage, MaskPreview, PreviewImage, ReferenceLatent, SAM3Segment, SamplerCustom, SamplerEulerAncestral, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/seedvr2+qwen-edit-2511+z-image-turbo-人像专用高清修复放大流_2021608580713029633.json, 平台全量/TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/seedvr2+qwen-edit-2511+z-image-turbo-人像专用高清修复放大流_2021608580713029633.json、平台全量/TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailDaemonSamplerNode`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSamplerSelect`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `MaskPreview`
- `PreviewImage`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustom`
- `SamplerEulerAncestral`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
