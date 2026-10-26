---
name: unknown_workflow_sampler_clip_unet_64
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.95
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein9b 一键角色三视图_2090364063200137218.json, 图片生成/图生图/Klein9b 一键角色四视图_2090374767605014530.json, 图片生成/图生图/Klein9b产品渲染精修_2050593610407653377.json, 图片生成/图生图/Klein9b产品渲染精修_2056925453222502402.json, 图片生成/图生图/KleinFace换头换脸工作流_2046745039136628737.json, 图片生成/图生图/KleinFace换头换脸工作流：Flux2-Klein-9B模型高清人物AI智能面部替换高清换脸_2017818308925464578.json, 图片生成/图生图/KleinFace换头换脸工作流：Flux2-Klein-9B模型高清人物AI智能面部替换高清换脸_2041101850404982786.json, 图片生成/图生图/KleinFace换头换脸工作流：Flux2-Klein-9B模型高清人物AI智能面部替换高清换脸_2068673231879491585.json, 图片生成/图生图/KleinFace换头换脸工作流：Flux2-Klein-9B模型高清人物AI智能面部替换高清换脸_2081686492463849473.json, 图片生成/图生图/KleinFace换头换脸工作流：Flux2-Klein-9B模型高清人物AI智能面部替换高清换脸_2106322415092588546.json, 图片生成/图生图/KleinFace换头换脸工作流：Flux2-Klein-9B模型高清人物AI智能面部替换高清换脸_2106362368719679489.json, 图片生成/图生图/Klein_亚秒级自然无缝扩图_2087736728642744321.json, 图片生成/图生图/Klein_指定位置物品替换_2065273212941979650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Klein9b 一键角色三视图_2090364063200137218.json、图片生成/图生图/Klein9b 一键角色四视图_2090374767605014530.json、图片生成/图生图/Klein9b产品渲染精修_2050593610407653377.json、图片生成/图生图/Klein9b产品渲染精修_2056925453222502402.json、图片生成/图生图/KleinFace换头换脸工作流_2046745039136628737.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 12/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `Flux2Scheduler` —— 11/13 个有
- `Image Comparer (rgthree)` —— 11/13 个有
- `GetImageSize` —— 10/13 个有
- `FluxKontextImageScale` —— 7/13 个有
- `YC Color Match` —— 7/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `DapaoImageAspectRatioResizeNode` —— 3/13 个有
- `BasicScheduler` —— 2/13 个有
- `Int` —— 2/13 个有
- `ConstrainImage|pysssss` —— 1/13 个有
- `DrawMaskOnImage` —— 1/13 个有
- `GetImageSize+` —— 1/13 个有
- `ImpactInt` —— 1/13 个有
- `LayerUtility: ExtendCanvasV2` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `easy seed` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
