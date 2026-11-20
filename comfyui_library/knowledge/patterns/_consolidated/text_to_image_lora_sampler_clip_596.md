---
name: text_to_image_lora_sampler_clip_596
type: Text To Image
frequency: 3
level: strong
coverage: 0.987667
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningConcat, ConditioningZeroOut, DF_Get_latent_size, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PulidFluxInsightFaceLoader, PulidFluxModelLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux定制专属盲盒形象_1923047780451799041.json, 平台全量/照片生成苗族少女动漫肖像_1917894962493456386.json, 数字人/数字人/照片生成3d数字人形象_1918957193448853505.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_596

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Flux定制专属盲盒形象_1923047780451799041.json、平台全量/照片生成苗族少女动漫肖像_1917894962493456386.json、数字人/数字人/照片生成3d数字人形象_1918957193448853505.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningConcat`
- `ConditioningZeroOut`
- `DF_Get_latent_size`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PulidEvaClipLoader` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `ImageScaleToMegapixels` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `SeedSelector` —— 1/3 个有
- `easy imageScaleToNormPixels` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 3 | 65% |
| 宽度 | 896 | 832 - 904 | 3 | 96% |
| 高度 | 1600 | 1216 - 1600 | 3 | 88% |
| ControlNet 权重 | 0.6 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，3 个样本
- 宽度 中位数 896，观测区间 832 - 904，3 个样本，取值集中（一致性 96%）
- 高度 中位数 1600，观测区间 1216 - 1600，3 个样本，取值集中（一致性 88%）
