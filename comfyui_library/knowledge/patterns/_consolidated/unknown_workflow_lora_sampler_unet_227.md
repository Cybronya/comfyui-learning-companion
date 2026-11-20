---
name: unknown_workflow_lora_sampler_unet_227
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.90825
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/洞洞鞋 拖鞋迁移换背景_2025502394594893826.json, 图片生成/图生图/真人转动漫人物 Qwen 2511_2072244143887306753.json, 图片生成/图生图/色块变泡泡_2010018737121927169.json, 平台全量/商用级 _ QwenEdit2509万物迁移+自动光影融合（最新修复版）_2002401677099560962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_227

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/洞洞鞋 拖鞋迁移换背景_2025502394594893826.json、图片生成/图生图/真人转动漫人物 Qwen 2511_2072244143887306753.json、图片生成/图生图/色块变泡泡_2010018737121927169.json、平台全量/商用级 _ QwenEdit2509万物迁移+自动光影融合（最新修复版）_2002401677099560962.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `LayerUtility: ImageAutoCrop V2` —— 2/4 个有
- `CR Simple Image Compare` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Int` —— 1/4 个有
- `MaskColorize` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
