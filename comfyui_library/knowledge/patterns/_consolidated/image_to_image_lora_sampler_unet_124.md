---
name: image_to_image_lora_sampler_unet_124
type: Image To Image
frequency: 5
level: strong
coverage: 0.9116
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2画质提升+单图图片编辑(可添加风格lora)_2075197075234582529.json, 图片生成/图生图/Krea2画质提升+双图图片编辑(可添加风格lora)_2075197088782184450.json, 图片生成/图生图/MiniMaxH3-四视图-生成-模板_2089908477585084418.json, 图片生成/图生图/NO8D_Krea2_2090412463098519554.json, 图片生成/图生图/krea2 人像转角色设计图_2086649230344671233.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Krea2画质提升+单图图片编辑(可添加风格lora)_2075197075234582529.json、图片生成/图生图/Krea2画质提升+双图图片编辑(可添加风格lora)_2075197088782184450.json、图片生成/图生图/MiniMaxH3-四视图-生成-模板_2089908477585084418.json、图片生成/图生图/NO8D_Krea2_2090412463098519554.json、图片生成/图生图/krea2 人像转角色设计图_2086649230344671233.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `ZNGB_ResizeImage` —— 2/5 个有
- `> Scale Image to Side` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `easy pipeIn` —— 1/5 个有
- `easy pipeOut` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 14 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 14，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
