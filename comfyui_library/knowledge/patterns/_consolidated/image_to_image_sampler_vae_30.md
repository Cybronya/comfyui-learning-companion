---
name: image_to_image_sampler_vae_30
type: Image To Image
frequency: 3
level: strong
coverage: 1
common_nodes: [ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【阡陌】Nunchaku 8倍加速 flux 图生图_1944739551309123585.json, 图片生成/图生图/单图-kontext-nunchaku_1952297107749285889.json, 图片生成/图生图/图像编辑 _ Kontext单图编辑_1951659077866827777.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【阡陌】Nunchaku 8倍加速 flux 图生图_1944739551309123585.json、图片生成/图生图/单图-kontext-nunchaku_1952297107749285889.json、图片生成/图生图/图像编辑 _ Kontext单图编辑_1951659077866827777.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `NunchakuTextEncoderLoaderV2` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.7 - 1 | 3 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
