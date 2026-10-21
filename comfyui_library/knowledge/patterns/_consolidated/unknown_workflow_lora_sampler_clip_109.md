---
name: unknown_workflow_lora_sampler_clip_109
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.918667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt List]
members: [图片生成/文生图/1955973376605126657.json, 图片生成/文生图/Qwen 文生图(二次元)_2057795247358435330.json, 图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1955973376605126657.json、图片生成/文生图/Qwen 文生图(二次元)_2057795247358435330.json、图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Prompt List` —— 2/3 个有
- `Text` —— 2/3 个有
- `IndexTTSNode` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 30 | 3 | 29% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 3 | 51% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 30，3 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt List
