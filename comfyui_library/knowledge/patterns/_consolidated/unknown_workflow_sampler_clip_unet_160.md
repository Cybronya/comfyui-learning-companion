---
name: unknown_workflow_sampler_clip_unet_160
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.939
common_nodes: [CLIPLoader, CLIPTextEncode, CustomAddLabel, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Fun- Lora-Distill-4步、8步对比工作流-20倍提速_2025134419132026881.json, 图片生成/文生图/Z-Image-Fun- Lora-Distill-4步工作流-20倍提速-高清放大_2025147553636950017.json, 图片生成/文生图/Z-Image-Fun- Lora-Distill-8步工作流-速度极快-高清放大_2025157935407570946.json, 图片生成/文生图/Z-image Base Meancache加速版-高清直出-质量高-速度快_2019623700148002818.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_160

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image-Fun- Lora-Distill-4步、8步对比工作流-20倍提速_2025134419132026881.json、图片生成/文生图/Z-Image-Fun- Lora-Distill-4步工作流-20倍提速-高清放大_2025147553636950017.json、图片生成/文生图/Z-Image-Fun- Lora-Distill-8步工作流-速度极快-高清放大_2025157935407570946.json、图片生成/文生图/Z-image Base Meancache加速版-高清直出-质量高-速度快_2019623700148002818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CustomAddLabel`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Int` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MeanCache_ZImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 4 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
