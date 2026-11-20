---
name: text_to_image_lora_sampler_clip_615
type: Text To Image
frequency: 2
level: weak
coverage: 0.9425
common_nodes: [Apply Text Template (mtb), ApplyPulidFlux, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, FluxGuidance, Image Crop Face, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, SDXLAspectRatioSelector, SaveImage, VAEDecode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/反推提示词/Flux最强肖像转素描(铅笔画_速写_线稿_底稿_灰度画_单色画)工作流_1905892025487511554.json, 平台全量/肖像转素描_1856959468931108865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_615

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Flux最强肖像转素描(铅笔画_速写_线稿_底稿_灰度画_单色画)工作流_1905892025487511554.json、平台全量/肖像转素描_1856959468931108865.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Text Template (mtb)`
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Crop Face`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `SDXLAspectRatioSelector`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `Get resolution [Crystools]` —— 1/2 个有
- `Grayscale Image (WLSH)` —— 1/2 个有
- `ImageEffectsGrayscale` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LineArtPreprocessor` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | - | 1 | 100% |
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
