---
name: unknown_workflow_sampler_clip_vae_71
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.938333
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux「最强网感+极速换脸」图片换脸_1884253762348007425.json, 平台全量/FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066.json, 平台全量/FLUX-PuLID + REDUX指定人脸和风格写真_1894723929909428225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux「最强网感+极速换脸」图片换脸_1884253762348007425.json、平台全量/FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066.json、平台全量/FLUX-PuLID + REDUX指定人脸和风格写真_1894723929909428225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Image Crop Face` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SDXLAspectRatioSelector` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
