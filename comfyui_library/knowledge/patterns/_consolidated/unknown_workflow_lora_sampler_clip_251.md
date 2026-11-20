---
name: unknown_workflow_lora_sampler_clip_251
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.862667
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, ImpactInt, KSampler, LoraLoader, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949336324483031041.json, 图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949349633655545857.json, 平台全量/Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_251

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949336324483031041.json、图片生成/文生图/wan通义万相最强批量文生图写实工作流（直出2K且提示词优化）_1949349633655545857.json、平台全量/Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
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
- `RHHiddenNodes` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Text Find and Replace` —— 2/3 个有
- `Text Load Line From File` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有
- `ImpactSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.4 | 0.4 - 1 | 3 | 53% |
| LoRA 文本强度 | 0.4 | 0.4 - 1 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 1，3 个样本
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 1，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
