---
name: unknown_workflow_sampler_clip_unet_190
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.964571
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2 klein 文生图+高清放大_2062019207847567361.json, 图片生成/文生图/Flux2 klein 直出不崩手基础流（文生图）_2018252380457930754.json, 图片生成/文生图/Flux2-Klein 极速文生图_2021569732054355969.json, 图片生成/文生图/Flux2-Klein-9B基础工作流_2012498111796613121.json, 图片生成/文生图/Flux2-Klein-9B基础工作流_2012504605866860545.json, 图片生成/文生图/Flux2文生图极速版—阿浩_2029018694231269377.json, 图片生成/文生图/文生图（解禁模型）：Flux.2 Klein 9B_2051283326727663617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_190

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux2 klein 文生图+高清放大_2062019207847567361.json、图片生成/文生图/Flux2 klein 直出不崩手基础流（文生图）_2018252380457930754.json、图片生成/文生图/Flux2-Klein 极速文生图_2021569732054355969.json、图片生成/文生图/Flux2-Klein-9B基础工作流_2012498111796613121.json、图片生成/文生图/Flux2-Klein-9B基础工作流_2012504605866860545.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

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
- `ConditioningZeroOut` —— 6/7 个有
- `Int` —— 5/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `SeedVR2LoadDiTModel` —— 2/7 个有
- `SeedVR2LoadVAEModel` —— 2/7 个有
- `SeedVR2VideoUpscaler` —— 2/7 个有
- `String Literal` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
