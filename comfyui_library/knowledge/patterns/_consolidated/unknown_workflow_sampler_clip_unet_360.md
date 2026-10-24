---
name: unknown_workflow_sampler_clip_unet_360
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.707333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSizeAndCount, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, easy positive, easy seed]
problems: []
missing: []
members: [图片生成/图生图/生图-单图编辑-FLUX2-Klein_2012457714856759298.json, 图片生成/图生图/生图-双图编辑-FLUX2-Klein_2013071704305704962.json, 图片生成/图生图/生图-图像扩图-FLUX2-Klein_2013157683704111105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_360

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/生图-单图编辑-FLUX2-Klein_2012457714856759298.json、图片生成/图生图/生图-双图编辑-FLUX2-Klein_2013071704305704962.json、图片生成/图生图/生图-图像扩图-FLUX2-Klein_2013157683704111105.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSizeAndCount`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
