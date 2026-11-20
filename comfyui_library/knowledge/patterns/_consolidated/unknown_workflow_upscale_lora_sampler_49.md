---
name: unknown_workflow_upscale_lora_sampler_49
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92525
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426.json, 图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json, 图片生成/文生图/Qwen八步生图+SPRO洗图+Wan2.2洗图+对比展示_1988050506423668737.json, 图片生成/文生图/Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426.json、图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json、图片生成/文生图/Qwen八步生图+SPRO洗图+Wan2.2洗图+对比展示_1988050506423668737.json、图片生成/文生图/Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `EmptySD3LatentImage` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `TextInputBasic` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.35 - 1 | 4 | 66% |
| LoRA 模型强度 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| LoRA 文本强度 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，4 个样本
- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
