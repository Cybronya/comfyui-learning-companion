---
name: unknown_workflow_sampler_clip_unet_111
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8975
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein三视图_2047955676676231169.json, 图片生成/图生图/Flux2-Klein人物角色三视图3D国漫CG风格（图生图）_2090025230700990466.json, 图片生成/图生图/Flux2-klein9B单图+双图编辑工作流_2012386786735034369.json, 图片生成/图生图/Flux2-klein单图+双图编辑_2012711003414339585.json, 图片生成/图生图/Flux2Klein动漫转写实真人+细节增强_2063438140592975874.json, 图片生成/图生图/Flux2Klein动漫转真实+细节增强_2060937329581318146.json, 图片生成/图生图/Klein - 万物迁移_2064542485938008065.json, 图片生成/图生图/Klein - 万物迁移_2067150065982070785.json, 图片生成/图生图/Klein - 万物迁移_2086300867355037698.json, 图片生成/图生图/产品精修工作流_2032002851513307137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_111

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein三视图_2047955676676231169.json、图片生成/图生图/Flux2-Klein人物角色三视图3D国漫CG风格（图生图）_2090025230700990466.json、图片生成/图生图/Flux2-klein9B单图+双图编辑工作流_2012386786735034369.json、图片生成/图生图/Flux2-klein单图+双图编辑_2012711003414339585.json、图片生成/图生图/Flux2Klein动漫转写实真人+细节增强_2063438140592975874.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

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
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `ConditioningZeroOut` —— 8/10 个有
- `GetImageSize` —— 8/10 个有
- `ImageScaleToTotalPixels` —— 8/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `CR Text` —— 5/10 个有
- `PrimitiveFloat` —— 4/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `Anything Everywhere` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `easy imageConcat` —— 2/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `EmptyLatentImage` —— 1/10 个有
- `ImageCompositeMasked` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `LayerColor: ColorAdapter` —— 1/10 个有
- `MaskBlur+` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `ttN concat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 576 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
