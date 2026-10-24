---
name: image_to_image_lora_sampler_checkpoint_9
type: Image To Image
frequency: 3
level: strong
coverage: 0.886333
common_nodes: [Anything Everywhere3, CheckpointLoaderSimple, ImageResize+, Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, SeedVR2, SeedVR2BlockSwap, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, ZML_SwitchOutput]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/v19q_2017200654959255553.json, 图片生成/图生图/自用修图_2015717591909666818.json, 图片生成/图生图/自用修图v5.2-23_2016519083302330369.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/v19q_2017200654959255553.json、图片生成/图生图/自用修图_2015717591909666818.json、图片生成/图生图/自用修图v5.2-23_2016519083302330369.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CheckpointLoaderSimple`
- `ImageResize+`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `ZML_SwitchOutput`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 2/3 个有
- `LamSaveOnly` —— 1/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 67% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
