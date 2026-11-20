---
name: unknown_workflow_lora_sampler_clip_116
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9044
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json, 图片生成/文生图/kontext_dev+Lora基础文生图_1954834253982908418.json, 图片生成/文生图/kontext_dev基础文生图_1952701907708088321.json, 图片生成/文生图/工作流基础系列16-FLUX-Krea文生图工作流_2047554003969511425.json, 图片生成/文生图/极速4步采样生图——SoilsihgStudio_1895380500704002050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json、图片生成/文生图/kontext_dev+Lora基础文生图_1954834253982908418.json、图片生成/文生图/kontext_dev基础文生图_1952701907708088321.json、图片生成/文生图/工作流基础系列16-FLUX-Krea文生图工作流_2047554003969511425.json、图片生成/文生图/极速4步采样生图——SoilsihgStudio_1895380500704002050.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `PreviewImage` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `ModelSamplingFlux` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `TeaCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 5 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
