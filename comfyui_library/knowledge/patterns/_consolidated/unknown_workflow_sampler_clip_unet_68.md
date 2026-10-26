---
name: unknown_workflow_sampler_clip_unet_68
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.973615
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ERNIE文心生图蒸馏版本VS原生版本_2044661245202141185.json, 图片生成/文生图/Erine满血版--文生图_2044756541005373442.json, 图片生成/文生图/FLUX2文生图_2038528285033897986.json, 图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json, 图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json, 图片生成/文生图/Flux-Kelin--文生图_2034949979520901121.json, 图片生成/文生图/Flux.2-Klein-文生图_2057389434856886274.json, 图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json, 图片生成/文生图/z-image-文生图_2041812350243704833.json, 图片生成/文生图/z-image-文生图_2059886095051087873.json, 图片生成/文生图/百度 ERNIE_Image 生图基础工作流_2044955952499134465.json, 图片生成/文生图/百度 ERNIE_Image 生图基础工作流_2045013148784136193.json, 图片生成/文生图/百度 ERNIE_Image 生图基础工作流_2045101296834846722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/ERNIE文心生图蒸馏版本VS原生版本_2044661245202141185.json、图片生成/文生图/Erine满血版--文生图_2044756541005373442.json、图片生成/文生图/FLUX2文生图_2038528285033897986.json、图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json、图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 11/13 个有
- `Seed (rgthree)` —— 8/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `LayerUtility: PurgeVRAM V2` —— 4/13 个有
- `LoraLoader` —— 4/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `EmptySD3LatentImage` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `MuyeTextEditOutput` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 50 | 13 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 28% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| LoRA 模型强度 | 0.6 | 0.4 - 0.8 | 4 | 67% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 50，13 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.4 - 0.8，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（11/13 个样本）：Steps较低可能导致细节不足
