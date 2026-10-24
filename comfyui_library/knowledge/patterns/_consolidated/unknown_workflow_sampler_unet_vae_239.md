---
name: unknown_workflow_sampler_unet_vae_239
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.52125
common_nodes: [CFGGuider, CLIPLoader, CR Text, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ColorImage, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, 取色器_孤海]
problems: []
missing: []
members: [图片生成/图生图/klein多人换脸工作流_2053015236344590337.json, 图片生成/图生图/klein换脸工作流_2053009442458873858.json, 图片生成/文生图/Klein人物换装_2053675322071105538.json, 图片生成/文生图/Klein物体精准迁移_2052612982663852033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_239

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/klein多人换脸工作流_2053015236344590337.json、图片生成/图生图/klein换脸工作流_2053009442458873858.json、图片生成/文生图/Klein人物换装_2053675322071105538.json、图片生成/文生图/Klein物体精准迁移_2052612982663852033.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CR Text`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `取色器_孤海`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `LayerUtility: CropBoxResolve` —— 3/4 个有
- `LayerUtility: CropByMask V2` —— 3/4 个有
- `Mask Fill Holes` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `ColorMatch` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
