---
name: unknown_workflow_lora_sampler_clip_113
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.636667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SDXLEmptyLatentSizePicker+, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, Text Multiline, SDXLEmptyLatentSizePicker+, CR Prompt List, CR Upscale Image, easy promptConcat, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1966870624557731842.json, 图片生成/文生图/1968866874069065729.json, 图片生成/文生图/小说推文古风小说推文抖音超火_1991148887255920641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1966870624557731842.json、图片生成/文生图/1968866874069065729.json、图片生成/文生图/小说推文古风小说推文抖音超火_1991148887255920641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `RMBG` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `CR Upscale Image` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 3 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 832x1152 (0.72) | - | 3 | 67% |
| 高度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 最常用 832x1152 (0.72)，3 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Text Multiline、SDXLEmptyLatentSizePicker+、CR Prompt List、CR Upscale Image
