---
name: unknown_workflow_lora_sampler_clip_215
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.929667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Rebelance文生图V1_1981953788003139586.json, 图片生成/文生图/Qwen_文生图_fp8_官方版_1955386783511056385.json, 图片生成/文生图/高级人像质感 Qwen_Rebalance_1981042700025729026.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_215

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Rebelance文生图V1_1981953788003139586.json、图片生成/文生图/Qwen_文生图_fp8_官方版_1955386783511056385.json、图片生成/文生图/高级人像质感 Qwen_Rebalance_1981042700025729026.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `Replace Text _O` —— 2/3 个有
- `String` —— 2/3 个有
- `Text _O` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `easy textSwitch` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `EmptyUnitGenerator_UTK` —— 1/3 个有
- `OllamaGenerateAdvance` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PurgeVRAM_UTK` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextBoxNode_UTK` —— 1/3 个有
- `ThinkRemover_UTK` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
