---
name: unknown_workflow_sampler_clip_unet_59
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.968533
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图案转刺绣风格加抠图_2043607679398060034.json, 图片生成/图生图/图片换背景换人物换衣服_2052614808108838913.json, 图片生成/图生图/图片编辑（对比）_2094024830000656386.json, 图片生成/图生图/图片自动转贴纸风格_2052206077697118210.json, 图片生成/图生图/图片自动转贴纸风格，超cute！_2056556461433638913.json, 图片生成/图生图/图片自动转贴纸风格，超cute！_2056907377747783682.json, 图片生成/图生图/建筑、室内 flux2-klein3图 编辑_2039312458275364866.json, 图片生成/图生图/更用好的换脸工作流 DarkBeast（黑兽）风格-Klein9b-BFS_2039134741198282753.json, 图片生成/图生图/最强换面流-Klein9b-BFS_2029175273211564034.json, 图片生成/图生图/贼好用的换脸-Klein9b-BFS_2087457438445424641.json, 图片生成/图生图/🦖Flux2-klein单图编辑_2013897331980111873.json, 图片生成/文生图/AI一键生成12张绝美新年写真集_2024044240682098690.json, 图片生成/文生图/人像换脸丨Flux2-Klein 9B丨面部发型替换_2105644038434152450.json, 平台全量/Flux 2 klein 4b 换头换脸 真实自然 局部重绘  换装 写实摄影_2015291498807431170.json, 平台全量/Flux-Klein｜换头+换脸二合一③_2102028983708770306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/图案转刺绣风格加抠图_2043607679398060034.json、图片生成/图生图/图片换背景换人物换衣服_2052614808108838913.json、图片生成/图生图/图片编辑（对比）_2094024830000656386.json、图片生成/图生图/图片自动转贴纸风格_2052206077697118210.json、图片生成/图生图/图片自动转贴纸风格，超cute！_2056556461433638913.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 15 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 14/15 个有
- `GetImageSize` —— 14/15 个有
- `SaveImage` —— 14/15 个有
- `ConditioningZeroOut` —— 13/15 个有
- `ImageScaleToTotalPixels` —— 9/15 个有
- `Image Comparer (rgthree)` —— 7/15 个有
- `LayerUtility: PurgeVRAM V2` —— 5/15 个有
- `ImageResize+` —— 4/15 个有
- `Seed (rgthree)` —— 4/15 个有
- `HAIGC_LoadImagesFromZip` —— 1/15 个有
- `Image Crop Face` —— 1/15 个有
- `Preview from image [Crystools]` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `RMBG` —— 1/15 个有
- `ResizeImageNode` —— 1/15 个有
- `SaveImageAndMetadata_` —— 1/15 个有
- `ttN text` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
