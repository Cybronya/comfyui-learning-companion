---
name: unknown_workflow_lora_sampler_clip_219
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.903
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen千问文生图+Z-image真实感洗图_1994294742995369986.json, 图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json, 图片生成/文生图/千问文生图+Z-image增强真实感强强联合_1993897697482571778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_219

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen千问文生图+Z-image真实感洗图_1994294742995369986.json、图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json、图片生成/文生图/千问文生图+Z-image增强真实感强强联合_1993897697482571778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `LoraLoader` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.19 - 0.4 | 3 | 70% |
| LoRA 模型强度 | 1.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.19 - 0.4，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
