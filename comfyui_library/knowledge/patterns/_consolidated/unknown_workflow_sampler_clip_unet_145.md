---
name: unknown_workflow_sampler_clip_unet_145
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.832
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, easy promptList, ttN seed]
members: [图片生成/文生图/1927021794954268673.json, 图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json, 图片生成/文生图/Flux2 klein 文生图+高清放大_2062019207847567361.json, 图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_145

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1927021794954268673.json、图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json、图片生成/文生图/Flux2 klein 文生图+高清放大_2062019207847567361.json、图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `Text` —— 2/4 个有
- `ttN seed` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、easy promptList、ttN seed
