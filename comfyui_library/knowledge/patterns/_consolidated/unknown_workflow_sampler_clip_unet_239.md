---
name: unknown_workflow_sampler_clip_unet_239
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9232
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 高清方法+seedvr2_2013887353395351553.json, 图片生成/图生图/PS高阶一键换脸_1903274591681421314.json, 图片生成/图生图/任意画风转写实_2053048956061536257.json, 图片生成/图生图/动漫少女现实化_2056400490073780225.json, 图片生成/图生图/服装上身与场景生成_2060636969994113025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_239

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein 高清方法+seedvr2_2013887353395351553.json、图片生成/图生图/PS高阶一键换脸_1903274591681421314.json、图片生成/图生图/任意画风转写实_2053048956061536257.json、图片生成/图生图/动漫少女现实化_2056400490073780225.json、图片生成/图生图/服装上身与场景生成_2060636969994113025.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
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
- `EmptyFlux2LatentImage` —— 4/5 个有
- `Flux2Scheduler` —— 4/5 个有
- `FluxKontextImageScale` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `SeedVR2` —— 2/5 个有
- `SeedVR2BlockSwap` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `BasicScheduler` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `LG_Color_Match_V2` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SeedVR2ExtraArgs` —— 1/5 个有
- `StringReplace` —— 1/5 个有
- `easy int` —— 1/5 个有
- `图像缩放V2_孤海` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
