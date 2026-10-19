---
name: image_to_image_sampler_clip_vae
type: Image To Image
frequency: 12
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1940230026011000833.json, 图片生成/文生图/1940235010588758018.json, 图片生成/文生图/1940236757055000577.json, 图片生成/文生图/1940238028432654337.json, 图片生成/文生图/1940239181278826498.json, 图片生成/文生图/1940240607094722562.json, 图片生成/文生图/1940242636722622465.json, 图片生成/文生图/1940243382793060354.json, 图片生成/文生图/1940245828193927170.json, 图片生成/文生图/1985614052636479490.json, 视频生成/图生视频/1985614052636479490.json, 视频生成/图生视频/1937024075837640705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1940230026011000833.json、图片生成/文生图/1940235010588758018.json、图片生成/文生图/1940236757055000577.json、图片生成/文生图/1940238028432654337.json、图片生成/文生图/1940239181278826498.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 9/12 个有
- `NunchakuFluxDiTLoader` —— 9/12 个有
- `RH_Translator` —— 9/12 个有
- `UNETLoader` —— 3/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `RepeatLatentBatch` —— 2/12 个有

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
