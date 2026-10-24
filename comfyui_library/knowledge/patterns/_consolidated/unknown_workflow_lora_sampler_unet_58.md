---
name: unknown_workflow_lora_sampler_unet_58
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.858111
common_nodes: [CLIPLoader, CR Text, GetImageSize+, KSampler, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合015.去AI增加真实感_2035272359480922113.json, 图片生成/图生图/003.FLUX.2智能综合016.动漫转真人_2035273526944473089.json, 图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-011.FLUX.2-Klein 动漫转真人_2027047523076018178.json, 图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-012.FLUX.2-Klein去AI增加真实感_2027047541266714626.json, 图片生成/图生图/F2K万物迁移全能版｜产品｜颜色｜服装｜饰品｜光影迁移_2088535780623994881.json, 图片生成/图生图/Klein细节增强【脱离AI味 增加真实感】_2026580381029376001.json, 图片生成/图生图/图片细节恢复及放大 02_2033577021472776194.json, 图片生成/图生图/图片超强去AI味【Klein细节增强+增加真实感】_2039591122405691394.json, 图片生成/图生图/🐅Klein 动漫转真人🐅_2022832031020879874.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合015.去AI增加真实感_2035272359480922113.json、图片生成/图生图/003.FLUX.2智能综合016.动漫转真人_2035273526944473089.json、图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-011.FLUX.2-Klein 动漫转真人_2027047523076018178.json、图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-012.FLUX.2-Klein去AI增加真实感_2027047541266714626.json、图片生成/图生图/F2K万物迁移全能版｜产品｜颜色｜服装｜饰品｜光影迁移_2088535780623994881.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `GetImageSize+`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 8/9 个有
- `ImageStitch` —— 8/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `easy int` —— 6/9 个有
- `CR Text Concatenate` —— 5/9 个有
- `ImpactFloat` —— 5/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 12 | 9 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 12，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
