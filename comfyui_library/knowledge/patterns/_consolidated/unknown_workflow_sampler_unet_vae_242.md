---
name: unknown_workflow_sampler_unet_vae_242
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.922
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, ManualSigmas, MiniMaxLowVRAMAttention, PathchSageAttentionKJ, QwenImage21Cache, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen2.1_Turbo8_加速-图生图_2110563208288366593.json, 图片生成/图生图/Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977.json, 图片生成/文生图/Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746.json, 图片生成/文生图/Qwen2.1_Turbo8_加速-文生图_2110563232632107010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_242

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2.1_Turbo8_加速-图生图_2110563208288366593.json、图片生成/图生图/Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977.json、图片生成/文生图/Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746.json、图片生成/文生图/Qwen2.1_Turbo8_加速-文生图_2110563232632107010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `ManualSigmas`
- `MiniMaxLowVRAMAttention`
- `PathchSageAttentionKJ`
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
- `EmptyLatentImage` —— 2/4 个有
- `ImageCompare` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1376 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1376，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
