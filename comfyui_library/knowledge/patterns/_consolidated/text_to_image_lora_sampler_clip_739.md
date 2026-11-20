---
name: text_to_image_lora_sampler_clip_739
type: Text To Image
frequency: 2
level: weak
coverage: 0.926
common_nodes: [ApplyPulidFlux, CLIPTextEncode, CLIPVisionLoader, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FusionText, GetImageSize+, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, PulidEvaClipLoader, PulidFluxModelLoader, PulidInsightFaceLoader, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/照片转绘像素画风格FLUX_1925204510002585602.json, 平台全量/蔚迦思短剧转绘_1935542487899635714.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_739

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/照片转绘像素画风格FLUX_1925204510002585602.json、平台全量/蔚迦思短剧转绘_1935542487899635714.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FusionText`
- `GetImageSize+`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidInsightFaceLoader`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
