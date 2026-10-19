---
name: unknown_workflow_sampler_unet_vae_98
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.875714
common_nodes: [CLIPLoader, CR Text, EmptyLatentImage, ImpactInt, KSampler, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103024191862824962.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104858323886632961.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104860600273825794.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104862705957036034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_98

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103024191862824962.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104858323886632961.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `ImpactInt`
- `KSampler`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 6/7 个有
- `String Literal` —— 6/7 个有
- `孤海注释` —— 2/7 个有
- `Note Plus (mtb)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 50 | 50 - 50 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
