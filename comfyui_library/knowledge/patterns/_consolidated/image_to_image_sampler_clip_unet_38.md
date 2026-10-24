---
name: image_to_image_sampler_clip_unet_38
type: Image To Image
frequency: 9
level: weak
coverage: 0.970444
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2512真实人像质感御姐美女_2038803931576410113.json, 图片生成/图生图/Qwen2512真实人像质感御姐美女_2040669755073372161.json, 图片生成/图生图/Qwen2512真实人像质感御姐美女_2040674015815147522.json, 图片生成/图生图/Qwen_Image_Layerd加速分层图像【图生图】_2003447063511744514.json, 图片生成/图生图/Z-image-Base-基础洗图_2017239330523189249.json, 图片生成/图生图/Z-image-base-极速洗图_2021931573834158081.json, 图片生成/图生图/anima edit 2秒（提示词待优化）_2061288008342663170.json, 图片生成/图生图/psd生成器，Qwen+Layerd分层图像，生成带透明通道的图层，直接在ps使用，生成psd_2008809805498032129.json, 图片生成/图生图/新版psd生成器，Qwen+Layerd分层图像，生成带透明通道的图层，直接在ps使用，生成psd_2056225742748389377.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen2512真实人像质感御姐美女_2038803931576410113.json、图片生成/图生图/Qwen2512真实人像质感御姐美女_2040669755073372161.json、图片生成/图生图/Qwen2512真实人像质感御姐美女_2040674015815147522.json、图片生成/图生图/Qwen_Image_Layerd加速分层图像【图生图】_2003447063511744514.json、图片生成/图生图/Z-image-Base-基础洗图_2017239330523189249.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `EmptyHunyuanLatentVideo` —— 3/9 个有
- `LatentCutToBatch` —— 3/9 个有
- `Note _O` —— 3/9 个有
- `ReferenceLatent` —— 3/9 个有
- `scale` —— 3/9 个有
- `Float` —— 2/9 个有
- `ImpactInt` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `ApplyCosmosReferenceLatent` —— 1/9 个有
- `JWInteger` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 60% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 0.6 | 0.5 - 1 | 9 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.5 - 1，9 个样本
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
