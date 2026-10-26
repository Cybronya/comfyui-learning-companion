---
name: unknown_workflow_lora_sampler_clip_165
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.67525
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyFlux2LatentImage, Flux2Scheduler, INTConstant, KSamplerSelect, Load Lora, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/kelin文生图_清新插画风格lora_2018877722025533441.json, 图片生成/文生图/kelin文生图_清新插画风格lora_2020376014404194305.json, 图片生成/文生图/klein文生图_手绘吉卜力风格lora一键出图_2019720294700687361.json, 图片生成/文生图/klein文生图_手绘吉卜力风格lora有原模型生图对比_2019693546772631553.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_165

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/kelin文生图_清新插画风格lora_2018877722025533441.json、图片生成/文生图/kelin文生图_清新插画风格lora_2020376014404194305.json、图片生成/文生图/klein文生图_手绘吉卜力风格lora一键出图_2019720294700687361.json、图片生成/文生图/klein文生图_手绘吉卜力风格lora有原模型生图对比_2019693546772631553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `INTConstant`
- `KSamplerSelect`
- `Load Lora`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
