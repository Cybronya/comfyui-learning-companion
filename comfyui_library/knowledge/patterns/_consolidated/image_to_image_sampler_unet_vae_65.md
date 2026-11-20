---
name: image_to_image_sampler_unet_vae_65
type: Image To Image
frequency: 3
level: strong
coverage: 0.899
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/融图V2_1969383780073021441.json, 平台全量/迷雾氛围_1967808203494928385.json, 数字人/数字人/野猪A6-电商产品光影融合V5_2004153498461741057.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_65

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/融图V2_1969383780073021441.json、平台全量/迷雾氛围_1967808203494928385.json、数字人/数字人/野猪A6-电商产品光影融合V5_2004153498461741057.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Batch Size` —— 2/3 个有
- `ControlNetApplySD3` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `DepthAnythingPreprocessor` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `JWImageResizeByLongerSide` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CannyEdgePreprocessor` —— 1/3 个有
- `Float` —— 1/3 个有
- `LineArtPreprocessor` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
