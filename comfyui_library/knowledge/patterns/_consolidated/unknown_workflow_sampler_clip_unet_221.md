---
name: unknown_workflow_sampler_clip_unet_221
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.869143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/生图-单图编辑-FLUX2-Klein_2012457714856759298.json, 图片生成/图生图/生图-双图编辑-FLUX2-Klein_2013071704305704962.json, 图片生成/图生图/生图-图像扩图-FLUX2-Klein_2013157683704111105.json, 图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json, 平台全量/flux2_klein_9b修改模特服装尺码_2014592786938466306.json, 平台全量/定制肖像（任意换脸）_2059415154013589506.json, 视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_221

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/生图-单图编辑-FLUX2-Klein_2012457714856759298.json、图片生成/图生图/生图-双图编辑-FLUX2-Klein_2013071704305704962.json、图片生成/图生图/生图-图像扩图-FLUX2-Klein_2013157683704111105.json、图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json、平台全量/flux2_klein_9b修改模特服装尺码_2014592786938466306.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Int` —— 6/7 个有
- `GetImageSize` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `GetImageSizeAndCount` —— 3/7 个有
- `StringFunction|pysssss` —— 3/7 个有
- `easy imageConcat` —— 3/7 个有
- `easy positive` —— 3/7 个有
- `easy seed` —— 3/7 个有
- `CR Prompt Text` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `easy promptReplace` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
