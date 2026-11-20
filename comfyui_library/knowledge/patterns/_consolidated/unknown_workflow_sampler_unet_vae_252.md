---
name: unknown_workflow_sampler_unet_vae_252
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8645
common_nodes: [CLIPLoader, EmptyLatentImage, KSamplerSelect, ManualSigmas, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json, 图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json, 图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json, 图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_252

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json、图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json、图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json、图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `SamplerCustom` —— 3/4 个有
- `TextGenerateLTX2Prompt` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `BasicGuider` —— 1/4 个有
- `QwenImage21Cache` —— 1/4 个有
- `RandomNoise` —— 1/4 个有
- `SamplerCustomAdvanced` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1152 | 4 | 95% |
| 高度 | 1024 | 1024 - 2048 | 4 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1152，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 2048，4 个样本
