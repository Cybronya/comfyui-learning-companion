---
name: unknown_workflow_sampler_clip_unet_116
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9654
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图案转刺绣风格加抠图_2043607679398060034.json, 图片生成/图生图/图片换背景换人物换衣服_2052614808108838913.json, 图片生成/图生图/图片编辑（对比）_2094024830000656386.json, 图片生成/图生图/图片自动转贴纸风格_2052206077697118210.json, 图片生成/图生图/图片自动转贴纸风格，超cute！_2056556461433638913.json, 图片生成/图生图/图片自动转贴纸风格，超cute！_2056907377747783682.json, 图片生成/图生图/常用_图片_flux2_单图_2037742922816299009.json, 图片生成/图生图/建筑、室内 flux2-klein3图 编辑_2039312458275364866.json, 图片生成/图生图/添加真实感细节 _ flux 2_1962490094668132354.json, 图片生成/图生图/自拍照+服装参考图一键生成证件照_2020047100834226178.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_116

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图案转刺绣风格加抠图_2043607679398060034.json、图片生成/图生图/图片换背景换人物换衣服_2052614808108838913.json、图片生成/图生图/图片编辑（对比）_2094024830000656386.json、图片生成/图生图/图片自动转贴纸风格_2052206077697118210.json、图片生成/图生图/图片自动转贴纸风格，超cute！_2056556461433638913.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 9/10 个有
- `SaveImage` —— 9/10 个有
- `ConditioningZeroOut` —— 8/10 个有
- `GetImageSize` —— 8/10 个有
- `ImageResize+` —— 4/10 个有
- `ImageScaleToTotalPixels` —— 4/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `Preview from image [Crystools]` —— 1/10 个有
- `PrimitiveString` —— 1/10 个有
- `RMBG` —— 1/10 个有
- `ResizeImageNode` —— 1/10 个有
- `SaveImageAndMetadata_` —— 1/10 个有
- `StringReplace` —— 1/10 个有
- `ttN text` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
