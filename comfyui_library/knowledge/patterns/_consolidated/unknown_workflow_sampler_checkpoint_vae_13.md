---
name: unknown_workflow_sampler_checkpoint_vae_13
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78
common_nodes: [CFGGuider, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, T8LLaDAImageCheckpointLoader, T8LLaDAImageScheduler, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/2097527631431421954.json, 图片生成/图生图/2097527825980026881.json, 图片生成/文生图/LLaDA-Image Base VQ文生图·VQ编码高保真_2097528015889719297.json, 图片生成/文生图/LLaDA-Image Turbo VQ文生图·极速VQ编码_2097528202888568834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2097527631431421954.json、图片生成/图生图/2097527825980026881.json、图片生成/文生图/LLaDA-Image Base VQ文生图·VQ编码高保真_2097528015889719297.json、图片生成/文生图/LLaDA-Image Turbo VQ文生图·极速VQ编码_2097528202888568834.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T8LLaDAImageCheckpointLoader`
- `T8LLaDAImageScheduler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `T8LLaDAImageEditConditioning` —— 2/4 个有
- `T8LLaDAImageVQConditioning` —— 2/4 个有
- `T8SamplerLLaDAImageTurbo` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
