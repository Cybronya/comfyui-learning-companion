---
name: image_to_image_sampler_clip_unet_154
type: Image To Image
frequency: 4
level: moderate
coverage: 0.84525
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2-klein-万物提取白底图_2081290693993132033.json, 图片生成/图生图/flux2-klein-人物动作九宫格_2080520633963859969.json, 图片生成/图生图/全能图片2.0+Z-Image图生图（细节增强版）_2033800127114125314.json, 图片生成/文生图/flux-2-klein-文生图+图生图单图多图工作流_2047155183376928770.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux2-klein-万物提取白底图_2081290693993132033.json、图片生成/图生图/flux2-klein-人物动作九宫格_2080520633963859969.json、图片生成/图生图/全能图片2.0+Z-Image图生图（细节增强版）_2033800127114125314.json、图片生成/文生图/flux-2-klein-文生图+图生图单图多图工作流_2047155183376928770.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Input Switch` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `SizeSelector` —— 2/4 个有
- `DimensionMultiplierNode` —— 1/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/4 个有
- `StringReplace` —— 1/4 个有
- `TextInputNode` —— 1/4 个有
- `easy imageColorMatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 10 | 4 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.2 - 1 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
