---
name: unknown_workflow_upscale_sampler_clip_45
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.854
common_nodes: [Anything Everywhere, CFGGuider, CLIPLoader, CLIPTextEncode, DF_Integer, EmptyFlux2LatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, 孤海图像缩放按像素]
problems: []
missing: []
members: [图片生成/图生图/千府AI-FLUX3KLEIN高清放大工作流_2112723870837993473.json, 图片生成/图生图/千府AI-高清修复放大二合一工作流_2009061305344331777.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千府AI-FLUX3KLEIN高清放大工作流_2112723870837993473.json、图片生成/图生图/千府AI-高清修复放大二合一工作流_2009061305344331777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
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
- `ConditioningZeroOut` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ShunjingAIShade` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `TextGenerate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
