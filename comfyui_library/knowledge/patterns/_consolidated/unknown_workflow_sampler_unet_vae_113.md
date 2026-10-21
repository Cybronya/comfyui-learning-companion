---
name: unknown_workflow_sampler_unet_vae_113
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.902857
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json, 图片生成/文生图/Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json, 图片生成/文生图/Qwen image 2.1 文生图_2101796288126865410.json, 图片生成/文生图/Qwen image 2.1 文生图_2101863614746554369.json, 图片生成/文生图/Qwen image 2.1 文生图_2102294732612395009.json, 图片生成/文生图/QwenImage2.1-文生图_2101870210432200706.json, 图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_113

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json、图片生成/文生图/Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json、图片生成/文生图/Qwen image 2.1 文生图_2101796288126865410.json、图片生成/文生图/Qwen image 2.1 文生图_2101863614746554369.json、图片生成/文生图/Qwen image 2.1 文生图_2102294732612395009.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SaveImageAdvanced` —— 6/7 个有
- `CR Text` —— 3/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `Text` —— 2/7 个有
- `ImpactSwitch` —— 1/7 个有
- `QwenImage21BlockCacheT8` —— 1/7 个有
- `QwenImage21SageAttentionT8` —— 1/7 个有
- `QwenImage21SpectrumT8` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 45 | 25 - 50 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 45，观测区间 25 - 50，7 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
