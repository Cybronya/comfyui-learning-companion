---
name: unknown_workflow_sampler_clip_unet_70
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.949333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FluxKlein场景替换_人物替换加速高质量_2033122074021076994.json, 图片生成/图生图/FluxKlein局部重绘_指定区域_人物替换加速高质量_2033369130442690561.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2041822266979262465.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2067227622874107905.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2082102047633141761.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器！Flux2！_2041743908442476546.json, 图片生成/图生图/Klein BFS 换脸换头！加强版！Flux2_2041514830745571329.json, 图片生成/图生图/NEW　Flux2-Klein-9B双图编辑_2013810307679916034.json, 图片生成/图生图/单图编辑版+10秒出图（FLUX2+Klein）_2012861610414575618.json, 图片生成/图生图/双图编辑版+全能模型（FLUX2+Klein）_2012868598808715265.json, 图片生成/图生图/😶_🌫️FLUX新王炸 Klein 图像编辑版 急速10秒出图😶_🌫️_2012100971706458113.json, 图片生成/图生图/😶‍🌫️FLUX新王炸 Klein 双图编辑版😶‍🌫️_2012282965887291393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_70

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FluxKlein场景替换_人物替换加速高质量_2033122074021076994.json、图片生成/图生图/FluxKlein局部重绘_指定区域_人物替换加速高质量_2033369130442690561.json、图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2041822266979262465.json、图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2067227622874107905.json、图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2082102047633141761.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
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
- `LayerUtility: ImageReel` —— 11/12 个有
- `LayerUtility: ImageReelComposit` —— 11/12 个有
- `EmptyFlux2LatentImage` —— 10/12 个有
- `GetImageSize` —— 10/12 个有
- `CR Text` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `Image Crop Face` —— 5/12 个有
- `LayerUtility: PurgeVRAM V2` —— 5/12 个有
- `JWFloat` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `ImageCompositeMasked` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `Mask Fill Holes` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
