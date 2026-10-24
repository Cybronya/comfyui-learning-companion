---
name: image_to_image_sampler_vae_21
type: Image To Image
frequency: 6
level: strong
coverage: 0.962333
common_nodes: [FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【阡陌】Nunchaku 8倍加速 flux 图生图_1944739551309123585.json, 图片生成/图生图/单图-kontext-nunchaku_1952297107749285889.json, 图片生成/图生图/双截棍-kontext（dev）_1938464979685433345.json, 图片生成/图生图/最好用的 nunchaku flux kontext 去水印_2053752457087467522.json, 图片生成/图生图/穆寒_2072683428708966401.json, 图片生成/图生图/超强去水印工作流Kontext_2095027681485217794.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_21

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【阡陌】Nunchaku 8倍加速 flux 图生图_1944739551309123585.json、图片生成/图生图/单图-kontext-nunchaku_1952297107749285889.json、图片生成/图生图/双截棍-kontext（dev）_1938464979685433345.json、图片生成/图生图/最好用的 nunchaku flux kontext 去水印_2053752457087467522.json、图片生成/图生图/穆寒_2072683428708966401.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `DualCLIPLoader` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `CLIPTextEncode` —— 4/6 个有
- `FluxKontextImageScale` —— 4/6 个有
- `DeepTranslatorTextNode` —— 2/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 1/6 个有
- `CLIPTextEncodeFlux` —— 1/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `LayerUtility: GetImageSize` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `NunchakuFluxLoraLoader` —— 1/6 个有
- `NunchakuTextEncoderLoaderV2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 0.7 - 1 | 6 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，6 个样本，取值集中（一致性 88%）
