---
name: image_to_image_sampler_clip_vae_16
type: Image To Image
frequency: 12
level: strong
coverage: 0.968083
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图像编辑 _ Kontext单图编辑_1951659077866827777.json, 图片生成/图生图/极速图像水印擦除无损文字_1942419516015980546.json, 图片生成/图生图/极速图像水印擦除无损文字_2005560503084740610.json, 图片生成/文生图/kontextNunchakuDev转绘低多边形风格_1940245828193927170.json, 图片生成/文生图/kontextNunchakuDev转绘动漫_1940236757055000577.json, 图片生成/文生图/kontextNunchakuDev转绘奇幻艺术_1940240607094722562.json, 图片生成/文生图/kontextNunchakuDev转绘工艺粘土风_1940239181278826498.json, 图片生成/文生图/kontextNunchakuDev转绘模拟电影_1940235010588758018.json, 图片生成/文生图/kontextNunchakuDev转绘漫画_1940238028432654337.json, 图片生成/文生图/kontextNunchakuDev转绘电影感风_1940230026011000833.json, 图片生成/文生图/kontextNunchakuDev转绘等距风格_1940242636722622465.json, 图片生成/文生图/kontextNunchakuDev转绘线条艺术_1940243382793060354.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/图像编辑 _ Kontext单图编辑_1951659077866827777.json、图片生成/图生图/极速图像水印擦除无损文字_1942419516015980546.json、图片生成/图生图/极速图像水印擦除无损文字_2005560503084740610.json、图片生成/文生图/kontextNunchakuDev转绘低多边形风格_1940245828193927170.json、图片生成/文生图/kontextNunchakuDev转绘动漫_1940236757055000577.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 11/12 个有
- `RH_Translator` —— 11/12 个有
- `ModelSamplingFlux` —— 9/12 个有
- `EmptySD3LatentImage` —— 3/12 个有
- `ImageStitch` —— 2/12 个有
- `LoadImageOutput` —— 2/12 个有
- `GetImageSize` —— 1/12 个有
- `JjkShowText` —— 1/12 个有
- `Text` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
