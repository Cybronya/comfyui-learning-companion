---
name: unknown_workflow_sampler_clip_unet_158
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.929875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein人物资产图三视图工作流_2085581343009886209.json, 图片生成/图生图/klein人物资产图四视图工作流_2095363498720186370.json, 图片生成/图生图/z2.tonnie-Klein单图编辑_2007964265013059585.json, 图片生成/图生图/z3.tonnie-klein双图编辑_2012791905364480002.json, 图片生成/图生图/z4.tonnie-klein三图编辑_2012802358866092033.json, 图片生成/图生图/人物换装-Klein-9B-工作流_2041526824202674177.json, 图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json, 图片生成/图生图/角色四视图-klein9b_2083577051046567937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/klein人物资产图三视图工作流_2085581343009886209.json、图片生成/图生图/klein人物资产图四视图工作流_2095363498720186370.json、图片生成/图生图/z2.tonnie-Klein单图编辑_2007964265013059585.json、图片生成/图生图/z3.tonnie-klein双图编辑_2012791905364480002.json、图片生成/图生图/z4.tonnie-klein三图编辑_2012802358866092033.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `LoraLoaderModelOnly` —— 7/8 个有
- `Flux2Scheduler` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `BasicScheduler` —— 3/8 个有
- `ModelSamplingAuraFlow` —— 3/8 个有
- `easy int` —— 3/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `ResizeImagesByLongerEdge` —— 2/8 个有
- `GetImageSize+` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
