---
name: unknown_workflow_sampler_unet_vae_78
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.816538
common_nodes: [BasicGuider, CLIPLoader, EmptyLatentImage, KSamplerSelect, ManualSigmas, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/QwenImage2.1-turbo-三图编辑-绘世专用工作流_2115535900909326338.json, 图片生成/图生图/QwenImage2.1-turbo-单图编辑-绘世专用工作流_2115517604566753282.json, 图片生成/图生图/QwenImage2.1-turbo-双图编辑-绘世专用工作流_2115535885277163522.json, 图片生成/图生图/QwenImage2.1-turbo-双图编辑-绘世专用工作流_2115601588973821954.json, 图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json, 图片生成/文生图/Qwen-image2.1文生图3D国漫CG风格_V2.0_2114972367574360065.json, 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_V2.0_2116592766540144641.json, 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_V2.0_2116708137842601985.json, 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_V2.0_2116722333204443138.json, 图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json, 图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json, 平台全量/QwenImage2.1-turbo-多图编辑-LoRA_2118169836537868289.json, 平台全量/QwenImage2.1-turbo-多图编辑_2117807215678672897.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_78

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/QwenImage2.1-turbo-三图编辑-绘世专用工作流_2115535900909326338.json、图片生成/图生图/QwenImage2.1-turbo-单图编辑-绘世专用工作流_2115517604566753282.json、图片生成/图生图/QwenImage2.1-turbo-双图编辑-绘世专用工作流_2115535885277163522.json、图片生成/图生图/QwenImage2.1-turbo-双图编辑-绘世专用工作流_2115601588973821954.json、图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `QwenImage21Cache`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `LoadImage` —— 8/13 个有
- `PrimitiveBoolean` —— 8/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `ResolutionSelector` —— 7/13 个有
- `PrimitiveInt` —— 6/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `easy showAnything` —— 5/13 个有
- `QwenImageLoraLoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1152 | 13 | 94% |
| 高度 | 1024 | 1024 - 2048 | 13 | 65% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1152，13 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 1024 - 2048，13 个样本
