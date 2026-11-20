---
name: image_to_image_sampler_clip_checkpoint_6
type: Image To Image
frequency: 5
level: strong
coverage: 0.7046
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/Alan测-图生图（Z-image-AIO）真实感拉满轻松洗图+N_2046221451795111937.json, 图片生成/图生图/QT105-图生图（Z-image-AIO）真实感拉满轻松洗图+N_2033156077625286658.json, 图片生成/图生图/Qwen3VL-反推洗图_2075824889159831554.json, 图片生成/图生图/Redzimage AIO洗图高清_2062139306625556482.json, 图片生成/图生图/z-image真实感洗图_2009946001653633026.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Alan测-图生图（Z-image-AIO）真实感拉满轻松洗图+N_2046221451795111937.json、图片生成/图生图/QT105-图生图（Z-image-AIO）真实感拉满轻松洗图+N_2033156077625286658.json、图片生成/图生图/Qwen3VL-反推洗图_2075824889159831554.json、图片生成/图生图/Redzimage AIO洗图高清_2062139306625556482.json、图片生成/图生图/z-image真实感洗图_2009946001653633026.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `PlaySound|pysssss` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.9 | 0.65 - 0.9 | 5 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.65 - 0.9，5 个样本，取值集中（一致性 88%）
