---
name: image_to_image_lora_sampler_clip_32
type: Image To Image
frequency: 8
level: weak
coverage: 0.96675
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2512真实人像质感御姐美女_2038803931576410113.json, 图片生成/图生图/Qwen2512真实人像质感御姐美女_2040669755073372161.json, 图片生成/图生图/Qwen2512真实人像质感御姐美女_2040674015815147522.json, 图片生成/图生图/Qwen_Image_Layerd加速分层图像【图生图】_2003447063511744514.json, 图片生成/图生图/Z-image-base-极速洗图_2021931573834158081.json, 图片生成/图生图/anima edit 2秒（提示词待优化）_2061288008342663170.json, 图片生成/图生图/psd生成器，Qwen+Layerd分层图像，生成带透明通道的图层，直接在ps使用，生成psd_2008809805498032129.json, 图片生成/图生图/新版psd生成器，Qwen+Layerd分层图像，生成带透明通道的图层，直接在ps使用，生成psd_2056225742748389377.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen2512真实人像质感御姐美女_2038803931576410113.json、图片生成/图生图/Qwen2512真实人像质感御姐美女_2040669755073372161.json、图片生成/图生图/Qwen2512真实人像质感御姐美女_2040674015815147522.json、图片生成/图生图/Qwen_Image_Layerd加速分层图像【图生图】_2003447063511744514.json、图片生成/图生图/Z-image-base-极速洗图_2021931573834158081.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `EmptyHunyuanLatentVideo` —— 3/8 个有
- `LatentCutToBatch` —— 3/8 个有
- `Note _O` —— 3/8 个有
- `ReferenceLatent` —— 3/8 个有
- `scale` —— 3/8 个有
- `Float` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `ApplyCosmosReferenceLatent` —— 1/8 个有
- `JWInteger` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 50 | 8 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 0.775 | 0.5 - 1 | 8 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 50，8 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 0.775，观测区间 0.5 - 1，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
