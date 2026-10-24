---
name: unknown_workflow_sampler_clip_unet_136
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.961667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问文生图_1952243963510075394.json, 图片生成/文生图/千问文生图最新版工作流_2000925762351923202.json, 图片生成/文生图/千问文生图（中文海报直出）_1962714914005626881.json, 图片生成/文生图/原生z-image-turbo_2003323871308677121.json, 图片生成/文生图/国产之光-Qwen-Image 文生图 支持中英文生成-StarAI_1953162182935703553.json, 图片生成/文生图/微软-Lens VS Z Image 文生图工作流_2059584817586593793.json, 图片生成/文生图/文生图_2109550123767386113.json, 图片生成/文生图/更快 更强 支持中文 Z turbo_1993984068826103810.json, 图片生成/文生图/柔美手写字体一键直出 - 媲美即梦 - Qwen-Image文生图_1953769832510574594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/千问文生图_1952243963510075394.json、图片生成/文生图/千问文生图最新版工作流_2000925762351923202.json、图片生成/文生图/千问文生图（中文海报直出）_1962714914005626881.json、图片生成/文生图/原生z-image-turbo_2003323871308677121.json、图片生成/文生图/国产之光-Qwen-Image 文生图 支持中英文生成-StarAI_1953162182935703553.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

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
- `EmptySD3LatentImage` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `Int` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `FluxEmptyLatentSizePicker` —— 1/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `Text Find and Replace` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `Text String` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 8 - 35 | 9 | 46% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 9 | 44% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 832x1152 (0.96MP) - 3:4 | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 8 - 35，9 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，9 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
