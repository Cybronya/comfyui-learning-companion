---
name: unknown_workflow_sampler_checkpoint_vae_9
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9834
common_nodes: [CFGGuider, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, SaveImage, T8LLaDAImageCheckpointLoader, T8LLaDAImageScheduler, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/Llada Image Base VQ文生图_2096898925117657089.json, 图片生成/文生图/Llada Image Base文生图_2096898914665451522.json, 图片生成/文生图/Llada Image Turbo VQ文生图_2096898952783294465.json, 图片生成/文生图/Llada Image Turbo 文生图_2097314140187615233.json, 图片生成/文生图/Llada Image Turbo文生图_2096898945132879874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Llada Image Base VQ文生图_2096898925117657089.json、图片生成/文生图/Llada Image Base文生图_2096898914665451522.json、图片生成/文生图/Llada Image Turbo VQ文生图_2096898952783294465.json、图片生成/文生图/Llada Image Turbo 文生图_2097314140187615233.json、图片生成/文生图/Llada Image Turbo文生图_2096898945132879874.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T8LLaDAImageCheckpointLoader`
- `T8LLaDAImageScheduler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/5 个有
- `CR Prompt Text` —— 3/5 个有
- `T8SamplerLLaDAImageTurbo` —— 3/5 个有
- `KSamplerSelect` —— 2/5 个有
- `T8LLaDAImageVQConditioning` —— 2/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
