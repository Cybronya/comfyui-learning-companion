---
name: unknown_workflow_sampler_clip_unet_123
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.981444
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein9b超高清三视图_2034183674899472385.json, 图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json, 图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json, 图片生成/图生图/flux klein单图编辑_2085594588139581442.json, 图片生成/图生图/flux klein双图编辑工作流_2085595709289623554.json, 图片生成/图生图/flux klein双图编辑工作流_2105577595982143490.json, 图片生成/图生图/flux klein双图编辑工作流_2105650140253089794.json, 图片生成/图生图/一键拍立得_2077678322762473473.json, 图片生成/图生图/电商一键扩图 flux2 klein_2013426255588237313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Klein9b超高清三视图_2034183674899472385.json、图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json、图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json、图片生成/图生图/flux klein单图编辑_2085594588139581442.json、图片生成/图生图/flux klein双图编辑工作流_2085595709289623554.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `ImagePadForOutpaint` —— 3/9 个有
- `AILab_ImageStitch` —— 1/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有
- `ColorMatch` —— 1/9 个有
- `DrawMaskOnImage` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `LayerStyle: ColorOverlay` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `ResolutionMaster` —— 1/9 个有
- `StringConcatenate` —— 1/9 个有
- `StringConstant` —— 1/9 个有
- `VRAMReserver` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
