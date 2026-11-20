---
name: unknown_workflow_lora_sampler_clip_152
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9132
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/👾怪獸-千问漫画转真人👾_1984107523055779842.json, 图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json, 图片生成/文生图/qwen-image-2512工作流_2067229524982587394.json, 图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json, 图片生成/文生图/qwen-image文生图官方工作流_1953019372622311426.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/👾怪獸-千问漫画转真人👾_1984107523055779842.json、图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json、图片生成/文生图/qwen-image-2512工作流_2067229524982587394.json、图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json、图片生成/文生图/qwen-image文生图官方工作流_1953019372622311426.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `LoraLoader` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 30 | 5 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.19 - 1 | 5 | 61% |
| LoRA 模型强度 | 1.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 30，5 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.19 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
