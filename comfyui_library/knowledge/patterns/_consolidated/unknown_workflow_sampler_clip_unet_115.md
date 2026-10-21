---
name: unknown_workflow_sampler_clip_unet_115
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.852667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux Klein 9b FP8 文生图 极简工作流_2015298868837093378.json, 图片生成/文生图/Flux-2-Klein-4B （文生图）_2011880923473645570.json, 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json, 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json, 图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json, 图片生成/文生图/Flux2-Klein 9B文生图+ 提示词扩写_2012402078878011394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Flux Klein 9b FP8 文生图 极简工作流_2015298868837093378.json、图片生成/文生图/Flux-2-Klein-4B （文生图）_2011880923473645570.json、图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json、图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json、图片生成/文生图/Flux.2-Klein 文生图-模板_2090689443601666049.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CFGGuider` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `BasicGuider` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `FluxResolutionNode` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `ModelPatchTorchSettings` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
