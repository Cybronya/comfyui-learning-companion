---
name: unknown_workflow_lora_sampler_clip_154
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9694
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux图生图_2116132881838989314.json, 图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json, 图片生成/文生图/flux1_dev文生图_2059177447408627714.json, 图片生成/文生图/flux基础工作流-古琴_1935657646269595649.json, 图片生成/文生图/kontext_dev+Lora基础文生图_1954834253982908418.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux图生图_2116132881838989314.json、图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json、图片生成/文生图/flux1_dev文生图_2059177447408627714.json、图片生成/文生图/flux基础工作流-古琴_1935657646269595649.json、图片生成/文生图/kontext_dev+Lora基础文生图_1954834253982908418.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `TeaCache` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `VAELoader_Any` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 5 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
