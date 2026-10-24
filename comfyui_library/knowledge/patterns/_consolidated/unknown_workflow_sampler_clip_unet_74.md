---
name: unknown_workflow_sampler_clip_unet_74
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.82075
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2 Klein 文生图工作流_2091474310002200578.json, 图片生成/文生图/FLUX2 klein-9B 【文生图】_2013859086563024897.json, 图片生成/文生图/FLUX2 klein-9B 文生图_2013123316474716162.json, 图片生成/文生图/FLUX2-KLEIN 4B快速文生图_2012166692574601217.json, 图片生成/文生图/FLUX2-KLEIN-文生图_2086265051199135746.json, 图片生成/文生图/FLUX2-Klein文生图_2039582984268943361.json, 图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json, 图片生成/文生图/Flux.2-Klein 文生图_2012020733546860545.json, 图片生成/文生图/Flux2 Klein 文生图_2012770598530846721.json, 图片生成/文生图/Flux2-Klein 9B文生图+ 提示词扩写_2012402078878011394.json, 图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json, 图片生成/文生图/建筑 室内 文字生成图片上传_2043882512698576897.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/FLUX2 Klein 文生图工作流_2091474310002200578.json、图片生成/文生图/FLUX2 klein-9B 【文生图】_2013859086563024897.json、图片生成/文生图/FLUX2 klein-9B 文生图_2013123316474716162.json、图片生成/文生图/FLUX2-KLEIN 4B快速文生图_2012166692574601217.json、图片生成/文生图/FLUX2-KLEIN-文生图_2086265051199135746.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
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
- `PrimitiveInt` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `ConditioningZeroOut` —— 6/12 个有
- `PlaySound|pysssss` —— 4/12 个有
- `CR SDXL Aspect Ratio` —— 2/12 个有
- `FluxResolutionNode` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `ImpactSwitch` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
