---
name: unknown_workflow_sampler_clip_unet_270
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8244
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/生图-单图编辑-FLUX2-Klein_2012457714856759298.json, 图片生成/图生图/生图-双图编辑-FLUX2-Klein_2013071704305704962.json, 图片生成/图生图/生图-图像扩图-FLUX2-Klein_2013157683704111105.json, 图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json, 视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_270

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/生图-单图编辑-FLUX2-Klein_2012457714856759298.json、图片生成/图生图/生图-双图编辑-FLUX2-Klein_2013071704305704962.json、图片生成/图生图/生图-图像扩图-FLUX2-Klein_2013157683704111105.json、图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json、视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Int`
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
- `GetImageSizeAndCount` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `StringFunction|pysssss` —— 3/5 个有
- `easy imageConcat` —— 3/5 个有
- `easy positive` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImagePadForOutpaint` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
