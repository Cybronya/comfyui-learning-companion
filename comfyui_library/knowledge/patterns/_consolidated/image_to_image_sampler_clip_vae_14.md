---
name: image_to_image_sampler_clip_vae_14
type: Image To Image
frequency: 18
level: strong
coverage: 0.964667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超强去水印工作流Kontext_2095027681485217794.json, 图片生成/文生图/kontextNunchakuDev转绘低多边形风格_1940245828193927170.json, 图片生成/文生图/kontextNunchakuDev转绘动漫_1940236757055000577.json, 图片生成/文生图/kontextNunchakuDev转绘奇幻艺术_1940240607094722562.json, 图片生成/文生图/kontextNunchakuDev转绘工艺粘土风_1940239181278826498.json, 图片生成/文生图/kontextNunchakuDev转绘模拟电影_1940235010588758018.json, 图片生成/文生图/kontextNunchakuDev转绘漫画_1940238028432654337.json, 图片生成/文生图/kontextNunchakuDev转绘电影感风_1940230026011000833.json, 图片生成/文生图/kontextNunchakuDev转绘等距风格_1940242636722622465.json, 图片生成/文生图/kontextNunchakuDev转绘线条艺术_1940243382793060354.json, 平台全量/2D转3D 潮玩盲盒对象一致性生图_Kontext1.0_1975106133272735746.json, 平台全量/Kontext去水印_1963082615362392066.json, 平台全量/kontext一键去除水印(20秒双加速版）_1939970423499190274.json, 平台全量/电商一键提取模特服装_1947502221950865409.json, 平台全量/直播图片生成粒子特效_1947498857430159361.json, 平台全量/直播定制人物手办_1947494086783684610.json, 平台全量/直播老照片修复_1943215616889413634.json, 平台全量/超强Kontext去水印工作流_1948299121468813314.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/超强去水印工作流Kontext_2095027681485217794.json、图片生成/文生图/kontextNunchakuDev转绘低多边形风格_1940245828193927170.json、图片生成/文生图/kontextNunchakuDev转绘动漫_1940236757055000577.json、图片生成/文生图/kontextNunchakuDev转绘奇幻艺术_1940240607094722562.json、图片生成/文生图/kontextNunchakuDev转绘工艺粘土风_1940239181278826498.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 18 个 workflow 都包含：
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
- `RH_Translator` —— 14/18 个有
- `ModelSamplingFlux` —— 9/18 个有
- `NunchakuFluxLoraLoader` —— 6/18 个有
- `EmptySD3LatentImage` —— 4/18 个有
- `easy imageSize` —— 4/18 个有
- `DeepTranslatorTextNode` —— 3/18 个有
- `Image Comparer (rgthree)` —— 3/18 个有
- `ConstrainImage|pysssss` —— 2/18 个有
- `LayerUtility: GetImageSize` —— 2/18 个有
- `easy cleanGpuUsed` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 18 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
