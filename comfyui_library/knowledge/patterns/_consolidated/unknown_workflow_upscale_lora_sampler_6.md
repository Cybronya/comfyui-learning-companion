---
name: unknown_workflow_upscale_lora_sampler_6
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.689
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SDXLEmptyLatentSizePicker+, SaveImage, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, Text Multiline, easy cleanGpuUsed, SDXLEmptyLatentSizePicker+, easy promptConcat]
members: [图片生成/文生图/1960893369214013442.json, 图片生成/文生图/1960894339947933698.json, 图片生成/文生图/1962119597363236866.json, 图片生成/文生图/1965258449992994817.json, 图片生成/文生图/1965638195176198145.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1960893369214013442.json、图片生成/文生图/1960894339947933698.json、图片生成/文生图/1962119597363236866.json、图片生成/文生图/1965258449992994817.json、图片生成/文生图/1965638195176198145.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/5 个有
- `CR Text Concatenate` —— 3/5 个有
- `ImageUpscaleWithModel` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `UltimateSDUpscale` —— 2/5 个有
- `SaveLatent` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 5 | 60% |
| 高度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 最常用 1024x1024 (1.0)，5 个样本，一致性 60%
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Text Multiline、easy cleanGpuUsed、SDXLEmptyLatentSizePicker+、easy promptConcat
