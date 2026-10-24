---
name: unknown_workflow_sampler_clip_unet_52
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.9178
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.2多图编辑工作流_2035290550059929602.json, 图片生成/图生图/Flux-Klein-9b图片编辑_2078379352756146178.json, 图片生成/图生图/Flux.2 Klein 细节增强_2053519932205355010.json, 图片生成/图生图/Flux.2 Klein 细节增强_2058818588181622785.json, 图片生成/图生图/Flux.2 Klein 细节增强_2065718342186520578.json, 图片生成/图生图/Flux.2 Klein 细节增强_2067146753337544705.json, 图片生成/图生图/Flux.2 Klein 细节增强_2086293216298618882.json, 图片生成/图生图/Flux.2 [Klein]：图片编辑4B ComfyUI官方流_2012038832811675650.json, 图片生成/图生图/Flux.2 [Klein]：多图编辑4B ComfyUI官方流_2012024295991549954.json, 图片生成/图生图/Flux.2-Klein-图像编辑_2012002471639523329.json, 图片生成/图生图/Flux2 Klein 9B Klein 海量 一图生多图 保持人物一致 多角度_2055163523919032321.json, 图片生成/图生图/Flux2 Klein 9B Klein 海量 一图生多图 保持人物一致 多角度_2059923401174765569.json, 图片生成/图生图/Klein - 万物迁移_2064542485938008065.json, 图片生成/图生图/Klein - 万物迁移_2067150065982070785.json, 图片生成/图生图/Klein - 万物迁移_2086300867355037698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/FLUX.2多图编辑工作流_2035290550059929602.json、图片生成/图生图/Flux-Klein-9b图片编辑_2078379352756146178.json、图片生成/图生图/Flux.2 Klein 细节增强_2053519932205355010.json、图片生成/图生图/Flux.2 Klein 细节增强_2058818588181622785.json、图片生成/图生图/Flux.2 Klein 细节增强_2065718342186520578.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 14/15 个有
- `VAEEncode` —— 14/15 个有
- `ConditioningZeroOut` —— 13/15 个有
- `GetImageSize` —— 13/15 个有
- `ImageScaleToTotalPixels` —— 13/15 个有
- `CR Text` —— 10/15 个有
- `LoraLoaderModelOnly` —— 9/15 个有
- `PreviewImage` —— 9/15 个有
- `Image Comparer (rgthree)` —— 8/15 个有
- `Int` —— 4/15 个有
- `PrimitiveFloat` —— 3/15 个有
- `CR Prompt List` —— 2/15 个有
- `easy promptLine` —— 2/15 个有
- `Anything Everywhere` —— 1/15 个有
- `ConditioningAddImageReferenceDual` —— 1/15 个有
- `FluxKontextImageScale` —— 1/15 个有
- `ImageScale` —— 1/15 个有
- `ImageScaleToMaxDimension` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
