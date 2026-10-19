---
name: unknown_workflow_sampler_checkpoint_vae_18
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.846
common_nodes: [CFGGuider, FluxKontextImageScale, LoadImage, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, T8LLaDAImageCheckpointLoader, T8LLaDAImageEditConditioning, T8LLaDAImageScheduler, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/2097527631431421954.json, 图片生成/图生图/2097527825980026881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2097527631431421954.json、图片生成/图生图/2097527825980026881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `FluxKontextImageScale`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T8LLaDAImageCheckpointLoader`
- `T8LLaDAImageEditConditioning`
- `T8LLaDAImageScheduler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 1/2 个有
- `T8SamplerLLaDAImageTurbo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
