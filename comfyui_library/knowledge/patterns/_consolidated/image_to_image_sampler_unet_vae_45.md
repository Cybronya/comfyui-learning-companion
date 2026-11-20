---
name: image_to_image_sampler_unet_vae_45
type: Image To Image
frequency: 3
level: strong
coverage: 0.732667
common_nodes: [ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, SaveImage, SetNode, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/1.tonnie-flux-美容_1992164436458926081.json, 图片生成/图生图/2.tonnie-flux-洗图+反推_1992162924227784705.json, 图片生成/图生图/3.tonnie-flux-redux洗图+反推_1992519039715004418.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_45

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/1.tonnie-flux-美容_1992164436458926081.json、图片生成/图生图/2.tonnie-flux-洗图+反推_1992162924227784705.json、图片生成/图生图/3.tonnie-flux-redux洗图+反推_1992519039715004418.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingFlux`
- `SaveImage`
- `SetNode`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `WD14Tagger|pysssss` —— 2/3 个有
- `ApplyPulidFlux` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `PulidFluxInsightFaceLoader` —— 1/3 个有
- `PulidFluxModelLoader` —— 1/3 个有
- `ReduxAdvanced` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.4 - 0.6 | 3 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.4 - 0.6，3 个样本，取值集中（一致性 82%）
