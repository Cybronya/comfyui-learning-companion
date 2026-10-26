---
name: unknown_workflow_sampler_clip_unet_218
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.877
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, Flux2Scheduler, GrowMaskWithBlur, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein移除水印单图版V2（保持原图不变）_2014510703759069185.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2015367193973760002.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2028122775256305666.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2054741458850205697.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2054837030131126273.json, 图片生成/图生图/移除即梦水印单图版V2（保持原图不变）_2012487948297572353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_218

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein移除水印单图版V2（保持原图不变）_2014510703759069185.json、图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2015367193973760002.json、图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2028122775256305666.json、图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2054741458850205697.json、图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2054837030131126273.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `DrawMaskOnImage` —— 4/6 个有
- `EmptyFlux2LatentImage` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `ImagePadForOutpaint` —— 4/6 个有
- `ImageMaskSwitch` —— 3/6 个有
- `ImpactSwitch` —— 3/6 个有
- `Int` —— 3/6 个有
- `ImageCompositeMasked` —— 2/6 个有
- `ImageConcanate` —— 2/6 个有
- `ImageCrop+` —— 2/6 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/6 个有
- `LayerUtility: ImageReel` —— 2/6 个有
- `LayerUtility: ImageReelComposit` —— 2/6 个有
- `MaskPreview` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
