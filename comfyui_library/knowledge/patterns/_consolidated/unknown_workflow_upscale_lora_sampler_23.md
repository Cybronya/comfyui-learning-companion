---
name: unknown_workflow_upscale_lora_sampler_23
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.866
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, Image Comparer (rgthree), Image Tiled, ImageConcanateOfUtils, ImageFromBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoraLoader, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text, Image Tiled]
members: [图片生成/文生图/1952618606662234114.json, 图片生成/文生图/1953397505272807426.json, 图片生成/文生图/1953719913837985794.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1952618606662234114.json、图片生成/文生图/1953397505272807426.json、图片生成/文生图/1953719913837985794.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.4 - 0.7 | 3 | 72% |
| LoRA 文本强度 | 0.4 | 0.4 - 0.7 | 3 | 72% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 0.7，3 个样本
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 0.7，3 个样本
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Image Tiled
