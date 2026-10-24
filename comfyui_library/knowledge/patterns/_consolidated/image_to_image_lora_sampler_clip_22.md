---
name: image_to_image_lora_sampler_clip_22
type: Image To Image
frequency: 9
level: weak
coverage: 0.894778
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LatentCutToBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(10倍加速版)Qwen Layerd分层图像图生图_2002222132568440833.json, 图片生成/图生图/(10倍加速版)Qwen Layerd分层图像图生图_2004883562950258689.json, 图片生成/图生图/01-12-01-QwenImage-Qwen-Layerd分层图像图生图_2004832173045805058.json, 图片生成/图生图/65.tonnie-layered图像分层（效果不好）_2009437356616585218.json, 图片生成/图生图/PSD生成器，Qwen+Layerd分层图像，直接在PS使用，生成psd_2061362779352817665.json, 图片生成/图生图/Qwen Image Layerd 图像智能分层（加速版）｜保存PSD_2091058647039307777.json, 图片生成/图生图/Qwen Image Layerd 图像智能分层（加速版）｜保存PSD_2110550275323949057.json, 图片生成/图生图/Qwen Layerd-图生图-分层（加速版）_2002729003507150850.json, 图片生成/图生图/（PSD分层）Qwen Image Layerd 图像智能分层（加速版）｜保存PSD_2111802213214547970.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/(10倍加速版)Qwen Layerd分层图像图生图_2002222132568440833.json、图片生成/图生图/(10倍加速版)Qwen Layerd分层图像图生图_2004883562950258689.json、图片生成/图生图/01-12-01-QwenImage-Qwen-Layerd分层图像图生图_2004832173045805058.json、图片生成/图生图/65.tonnie-layered图像分层（效果不好）_2009437356616585218.json、图片生成/图生图/PSD生成器，Qwen+Layerd分层图像，直接在PS使用，生成psd_2061362779352817665.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LatentCutToBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 8/9 个有
- `MathExpression|pysssss` —— 8/9 个有
- `Float` —— 4/9 个有
- `ImpactInt` —— 4/9 个有
- `Int` —— 4/9 个有
- `JWInteger` —— 4/9 个有
- `HAIGC_CombineUnits` —— 3/9 个有
- `HAIGC_Layer` —— 3/9 个有
- `HAIGC_SavePSD` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `EmptyHunyuanVideo15Latent` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `LatentFromBatch` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 9 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 29% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（5/9 个样本）：Steps较低可能导致细节不足
