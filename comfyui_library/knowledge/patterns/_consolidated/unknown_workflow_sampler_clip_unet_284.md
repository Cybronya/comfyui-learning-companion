---
name: unknown_workflow_sampler_clip_unet_284
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8794
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【遇见AI】ernie-image-turbo文生图_2046172974834786305.json, 图片生成/文生图/【遇见AI】ernie-image文生图_2046172899383447554.json, 图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json, 图片生成/文生图/基础工作流系列14-百度ERNIE文生图工作流_2048740264847613954.json, 图片生成/文生图/更快 更强 支持中文 Z turbo_1993984068826103810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_284

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/【遇见AI】ernie-image-turbo文生图_2046172974834786305.json、图片生成/文生图/【遇见AI】ernie-image文生图_2046172899383447554.json、图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json、图片生成/文生图/基础工作流系列14-百度ERNIE文生图工作流_2048740264847613954.json、图片生成/文生图/更快 更强 支持中文 Z turbo_1993984068826103810.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 5 | 65% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 48% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
