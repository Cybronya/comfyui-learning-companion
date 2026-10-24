---
name: unknown_workflow_sampler_clip_unet_340
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.749
common_nodes: [Anything Everywhere, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WH-AI-Studio电商图片高清放大增强细节提高真实感（皮肤、服装材质放大器）_2022619703398633474.json, 图片生成/图生图/WH-AI-Studio电商换装-服装迁移-flux2-klein(材质增强版)(超越原图材质)_2022631112878592002.json, 图片生成/图生图/WH-AI-Studio电商换装-服装迁移klein材质版（带颜色校正）_2019751763208839169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_340

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio电商图片高清放大增强细节提高真实感（皮肤、服装材质放大器）_2022619703398633474.json、图片生成/图生图/WH-AI-Studio电商换装-服装迁移-flux2-klein(材质增强版)(超越原图材质)_2022631112878592002.json、图片生成/图生图/WH-AI-Studio电商换装-服装迁移klein材质版（带颜色校正）_2019751763208839169.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Blending Mode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerColor: ColorAdapter` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImitationHueNode` —— 1/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/3 个有
- `MaskColorize` —— 1/3 个有
- `PainterFluxImageEdit` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
