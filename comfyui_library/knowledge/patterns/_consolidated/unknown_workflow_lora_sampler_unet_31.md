---
name: unknown_workflow_lora_sampler_unet_31
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.848571
common_nodes: [CLIPLoader, CR Prompt Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2KleinEditTextEncode_EditUtils, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Klein自动换装一致性强_2054482149025296386.json, 图片生成/图生图/F.2Klein自动换装一致性强_2057732864199970817.json, 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2053780349318115330.json, 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2056207288049913858.json, 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2057630170105864194.json, 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2058141247566606337.json, 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2058378118825594881.json, 图片生成/图生图/Flux+2+Klein全自动换头换脸_2016496929932316674.json, 图片生成/图生图/Flux+2+Klein换装，一致性强_2016528431097319425.json, 图片生成/图生图/Flux2 Klein 超强换头换脸保持一致性_2031951766127906818.json, 图片生成/图生图/Flux2Klein模特换头一致性_2048606266485907457.json, 图片生成/图生图/Flux2Klein模特换头换脸一致性_2051141990913462274.json, 图片生成/图生图/Flux2Klein自动换装一致性强_2042957317364260865.json, 图片生成/图生图/kelin 换头_2071892281627594754.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/F.2Klein自动换装一致性强_2054482149025296386.json、图片生成/图生图/F.2Klein自动换装一致性强_2057732864199970817.json、图片生成/图生图/F.2Klein超强换头换脸保持一致性_2053780349318115330.json、图片生成/图生图/F.2Klein超强换头换脸保持一致性_2056207288049913858.json、图片生成/图生图/F.2Klein超强换头换脸保持一致性_2057630170105864194.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2KleinEditTextEncode_EditUtils`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/14 个有
- `RMBG` —— 7/14 个有
- `ImpactInt` —— 6/14 个有
- `LoadRembgByBiRefNetModel` —— 6/14 个有
- `RembgByBiRefNet` —— 6/14 个有
- `SolidMask` —— 6/14 个有
- `easy ifElse` —— 6/14 个有
- `easy isMaskEmpty` —— 6/14 个有
- `ClothesSegment` —— 2/14 个有
- `easy imageConcat` —— 2/14 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/14 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 14 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，14 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
