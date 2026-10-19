---
name: unknown_workflow_lora_sampler_clip_55
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.60925
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, ImpactInt, KSampler, LoraLoader, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Text Concatenate, Text Find and Replace, Text Load Line From File, Text Multiline, easy forLoopEnd, easy forLoopStart]
members: [图片生成/文生图/1948706172485414914.json, 图片生成/文生图/1949336324483031041.json, 图片生成/文生图/1949349633655545857.json, 图片生成/文生图/1950729804771430402.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1948706172485414914.json、图片生成/文生图/1949336324483031041.json、图片生成/文生图/1949349633655545857.json、图片生成/文生图/1950729804771430402.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `KSampler`
- `LoraLoader`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Text Find and Replace` —— 2/4 个有
- `Text Load Line From File` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.4 - 1 | 4 | 53% |
| LoRA 文本强度 | 0.4 | 0.4 - 1 | 4 | 53% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 100% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 1，4 个样本
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 1，4 个样本
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 100%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、Text Find and Replace、Text Load Line From File、Text Multiline
