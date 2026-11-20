---
name: text_to_image_sampler_clip_unet_188
type: Text To Image
frequency: 3
level: strong
coverage: 0.981333
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ModelSamplingFlux, PulidFluxModelLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/使用AI发现最终的东方艺术创作工作流程_1943190429477060609.json, 平台全量/flux-pulid融图合照_1936709714103406594.json, 平台全量/flux人脸一致工作流_1946192815175163906.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_188

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/使用AI发现最终的东方艺术创作工作流程_1943190429477060609.json、平台全量/flux-pulid融图合照_1936709714103406594.json、平台全量/flux人脸一致工作流_1946192815175163906.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `PulidFluxModelLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EcomIDEvaClipLoader` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `MaskComposite` —— 2/3 个有
- `SolidMask` —— 2/3 个有
- `EcomIDFaceAnalysis` —— 1/3 个有
- `InstantIDFaceAnalysis` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `PulidInsightFaceLoader` —— 1/3 个有
- `easy stylesSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1280 | 768 - 1280 | 3 | 78% |
| 高度 | 928 | 928 - 1280 | 3 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 768 - 1280，3 个样本
- 高度 中位数 928，观测区间 928 - 1280，3 个样本，取值集中（一致性 84%）
