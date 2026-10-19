---
name: text_to_image_sampler_clip_vae_3
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7622
common_nodes: [CLIPTextEncode, EmptyLatentImage, FluxGuidance, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions]
members: [图片生成/文生图/1940313410569682946.json, 图片生成/文生图/1942186080890204162.json, 图片生成/文生图/1944743997447524354.json, 图片生成/文生图/1951531387230826497.json, 图片生成/文生图/F.1 在线生图-反推_1873979338214559746.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1940313410569682946.json、图片生成/文生图/1942186080890204162.json、图片生成/文生图/1944743997447524354.json、图片生成/文生图/1951531387230826497.json、图片生成/文生图/F.1 在线生图-反推_1873979338214559746.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `DeepTranslatorTextNode` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `NunchakuTextEncoderLoaderV2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 5 | 77% |
| 高度 | 1024 | 512 - 1536 | 5 | 68% |
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，5 个样本
- 高度 中位数 1024，观测区间 512 - 1536，5 个样本
- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: LoadJoyCaptionBeta1Model、LayerUtility: JoyCaptionBeta1ExtraOptions
