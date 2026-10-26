---
name: image_to_image_sampler_clip_unet_58
type: Image To Image
frequency: 7
level: moderate
coverage: 0.832571
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Layerd分层图【图生图版】【美工利器】_2002985926773075969.json, 图片生成/图生图/Qwen Layered图像分层v1_2003006409304358914.json, 图片生成/图生图/Qwen-Image-Layered 最新分层式生图（图生图）_2002559034429435906.json, 图片生成/图生图/Qwen-Image-Layered_2004923156139831298.json, 图片生成/图生图/电商图片分层_2109177659312918529.json, 图片生成/图生图/🐠Qwen Layerd分层图像生成【图生图版】【美工利器】🐠_2002369743199846401.json, 图片生成/文生图/Qwen Layered 加强版_2073294146231685121.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Layerd分层图【图生图版】【美工利器】_2002985926773075969.json、图片生成/图生图/Qwen Layered图像分层v1_2003006409304358914.json、图片生成/图生图/Qwen-Image-Layered 最新分层式生图（图生图）_2002559034429435906.json、图片生成/图生图/Qwen-Image-Layered_2004923156139831298.json、图片生成/图生图/电商图片分层_2109177659312918529.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `AILab_QwenVL` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `Int` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `easy int` —— 3/7 个有
- `PreviewAny` —— 2/7 个有
- `AILab_ImageResize` —— 1/7 个有
- `EmptyQwenImageLayeredLatentImage` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `ShowText` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 7 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 55% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
