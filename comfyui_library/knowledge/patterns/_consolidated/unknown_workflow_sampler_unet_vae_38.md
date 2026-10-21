---
name: unknown_workflow_sampler_unet_vae_38
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.869692
common_nodes: [CLIPLoader, CR Text, EmptyLatentImage, ImpactInt, KSampler, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102148485725376513.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103024191862824962.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104858323886632961.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104860600273825794.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104862705957036034.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2108032950725074946.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2108084813491167233.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2108474880806187009.json, 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2108477959433703426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102148485725376513.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103024191862824962.json、图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
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
- `CR Prompt List` —— 12/13 个有
- `String Literal` —— 12/13 个有
- `孤海注释` —— 4/13 个有
- `Note Plus (mtb)` —— 3/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1024 | 1024 - 1024 | 13 | 100% |
| 采样步数 | 50 | 50 - 50 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
