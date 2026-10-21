---
name: text_to_image_sampler_clip_checkpoint_15
type: Text To Image
frequency: 4
level: moderate
coverage: 0.892
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxSamplerParams+, Int2String, KSampler, SaveImage, Seed_, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: [FluxSamplerParams+]
members: [图片生成/文生图/1946424512231694337.json, 图片生成/文生图/FLUX文生图工作流（大全）_2018211270519955457.json, 图片生成/文生图/FLUX文生图工作流（大全）_2064692790755422210.json, 图片生成/文生图/FLUX文生图工作流（大全）_2070669383806054402.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1946424512231694337.json、图片生成/文生图/FLUX文生图工作流（大全）_2018211270519955457.json、图片生成/文生图/FLUX文生图工作流（大全）_2064692790755422210.json、图片生成/文生图/FLUX文生图工作流（大全）_2070669383806054402.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
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
- `PreviewImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 2048 | 4 | 54% |
| 高度 | 1024 | 1024 - 3640 | 4 | 32% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 2048，4 个样本
- 高度 中位数 1024，观测区间 1024 - 3640，4 个样本，取值分散，一致性仅 32%
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：FluxSamplerParams+
