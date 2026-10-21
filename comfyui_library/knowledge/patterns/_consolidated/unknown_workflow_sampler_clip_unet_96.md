---
name: unknown_workflow_sampler_clip_unet_96
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json, 图片生成/文生图/Flux2 klein 直出不崩手基础流（文生图）_2018252380457930754.json, 图片生成/文生图/Flux2-Klein 极速文生图_2021569732054355969.json, 图片生成/文生图/Flux2-Klein-9B基础工作流_2012498111796613121.json, 图片生成/文生图/Flux2-Klein-9B基础工作流_2012504605866860545.json, 图片生成/文生图/Flux2文生图_1995379549791825922.json, 视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_96

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json、图片生成/文生图/Flux2 klein 直出不崩手基础流（文生图）_2018252380457930754.json、图片生成/文生图/Flux2-Klein 极速文生图_2021569732054355969.json、图片生成/文生图/Flux2-Klein-9B基础工作流_2012498111796613121.json、图片生成/文生图/Flux2-Klein-9B基础工作流_2012504605866860545.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
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
- `CFGGuider` —— 5/7 个有
- `Int` —— 4/7 个有
- `BasicGuider` —— 3/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `FluxGuidance` —— 3/7 个有
- `CompressImages` —— 2/7 个有
- `Int Literal` —— 2/7 个有
- `String Literal` —— 2/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `WidthHeightPicker` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
