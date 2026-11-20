---
name: unknown_workflow_sampler_clip_unet_77
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.943077
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Klein 9b FP8 细节重绘超分辨率 极简工作流_2018990184506855426.json, 图片生成/图生图/Flux Klein 人物融入场景_2013179162063802369.json, 图片生成/图生图/Flux-2-Klein-4B（单图_多图编辑）_2012147672551006210.json, 图片生成/图生图/Flux-2-Klein-9B（单图编辑）_2012096588763635713.json, 图片生成/图生图/Flux-2-Klein-9B（多图编辑）_2012129810344054785.json, 图片生成/图生图/Flux-Klein｜换头+换脸二合一_2099320463754354690.json, 图片生成/图生图/Flux-Klein｜换头+换脸二合一_2099664438902222850.json, 图片生成/图生图/Flux2 Klein去除水印9B版_2012705879501574145.json, 图片生成/图生图/Flux2-Klein-衣服迁移_2012194675712593921.json, 图片生成/图生图/Flux2-klein 单双图编辑_2012469809119764482.json, 图片生成/图生图/Flux2-klein 双图编辑 指定画面比例_2013890699959209986.json, 平台全量/Flux-Klein｜换头+换脸二合一_2098444772523466753.json, 平台全量/换头换脸 并保持表情｜Flux-Klein- V2 BFS｜换头+换脸 LoRA_2044428246787301377.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux Klein 9b FP8 细节重绘超分辨率 极简工作流_2018990184506855426.json、图片生成/图生图/Flux Klein 人物融入场景_2013179162063802369.json、图片生成/图生图/Flux-2-Klein-4B（单图_多图编辑）_2012147672551006210.json、图片生成/图生图/Flux-2-Klein-9B（单图编辑）_2012096588763635713.json、图片生成/图生图/Flux-2-Klein-9B（多图编辑）_2012129810344054785.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
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
- `GetImageSize` —— 12/13 个有
- `ImageScaleToTotalPixels` —— 10/13 个有
- `Flux2Scheduler` —— 9/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/13 个有
- `BasicScheduler` —— 4/13 个有
- `ImageScale` —— 4/13 个有
- `EmptyUnitGenerator_UTK` —— 1/13 个有
- `FluxKontextImageScale` —— 1/13 个有
- `ImageScaleBy` —— 1/13 个有
- `ImageSharpen` —— 1/13 个有
- `LayerColor: AutoAdjustV2` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `Text` —— 1/13 个有
- `Text Multiline` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
