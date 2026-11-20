---
name: unknown_workflow_sampler_checkpoint_vae_12
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.94075
common_nodes: [CFGGuider, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, T8LLaDAImageCheckpointLoader, T8LLaDAImageEditConditioning, T8LLaDAImageScheduler, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/LLaDA-Image Base图像编辑·一句话改图_2097527631431421954.json, 图片生成/图生图/LLaDA-Image Turbo四步图像编辑·极速改图_2097527825980026881.json, 图片生成/图生图/LLaDA-Image-图像编辑-全扩散架构_2098233557859782657.json, 图片生成/图生图/LLaDA-Image文字替换工作流_2099392238013997058.json, 图片生成/图生图/LLada Image Turbo 4步图像编辑_2096898936022851585.json, 图片生成/图生图/LLada-Image-Turbo 4步图像编辑_2097594945153622017.json, 图片生成/图生图/Llada Image Base图像编辑_2096898880368635906.json, 图片生成/图生图/Llada-Image 图像编辑基础版_2097590607677050882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/LLaDA-Image Base图像编辑·一句话改图_2097527631431421954.json、图片生成/图生图/LLaDA-Image Turbo四步图像编辑·极速改图_2097527825980026881.json、图片生成/图生图/LLaDA-Image-图像编辑-全扩散架构_2098233557859782657.json、图片生成/图生图/LLaDA-Image文字替换工作流_2099392238013997058.json、图片生成/图生图/LLada Image Turbo 4步图像编辑_2096898936022851585.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T8LLaDAImageCheckpointLoader`
- `T8LLaDAImageEditConditioning`
- `T8LLaDAImageScheduler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 7/8 个有
- `CR Prompt Text` —— 5/8 个有
- `KSamplerSelect` —— 5/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `T8SamplerLLaDAImageTurbo` —— 3/8 个有
- `PrimitiveInt` —— 2/8 个有
- `CR Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
