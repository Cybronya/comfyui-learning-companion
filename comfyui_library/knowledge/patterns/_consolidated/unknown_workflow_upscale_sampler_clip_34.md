---
name: unknown_workflow_upscale_sampler_clip_34
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.929
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageScaleBy, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json, 图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json, 图片生成/图生图/老孙AI多功能  老照片修复、去水印、偏色曝光_2088834155399442434.json, 图片生成/图生图/老照片修复 模糊变清晰_2052034476519243778.json, 图片生成/图生图/脸部迁移+换头_2015404568665919489.json, 平台全量/Flux2_Klein_9B单图带mask局部编辑_2074061408735682561.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json、图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json、图片生成/图生图/老孙AI多功能  老照片修复、去水印、偏色曝光_2088834155399442434.json、图片生成/图生图/老照片修复 模糊变清晰_2052034476519243778.json、图片生成/图生图/脸部迁移+换头_2015404568665919489.json…）

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
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageScaleBy`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `Flux2Scheduler` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `KSamplerSelect` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `FeatherMask` —— 3/6 个有
- `ImageStitch` —— 3/6 个有
- `InpaintModelConditioning` —— 3/6 个有
- `MaskPreview` —— 3/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `ImageResize+` —— 1/6 个有
- `Int` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
