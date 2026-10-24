---
name: unknown_workflow_sampler_clip_unet_267
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9218
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image Base Meancache加速版-高清直出-质量高-速度快_2019623700148002818.json, 图片生成/文生图/Z-image Base Meancache加速版V1_2019064610539704322.json, 图片生成/文生图/Z-image Base Meancache加速版（好用质量高）_2019220127853580289.json, 图片生成/文生图/Z-image-base文生图_2017123904447320065.json, 图片生成/文生图/极致写实-Z-image-base-文生图_2017086284610670594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_267

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image Base Meancache加速版-高清直出-质量高-速度快_2019623700148002818.json、图片生成/文生图/Z-image Base Meancache加速版V1_2019064610539704322.json、图片生成/文生图/Z-image Base Meancache加速版（好用质量高）_2019220127853580289.json、图片生成/文生图/Z-image-base文生图_2017123904447320065.json、图片生成/文生图/极致写实-Z-image-base-文生图_2017086284610670594.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/5 个有
- `CustomAddLabel` —— 3/5 个有
- `MeanCache_ZImage` —— 3/5 个有
- `Label (rgthree)` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `SeedVR2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 2.5 - 4 | 5 | 78% |
| 采样算法 | res_multistep | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 2.5 - 4，5 个样本
- 采样算法 最常用 res_multistep，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
