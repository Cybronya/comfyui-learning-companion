---
name: image_to_image_sampler_clip_unet_143
type: Image To Image
frequency: 3
level: strong
coverage: 0.899667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Latent Input Switch, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2-klein-万物提取白底图_2081290693993132033.json, 图片生成/图生图/flux2-klein-人物动作九宫格_2080520633963859969.json, 图片生成/文生图/flux-2-klein-文生图+图生图单图多图工作流_2047155183376928770.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_143

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux2-klein-万物提取白底图_2081290693993132033.json、图片生成/图生图/flux2-klein-人物动作九宫格_2080520633963859969.json、图片生成/文生图/flux-2-klein-文生图+图生图单图多图工作流_2047155183376928770.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `SizeSelector` —— 2/3 个有
- `DimensionMultiplierNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `StringReplace` —— 1/3 个有
- `TextInputNode` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
