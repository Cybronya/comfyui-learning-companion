---
name: image_to_image_lora_sampler_unet_17
type: Image To Image
frequency: 5
level: strong
coverage: 0.8278
common_nodes: [CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [GetImageSize+, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2089356156211912706.json, 图片生成/图生图/2104374878999760898.json, 图片生成/文生图/Krea2-双图编辑_完美替换_2089961180281532417.json, 图片生成/文生图/Krea2-图片扩展_超乎你想象_2089999274397495298.json, 图片生成/文生图/Krea2-局部重绘_移除_2089978434125647873.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2089356156211912706.json、图片生成/图生图/2104374878999760898.json、图片生成/文生图/Krea2-双图编辑_完美替换_2089961180281532417.json、图片生成/文生图/Krea2-图片扩展_超乎你想象_2089999274397495298.json、图片生成/文生图/Krea2-局部重绘_移除_2089978434125647873.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 4/5 个有
- `DrawMaskOnImage` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：GetImageSize+、Seed (rgthree)、LayerUtility: ImageScaleByAspectRatio V2
