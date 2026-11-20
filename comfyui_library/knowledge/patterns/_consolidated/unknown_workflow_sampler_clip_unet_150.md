---
name: unknown_workflow_sampler_clip_unet_150
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.873875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FluxKlein局部重绘_指定区域_人物替换加速高质量_2033369130442690561.json, 图片生成/图生图/Klein-一致性_2028302502973677570.json, 图片生成/图生图/Klein-马克笔转绘（清新日系）_2034116719706378241.json, 图片生成/图生图/Klein一致性加强_2030832629217497090.json, 图片生成/图生图/Klein人物一致性发型衣服换脸一致性增强换衣服换发色换脸_2029595679181508609.json, 图片生成/图生图/NEW　Flux2-Klein-9B双图编辑_2013810307679916034.json, 图片生成/图生图/SQ-效果图优化工作流_2112780528683409410.json, 图片生成/图生图/bg_2068900398752157698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_150

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FluxKlein局部重绘_指定区域_人物替换加速高质量_2033369130442690561.json、图片生成/图生图/Klein-一致性_2028302502973677570.json、图片生成/图生图/Klein-马克笔转绘（清新日系）_2034116719706378241.json、图片生成/图生图/Klein一致性加强_2030832629217497090.json、图片生成/图生图/Klein人物一致性发型衣服换脸一致性增强换衣服换发色换脸_2029595679181508609.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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
- `ConditioningZeroOut` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `LayerUtility: ImageReel` —— 7/8 个有
- `LayerUtility: ImageReelComposit` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `JWFloat` —— 2/8 个有
- `MaskToImage` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `GrowMaskWithBlur` —— 1/8 个有
- `ImageCompositeMasked` —— 1/8 个有
- `InpaintModelConditioning` —— 1/8 个有
- `InvertMask` —— 1/8 个有
- `Mask Fill Holes` —— 1/8 个有
- `MaskPreview` —— 1/8 个有
- `SegmentV2` —— 1/8 个有
- `Text` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
