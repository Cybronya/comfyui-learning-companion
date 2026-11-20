---
name: unknown_workflow_upscale_lora_sampler_36
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.936167
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageScaleToTotalPixels, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json, 图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json, "图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2034815871520083969.json", "图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2037006862268239874.json", 图片生成/图生图/老孙AI多功能  老照片修复、去水印、偏色曝光_2088834155399442434.json, 图片生成/图生图/老照片修复 模糊变清晰_2052034476519243778.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json、图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json、图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2034815871520083969.json、图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2037006862268239874.json、图片生成/图生图/老孙AI多功能  老照片修复、去水印、偏色曝光_2088834155399442434.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly`
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
- `Image Comparer (rgthree)` —— 5/6 个有
- `Flux2Scheduler` —— 4/6 个有
- `ImageScaleBy` —— 4/6 个有
- `KSamplerSelect` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `ColorMatch` —— 2/6 个有
- `FeatherMask` —— 2/6 个有
- `ImageSharpen` —— 2/6 个有
- `ImageStitch` —— 2/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `InpaintModelConditioning` —— 2/6 个有
- `MaskPreview` —— 2/6 个有
- `MuyeLoadImage` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
