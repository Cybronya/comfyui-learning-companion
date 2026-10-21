---
name: unknown_workflow_upscale_lora_sampler_25
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.627
common_nodes: [CLIPLoader, CLIPTextEncode, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SDXLEmptyLatentSizePicker+, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy promptConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, SDXLEmptyLatentSizePicker+, Upscale Model Loader, easy promptConcat]
members: [图片生成/文生图/1970684621732147201.json, 图片生成/文生图/1975850526229311490.json, 图片生成/文生图/1977868579548844034.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1970684621732147201.json、图片生成/文生图/1975850526229311490.json、图片生成/文生图/1977868579548844034.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageUpscaleWithModel`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 3 | 100% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，3 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、SDXLEmptyLatentSizePicker+、Upscale Model Loader、easy promptConcat
