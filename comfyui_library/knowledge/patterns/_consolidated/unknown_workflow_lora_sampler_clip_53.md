---
name: unknown_workflow_lora_sampler_clip_53
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.851
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [StringFunction|pysssss, CR Simple Prompt List, GlobalSeed //Inspire]
members: [图片生成/文生图/1967455683580923905.json, 图片生成/文生图/1967848816110088193.json, 图片生成/文生图/1981285976733638658.json, 图片生成/文生图/1984457132592480258.json, 图片生成/文生图/1985931273690591234.json, 图片生成/文生图/1987591657719836673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1967455683580923905.json、图片生成/文生图/1967848816110088193.json、图片生成/文生图/1981285976733638658.json、图片生成/文生图/1984457132592480258.json、图片生成/文生图/1985931273690591234.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextInput_` —— 2/6 个有
- `CR Simple Prompt List` —— 1/6 个有
- `GlobalSeed //Inspire` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `ShellAgentPluginInputText` —— 1/6 个有
- `ShellAgentPluginSaveImage` —— 1/6 个有
- `StringFunction|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 59% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、CR Simple Prompt List、GlobalSeed //Inspire
