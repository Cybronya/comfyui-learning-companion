---
name: unknown_workflow_sampler_clip_unet_98
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9237
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-2-Klein 动漫转真人_2073666905835130882.json, 图片生成/图生图/Flux-Klein--去水印移除物体_2028367858878648322.json, 图片生成/图生图/Flux-Klein--模特融背景_2028368955097747457.json, 图片生成/图生图/Flux-Klein-姿势控制_2070702060726738946.json, 图片生成/图生图/Flux-Klein-深度姿势控制_2070700152016433154.json, 图片生成/图生图/Flux-Klein-线稿上色_2070705518980722689.json, 图片生成/图生图/Flux.2：90年代港风风格化_2079049505210724353.json, 图片生成/图生图/Klein 9B线稿参考上色_2070582629883269121.json, 图片生成/图生图/Klein 9B线稿参考上色_2070762276864487425.json, 图片生成/图生图/Klein 9B线稿参考上色_2070873331376676865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_98

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux-2-Klein 动漫转真人_2073666905835130882.json、图片生成/图生图/Flux-Klein--去水印移除物体_2028367858878648322.json、图片生成/图生图/Flux-Klein--模特融背景_2028368955097747457.json、图片生成/图生图/Flux-Klein-姿势控制_2070702060726738946.json、图片生成/图生图/Flux-Klein-深度姿势控制_2070700152016433154.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `LoraLoaderModelOnly` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `ImageConcatMulti` —— 6/10 个有
- `AIO_Preprocessor` —— 4/10 个有
- `ImageConcanate` —— 3/10 个有
- `AddLabel` —— 1/10 个有
- `ControlNetLoader` —— 1/10 个有
- `FluxUnionControlNetApply` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SetUnionControlNetType` —— 1/10 个有
- `TextGenerate` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | canny | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
