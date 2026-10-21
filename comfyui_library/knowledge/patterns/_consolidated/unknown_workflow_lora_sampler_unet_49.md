---
name: unknown_workflow_lora_sampler_unet_49
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.758667
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, ConstrainImage|pysssss, GetImageSize+]
members: [图片生成/图生图/2029756712529432577.json, 图片生成/图生图/2102275717336756225.json, 图片生成/文生图/Flux-Klein去除ai感优化光影效果去水印输入提示词_2071089227948969985.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2029756712529432577.json、图片生成/图生图/2102275717336756225.json、图片生成/文生图/Flux-Klein去除ai感优化光影效果去水印输入提示词_2071089227948969985.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DetailTransfer` —— 1/3 个有
- `ImageLoader` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、ConstrainImage|pysssss、GetImageSize+
