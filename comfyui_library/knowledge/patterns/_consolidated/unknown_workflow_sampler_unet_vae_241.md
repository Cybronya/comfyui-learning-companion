---
name: unknown_workflow_sampler_unet_vae_241
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8715
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux3 Klein 提示词增强文生图_2112106153021890562.json, 图片生成/文生图/Flux3&多图编辑-加速版_2111293209782603777.json, 图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json, 图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_241

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux3 Klein 提示词增强文生图_2112106153021890562.json、图片生成/文生图/Flux3&多图编辑-加速版_2111293209782603777.json、图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json、图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `EmptyFlux2LatentImage` —— 2/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `QwenImage21Cache` —— 2/4 个有
- `TextEncodeQwenImage21` —— 2/4 个有
- `ReferenceMultiLatent` —— 1/4 个有
- `TextGenerate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
