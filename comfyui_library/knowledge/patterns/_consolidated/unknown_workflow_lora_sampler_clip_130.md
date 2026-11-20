---
name: unknown_workflow_lora_sampler_clip_130
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93725
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatchToReference, Flux2Scheduler, GetImageSize, ImageCompositeMasked, ImageScaleToMaxDimension, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/7.脸部替换_2050760455714549761.json, 图片生成/图生图/flux2klein9b模特换装_2052730446903029761.json, 图片生成/图生图/flux2klein9b模特换装_2059443358996713474.json, 图片生成/图生图/flux2klein9b模特换装_2064546539829288961.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/7.脸部替换_2050760455714549761.json、图片生成/图生图/flux2klein9b模特换装_2052730446903029761.json、图片生成/图生图/flux2klein9b模特换装_2059443358996713474.json、图片生成/图生图/flux2klein9b模特换装_2064546539829288961.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchToReference`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageCompositeMasked`
- `ImageScaleToMaxDimension`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `ClothesSegment` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `Int` —— 3/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `AutoCropFaces` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `MaskPreview` —— 1/4 个有
- `SAM3Segment` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
