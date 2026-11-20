---
name: unknown_workflow_face_detailer_lora_sampler_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.972
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, EmptySD3LatentImage, FaceAnalysisModels, FaceBoundingBox, FaceDetailer, JanusImageUnderstanding, JanusModelLoader, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, ModelSamplingFlux, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, ReduxAdvanced, SAMLoader, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/网红图片一致性洗图一次性4张套图+面部细化+换脸保持人脸一致性_1923963138599735298.json, 平台全量/一致性洗图洗稿_1922866878644109314.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/网红图片一致性洗图一次性4张套图+面部细化+换脸保持人脸一致性_1923963138599735298.json、平台全量/一致性洗图洗稿_1922866878644109314.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FaceDetailer`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `ReduxAdvanced`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
