---
name: unknown_workflow_sampler_clip_unet_251
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8355
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json, 图片生成/图生图/Flux2-Klein9b一键产品加背景 白底产品换背景换场景_2033110402749435906.json, 图片生成/图生图/Flux2-Klein_9B_编辑_角度_光线_双图_2014310579040690177.json, 图片生成/图生图/三图编辑 Flux2-Klein_2012122566953013249.json, 图片生成/图生图/产品智能场景摆放_Flux2 Klein_2014540954375561218.json, 平台全量/Flux2 Klein 重新打光，照片过曝，光斑，上色，偏色，老照片修复，万能P图，去水印_2029451864806268929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_251

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json、图片生成/图生图/Flux2-Klein9b一键产品加背景 白底产品换背景换场景_2033110402749435906.json、图片生成/图生图/Flux2-Klein_9B_编辑_角度_光线_双图_2014310579040690177.json、图片生成/图生图/三图编辑 Flux2-Klein_2012122566953013249.json、图片生成/图生图/产品智能场景摆放_Flux2 Klein_2014540954375561218.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
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
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Flux2Scheduler` —— 5/6 个有
- `KSamplerSelect` —— 5/6 个有
- `ImageScaleBy` —— 3/6 个有
- `SeedVR2LoadDiTModel` —— 3/6 个有
- `SeedVR2LoadVAEModel` —— 3/6 个有
- `SeedVR2VideoUpscaler` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `QwenMultiangleLightningNode` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
