---
name: unknown_workflow_sampler_clip_unet_239
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.782857
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux2 Klein局部重绘_2014296617834254337.json, 平台全量/Flux2+Klein局部重绘_2018874839578185730.json, 平台全量/Flux2-Klein _单图编辑_2039283172344602625.json, 平台全量/Flux2-Klein-9B 单图编辑+局部重绘+图片扩展_2030499494369955841.json, 平台全量/Flux2-Klein扩图工作流_2013148167063216130.json, 平台全量/Flux2_klein图像编辑合集_2116045463802695682.json, 平台全量/星途Flux2 Klein重绘移除_2078589738642132993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_239

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Flux2 Klein局部重绘_2014296617834254337.json、平台全量/Flux2+Klein局部重绘_2018874839578185730.json、平台全量/Flux2-Klein _单图编辑_2039283172344602625.json、平台全量/Flux2-Klein-9B 单图编辑+局部重绘+图片扩展_2030499494369955841.json、平台全量/Flux2-Klein扩图工作流_2013148167063216130.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
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
- `ConditioningZeroOut` —— 6/7 个有
- `EmptyFlux2LatentImage` —— 5/7 个有
- `InpaintModelConditioning` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `GrowMaskWithBlur` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `DifferentialDiffusion` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `ImagePadForOutpaint` —— 3/7 个有
- `PlaySound|pysssss` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `LanPaint_MaskBlend` —— 2/7 个有
- `MaskPreview+` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `ColorMatch` —— 1/7 个有
- `TextInputNode` —— 1/7 个有
- `easy imageScaleDownToSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
