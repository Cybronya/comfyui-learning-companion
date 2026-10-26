---
name: image_to_image_sampler_clip_vae_19
type: Image To Image
frequency: 10
level: strong
coverage: 0.9941
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/超强去水印工作流Kontext_2095027681485217794.json, 图片生成/文生图/kontextNunchakuDev转绘低多边形风格_1940245828193927170.json, 图片生成/文生图/kontextNunchakuDev转绘动漫_1940236757055000577.json, 图片生成/文生图/kontextNunchakuDev转绘奇幻艺术_1940240607094722562.json, 图片生成/文生图/kontextNunchakuDev转绘工艺粘土风_1940239181278826498.json, 图片生成/文生图/kontextNunchakuDev转绘模拟电影_1940235010588758018.json, 图片生成/文生图/kontextNunchakuDev转绘漫画_1940238028432654337.json, 图片生成/文生图/kontextNunchakuDev转绘电影感风_1940230026011000833.json, 图片生成/文生图/kontextNunchakuDev转绘等距风格_1940242636722622465.json, 图片生成/文生图/kontextNunchakuDev转绘线条艺术_1940243382793060354.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/超强去水印工作流Kontext_2095027681485217794.json、图片生成/文生图/kontextNunchakuDev转绘低多边形风格_1940245828193927170.json、图片生成/文生图/kontextNunchakuDev转绘动漫_1940236757055000577.json、图片生成/文生图/kontextNunchakuDev转绘奇幻艺术_1940240607094722562.json、图片生成/文生图/kontextNunchakuDev转绘工艺粘土风_1940239181278826498.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 9/10 个有
- `RH_Translator` —— 9/10 个有
- `ConstrainImage|pysssss` —— 1/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `LayerUtility: GetImageSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
