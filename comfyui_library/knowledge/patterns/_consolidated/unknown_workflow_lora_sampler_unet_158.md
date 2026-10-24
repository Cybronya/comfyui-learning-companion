---
name: unknown_workflow_lora_sampler_unet_158
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8815
common_nodes: [CLIPLoaderGGUF, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UnetLoaderGGUF, VAEDecode, VaeGGUF]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/02-单图生图_2043581952241967105.json, 图片生成/文生图/01-文生图_2034563277493116930.json, 图片生成/文生图/01-文生图_2042200070795304961.json, 图片生成/文生图/01-文生图新加速_2042830702382682114.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/02-单图生图_2043581952241967105.json、图片生成/文生图/01-文生图_2034563277493116930.json、图片生成/文生图/01-文生图_2042200070795304961.json、图片生成/文生图/01-文生图新加速_2042830702382682114.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VaeGGUF`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `AnyBooleanSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 800 - 1080 | 4 | 88% |
| 高度 | 1920 | 1280 - 1920 | 4 | 84% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 75% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 800 - 1080，4 个样本，取值集中（一致性 88%）
- 高度 中位数 1920，观测区间 1280 - 1920，4 个样本，取值集中（一致性 84%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
