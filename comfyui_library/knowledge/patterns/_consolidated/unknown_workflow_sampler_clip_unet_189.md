---
name: unknown_workflow_sampler_clip_unet_189
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.876429
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-Klein-文生图-10秒急速出图_2012122075317669889.json, 图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json, 图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json, 图片生成/文生图/FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170.json, 图片生成/文生图/FLUX2 KLEIN True-V2底模升级-文生图_2049082614698479618.json, 图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json, 图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_189

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/FLUX-Klein-文生图-10秒急速出图_2012122075317669889.json、图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json、图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json、图片生成/文生图/FLUX.2-klein_官方基础工作流（文生图）_2048617862490759170.json、图片生成/文生图/FLUX2 KLEIN True-V2底模升级-文生图_2049082614698479618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `SeedVR2LoadDiTModel` —— 3/7 个有
- `SeedVR2LoadVAEModel` —— 3/7 个有
- `SeedVR2VideoUpscaler` —— 3/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `Text` —— 2/7 个有
- `easy promptList` —— 2/7 个有
- `ttN seed` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
