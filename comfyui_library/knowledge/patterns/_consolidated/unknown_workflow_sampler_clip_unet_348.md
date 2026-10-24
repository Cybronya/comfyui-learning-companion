---
name: unknown_workflow_sampler_clip_unet_348
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.959667
common_nodes: [CLIPTextEncode, ConstrainImage|pysssss, FluxGuidance, ImagePadForOutpaint, KSampler, LoadImage, RHHiddenNodes, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【保姆级】任意图片指定方向扩图，支持各种风格_1996770973594656770.json, 图片生成/图生图/【保姆级】任意图片指定方向扩图，支持各种风格_2050580205823115266.json, 图片生成/图生图/【保姆级】任意图片指定方向扩图，支持各种风格_2084122878726983682.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_348

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【保姆级】任意图片指定方向扩图，支持各种风格_1996770973594656770.json、图片生成/图生图/【保姆级】任意图片指定方向扩图，支持各种风格_2050580205823115266.json、图片生成/图生图/【保姆级】任意图片指定方向扩图，支持各种风格_2084122878726983682.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `FluxGuidance`
- `ImagePadForOutpaint`
- `KSampler`
- `LoadImage`
- `RHHiddenNodes`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 2/3 个有
- `CompressImages` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
