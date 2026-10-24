---
name: text_to_image_sampler_clip_checkpoint_16
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9104
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, FluxSamplerParams+, Int2String, KSampler, SaveImage, Seed_, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX文生图工作流（大全）_1946424512231694337.json, 图片生成/文生图/FLUX文生图工作流（大全）_2018211270519955457.json, 图片生成/文生图/FLUX文生图工作流（大全）_2064692790755422210.json, 图片生成/文生图/FLUX文生图工作流（大全）_2070669383806054402.json, 图片生成/文生图/基础FLUX_2048354576142704641.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX文生图工作流（大全）_1946424512231694337.json、图片生成/文生图/FLUX文生图工作流（大全）_2018211270519955457.json、图片生成/文生图/FLUX文生图工作流（大全）_2064692790755422210.json、图片生成/文生图/FLUX文生图工作流（大全）_2070669383806054402.json、图片生成/文生图/基础FLUX_2048354576142704641.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSamplerParams+`
- `Int2String`
- `KSampler`
- `SaveImage`
- `Seed_`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `PreviewImage` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 2048 | 5 | 53% |
| 高度 | 1024 | 1024 - 3640 | 5 | 32% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 2048，5 个样本
- 高度 中位数 1024，观测区间 1024 - 3640，5 个样本，取值分散，一致性仅 32%
- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
