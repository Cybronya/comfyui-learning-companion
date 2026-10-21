---
name: unknown_workflow_sampler_clip_unet_135
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7268
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/kelin文生图_清新插画风格lora_2018877722025533441.json, 图片生成/文生图/kelin文生图_清新插画风格lora_2020376014404194305.json, 图片生成/文生图/klein文生图_手绘吉卜力风格lora一键出图_2019720294700687361.json, 图片生成/文生图/klein文生图_手绘吉卜力风格lora有原模型生图对比_2019693546772631553.json, 图片生成/文生图/珠宝文生效果图_2102930912613847041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/kelin文生图_清新插画风格lora_2018877722025533441.json、图片生成/文生图/kelin文生图_清新插画风格lora_2020376014404194305.json、图片生成/文生图/klein文生图_手绘吉卜力风格lora一键出图_2019720294700687361.json、图片生成/文生图/klein文生图_手绘吉卜力风格lora有原模型生图对比_2019693546772631553.json、图片生成/文生图/珠宝文生效果图_2102930912613847041.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CR Prompt Text` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `Load Lora` —— 4/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
