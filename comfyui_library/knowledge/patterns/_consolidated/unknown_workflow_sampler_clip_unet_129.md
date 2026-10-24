---
name: unknown_workflow_sampler_clip_unet_129
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.973
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ERNIE文心生图蒸馏版本VS原生版本_2044661245202141185.json, 图片生成/文生图/Erine满血版--文生图_2044756541005373442.json, 图片生成/文生图/Flux.2-Klein-文生图_2057389434856886274.json, 图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json, 图片生成/文生图/z-image-文生图_2041812350243704833.json, 图片生成/文生图/z-image-文生图_2059886095051087873.json, 图片生成/文生图/百度 ERNIE_Image 生图基础工作流_2044955952499134465.json, 图片生成/文生图/百度 ERNIE_Image 生图基础工作流_2045013148784136193.json, 图片生成/文生图/百度 ERNIE_Image 生图基础工作流_2045101296834846722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_129

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/ERNIE文心生图蒸馏版本VS原生版本_2044661245202141185.json、图片生成/文生图/Erine满血版--文生图_2044756541005373442.json、图片生成/文生图/Flux.2-Klein-文生图_2057389434856886274.json、图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json、图片生成/文生图/z-image-文生图_2041812350243704833.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 8/9 个有
- `EmptyFlux2LatentImage` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `LayerUtility: PurgeVRAM V2` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `EmptySD3LatentImage` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 9 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 36% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 0.6 | 0.4 - 0.8 | 4 | 67% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.4 - 0.8，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
