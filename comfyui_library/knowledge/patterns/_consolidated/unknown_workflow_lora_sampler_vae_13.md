---
name: unknown_workflow_lora_sampler_vae_13
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8918
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/洞洞鞋 拖鞋迁移换背景_2025502394594893826.json, 图片生成/图生图/真人转动漫人物 Qwen 2511_2072244143887306753.json, 图片生成/图生图/真人转动漫风格_2058356461167800322.json, 图片生成/图生图/真人转动漫风格_2090648180265414657.json, 图片生成/文生图/QWEN-edit-2509 万物融图 简单版 手动调节前景图位置 简单易用_2000388136918282241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/洞洞鞋 拖鞋迁移换背景_2025502394594893826.json、图片生成/图生图/真人转动漫人物 Qwen 2511_2072244143887306753.json、图片生成/图生图/真人转动漫风格_2058356461167800322.json、图片生成/图生图/真人转动漫风格_2090648180265414657.json、图片生成/文生图/QWEN-edit-2509 万物融图 简单版 手动调节前景图位置 简单易用_2000388136918282241.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 3/5 个有
- `Easy_QwenEdit2509` —— 2/5 个有
- `FastCanvas` —— 2/5 个有
- `FastCanvasTool` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: ImageAutoCrop V2` —— 2/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
