---
name: unknown_workflow_sampler_clip_unet_237
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.921
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image Base Meancache加速版-高清直出-质量高-速度快_2019623700148002818.json, 图片生成/文生图/Z-image Base Meancache加速版V1_2019064610539704322.json, 图片生成/文生图/Z-image Base Meancache加速版（好用质量高）_2019220127853580289.json, 图片生成/文生图/Z-image-base文生图_2017123904447320065.json, 图片生成/文生图/z_image_turbo_飞速写实文生图_1994300683828527106.json, 图片生成/文生图/极致写实-Z-image-base-文生图_2017086284610670594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_237

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-image Base Meancache加速版-高清直出-质量高-速度快_2019623700148002818.json、图片生成/文生图/Z-image Base Meancache加速版V1_2019064610539704322.json、图片生成/文生图/Z-image Base Meancache加速版（好用质量高）_2019220127853580289.json、图片生成/文生图/Z-image-base文生图_2017123904447320065.json、图片生成/文生图/z_image_turbo_飞速写实文生图_1994300683828527106.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CR Prompt Text` —— 3/6 个有
- `CustomAddLabel` —— 3/6 个有
- `Label (rgthree)` —— 3/6 个有
- `MeanCache_ZImage` —— 3/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `SeedVR2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 9 - 50 | 6 | 65% |
| Prompt 约束强度(CFG) | 3.25 | 1 - 4 | 6 | 63% |
| 采样算法 | res_multistep | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 9 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 1 - 4，6 个样本
- 采样算法 最常用 res_multistep，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
