---
name: unknown_workflow_sampler_clip_vae_52
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86125
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, EmptySD3LatentImage, FluxGuidance, GetImageSize, ImageScaleToMegapixels, KSampler, LoadImage, ModelSamplingFlux, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/2025-04-15-new_redux_v2_flex_alpha_1913979039407898626.json, 图片生成/图生图/2025-04-15-new_redux_v2_flux_1913989626762330113.json, 图片生成/图生图/2025-04-15-new_redux_v2_nunchaku_1913998850091118593.json, 图片生成/图生图/reduxV2-反推洗图_1914546255769600001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_52

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2025-04-15-new_redux_v2_flex_alpha_1913979039407898626.json、图片生成/图生图/2025-04-15-new_redux_v2_flux_1913989626762330113.json、图片生成/图生图/2025-04-15-new_redux_v2_nunchaku_1913998850091118593.json、图片生成/图生图/reduxV2-反推洗图_1914546255769600001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GetImageSize`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `JanusImageUnderstanding` —— 1/4 个有
- `JanusModelLoader` —— 1/4 个有
- `NunchakuFluxDiTLoader` —— 1/4 个有
- `NunchakuFluxLoraLoader` —— 1/4 个有
- `NunchakuTextEncoderLoader` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
