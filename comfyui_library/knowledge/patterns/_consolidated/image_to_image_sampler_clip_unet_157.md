---
name: image_to_image_sampler_clip_unet_157
type: Image To Image
frequency: 4
level: strong
coverage: 0.96825
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键洗图(Flux)_1994939269535948802.json, 图片生成/图生图/一键美容(Flux)_1984595236137680898.json, 平台全量/flux一键美容_1930518049332346882.json, 平台全量/flux洗图_1928434265808347138.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键洗图(Flux)_1994939269535948802.json、图片生成/图生图/一键美容(Flux)_1984595236137680898.json、平台全量/flux一键美容_1930518049332346882.json、平台全量/flux洗图_1928434265808347138.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingFlux`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `PulidFluxModelLoader` —— 2/4 个有
- `EcomIDEvaClipLoader` —— 1/4 个有
- `EcomIDFaceAnalysis` —— 1/4 个有
- `PulidEvaClipLoader` —— 1/4 个有
- `PulidFluxInsightFaceLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 0.59 | 0.5 - 0.7 | 4 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 0.59，观测区间 0.5 - 0.7，4 个样本，取值集中（一致性 84%）
