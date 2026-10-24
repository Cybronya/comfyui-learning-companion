---
name: unknown_workflow_sampler_clip_unet_106
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9319
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生图海报1_2021770523801292801.json, 图片生成/图生图/多图编辑 Flux2-Klein-9b_2062081939934367746.json, 图片生成/图生图/多图编辑 Flux2-Klein_1979531857857515522.json, 图片生成/图生图/生产力-flux2_klein单图+多图参考_2013052924347289602.json, 图片生成/图生图/电商任意角度打光 flux2 klein_2012726242851692545.json, 图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json, 图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json, 图片生成/文生图/Flux2-Klein全家桶-多功能版_2016042987171614722.json, 图片生成/文生图/文生图+图生图_2039179127982399489.json, 图片生成/文生图/文生图+图生图_2044754006899171330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_106

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图生图海报1_2021770523801292801.json、图片生成/图生图/多图编辑 Flux2-Klein-9b_2062081939934367746.json、图片生成/图生图/多图编辑 Flux2-Klein_1979531857857515522.json、图片生成/图生图/生产力-flux2_klein单图+多图参考_2013052924347289602.json、图片生成/图生图/电商任意角度打光 flux2 klein_2012726242851692545.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 9/10 个有
- `GetImageSize` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `PreviewImage` —— 5/10 个有
- `Text` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `CompressImages` —— 3/10 个有
- `DoubaoSizePreset` —— 3/10 个有
- `PlaySound|pysssss` —— 3/10 个有
- `SaveImagePlus` —— 3/10 个有
- `Label (rgthree)` —— 2/10 个有
- `CR Latent Input Switch` —— 1/10 个有
- `FluxResolutionNode` —— 1/10 个有
- `InpaintModelConditioning` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `QwenMultiangleLightningNode` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
