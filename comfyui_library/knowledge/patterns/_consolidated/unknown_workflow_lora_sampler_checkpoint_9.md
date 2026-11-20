---
name: unknown_workflow_lora_sampler_checkpoint_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.838
common_nodes: [CR Prompt Text, CheckpointLoaderSimple, ConditioningZeroOut, DifferentialDiffusion, JWStringConcat, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, Qwen3_VQA, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, easy clearCacheAll, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一致性 分镜 模特套图 多场景 多视角 Qwen3VL Next Scene_2034084447141761026.json, 图片生成/图生图/自动分镜v1_2015336738490687490.json, 图片生成/图生图/🦖Qwen3VL+Next Scene（自动分镜）_2010592088135573505.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物一致性 分镜 模特套图 多场景 多视角 Qwen3VL Next Scene_2034084447141761026.json、图片生成/图生图/自动分镜v1_2015336738490687490.json、图片生成/图生图/🦖Qwen3VL+Next Scene（自动分镜）_2010592088135573505.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `JWStringConcat`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `Qwen3_VQA`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `easy clearCacheAll`
- `easy promptLine`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
