---
name: unknown_workflow_sampler_unet_vae_251
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.81175
common_nodes: [CLIPLoader, EmptyLatentImage, KSamplerSelect, ManualSigmas, QwenImage21Cache, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json, 图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json, 图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json, 图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_251

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json、图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json、图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json、图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `QwenImage21Cache`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `CFGGuider` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `TextGenerate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
