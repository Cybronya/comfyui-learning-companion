---
name: image_to_image_sampler_clip_vae_13
type: Image To Image
frequency: 14
level: strong
coverage: 0.976643
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, RH_Translator, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext 动漫转真人（双截棍）_1975110263445827585.json, 图片生成/图生图/kontext 手拿产品姿势生成_1976644315327893505.json, 图片生成/图生图/kontextNunchakuDev转绘像素艺术_1940592142769352705.json, 图片生成/图生图/kontextNunchakuDev转绘元素艺术_1940607114458935297.json, 图片生成/图生图/kontextNunchakuDev转绘动态插画_1940603858894696450.json, 图片生成/图生图/kontextNunchakuDev转绘古代插画_1940610524772200450.json, 图片生成/图生图/kontextNunchakuDev转绘史诗电影风格_1940597701073416194.json, 图片生成/图生图/kontextNunchakuDev转绘折纸艺术_1940246673190993921.json, 图片生成/图生图/kontextNunchakuDev转绘空间艺术_1940609295543332866.json, 图片生成/图生图/kontextNunchakuDev转绘纹理艺术_1940594910586187778.json, 图片生成/图生图/kontextNunchakuDev转绘艺术视觉风格_1940599249056985089.json, 图片生成/图生图/kontextNunchakuDev转绘超现实主义绘画风格_1940601783699877890.json, 图片生成/图生图/kontextNunchakuDev转绘遗忘艺术家作品_1940605971251048449.json, 图片生成/图生图/kontext_全能精修丨产品精修丨人像精修丨婚纱照精修全能精修V1_1947931579113975809.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/kontext 动漫转真人（双截棍）_1975110263445827585.json、图片生成/图生图/kontext 手拿产品姿势生成_1976644315327893505.json、图片生成/图生图/kontextNunchakuDev转绘像素艺术_1940592142769352705.json、图片生成/图生图/kontextNunchakuDev转绘元素艺术_1940607114458935297.json、图片生成/图生图/kontextNunchakuDev转绘动态插画_1940603858894696450.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 13/14 个有
- `FluxKontextImageScale` —— 13/14 个有
- `ModelSamplingFlux` —— 11/14 个有
- `NunchakuFluxLoraLoader` —— 3/14 个有
- `Image Comparer (rgthree)` —— 2/14 个有
- `PreviewImage` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `ImageBBoxOverlayByMask` —— 1/14 个有
- `ImageStitch` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有
- `NunchakuTextEncoderLoaderV2` —— 1/14 个有
- `TextInput_` —— 1/14 个有
- `UNETLoader` —— 1/14 个有
- `easy promptConcat` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
