---
name: unknown_workflow_upscale_lora_sampler_26
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.844333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Text Concatenate, Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1973197627275784193.json, 图片生成/文生图/1988050506423668737.json, 图片生成/文生图/1988095557270937601.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1973197627275784193.json、图片生成/文生图/1988050506423668737.json、图片生成/文生图/1988095557270937601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.35 - 1 | 3 | 61% |
| LoRA 模型强度 | 0.7 | - | 2 | 100% |
| LoRA 文本强度 | 0.7 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，3 个样本
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、Text Concatenate、Text Multiline、CR SDXL Aspect Ratio
