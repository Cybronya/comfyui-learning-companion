---
name: unknown_workflow_sampler_checkpoint_vae_17
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.786833
common_nodes: [CFGGuider, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, SaveImage, T8LLaDAImageCheckpointLoader, T8LLaDAImageScheduler, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/LLaDA-Image Base VQ文生图·VQ编码高保真_2097528015889719297.json, 图片生成/文生图/LLaDA-Image Base文生图·高保真图像生成_2097527015002955777.json, 图片生成/文生图/LLaDA-Image Turbo VQ文生图·极速VQ编码_2097528202888568834.json, 图片生成/文生图/LLaDA-Image Turbo极速文生图·4步出图_2097527440242466817.json, 图片生成/文生图/LLaDA-Image-Turbo-4步-文生图_2098231001439887361.json, 图片生成/文生图/Llada Image Turbo 文生图_2097314140187615233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/LLaDA-Image Base VQ文生图·VQ编码高保真_2097528015889719297.json、图片生成/文生图/LLaDA-Image Base文生图·高保真图像生成_2097527015002955777.json、图片生成/文生图/LLaDA-Image Turbo VQ文生图·极速VQ编码_2097528202888568834.json、图片生成/文生图/LLaDA-Image Turbo极速文生图·4步出图_2097527440242466817.json、图片生成/文生图/LLaDA-Image-Turbo-4步-文生图_2098231001439887361.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T8LLaDAImageCheckpointLoader`
- `T8LLaDAImageScheduler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `T8SamplerLLaDAImageTurbo` —— 4/6 个有
- `KSamplerSelect` —— 2/6 个有
- `T8LLaDAImageVQConditioning` —— 2/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
