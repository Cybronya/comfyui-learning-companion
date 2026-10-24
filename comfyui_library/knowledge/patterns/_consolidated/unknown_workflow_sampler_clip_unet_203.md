---
name: unknown_workflow_sampler_clip_unet_203
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.930833
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/11.高清放大，质感提升_2050782119433129985.json, 图片生成/图生图/13.老照片修复_2051995992244932609.json, 图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json, 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json, 图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json, 图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_203

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/11.高清放大，质感提升_2050782119433129985.json、图片生成/图生图/13.老照片修复_2051995992244932609.json、图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json、图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json、图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `SeedVR2VideoUpscaler` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `ImageScaleBy` —— 3/6 个有
- `FeatherMask` —— 2/6 个有
- `ImageStitch` —— 2/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `InpaintModelConditioning` —— 2/6 个有
- `MaskPreview` —— 2/6 个有
- `ResizeImagesByLongerEdge` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `ColorMatch` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ImageAddNoise` —— 1/6 个有
- `ImageCASharpening+` —— 1/6 个有
- `ImageColorMatch+` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
