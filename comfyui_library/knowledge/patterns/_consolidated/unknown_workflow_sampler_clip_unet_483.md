---
name: unknown_workflow_sampler_clip_unet_483
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.749
common_nodes: [Anything Everywhere, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WH-AI-Studio电商换装-服装迁移klein材质版（带颜色校正）_2019751763208839169.json, 平台全量/高清放大_包浆图修复_2012055646769778689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_483

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio电商换装-服装迁移klein材质版（带颜色校正）_2019751763208839169.json、平台全量/高清放大_包浆图修复_2012055646769778689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
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
- `Image Blending Mode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImitationHueNode` —— 1/2 个有
- `LayerColor: ColorAdapter` —— 1/2 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/2 个有
- `MaskColorize` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
