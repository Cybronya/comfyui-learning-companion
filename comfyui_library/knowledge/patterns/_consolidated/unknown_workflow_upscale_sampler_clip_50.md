---
name: unknown_workflow_upscale_sampler_clip_50
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.853667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, DF_Integer, EmptyFlux2LatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, 孤海图像缩放按像素]
problems: []
missing: []
members: [图片生成/图生图/千府AI-FLUX3KLEIN高清放大工作流_2112723870837993473.json, 图片生成/图生图/千府AI-FLUX3KLEIN高清放大工作流_2116142011337232386.json, 图片生成/图生图/千府AI-高清修复放大二合一工作流_2009061305344331777.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千府AI-FLUX3KLEIN高清放大工作流_2112723870837993473.json、图片生成/图生图/千府AI-FLUX3KLEIN高清放大工作流_2116142011337232386.json、图片生成/图生图/千府AI-高清修复放大二合一工作流_2009061305344331777.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `孤海图像缩放按像素`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ShunjingAIShade` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `Flux2Scheduler` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
