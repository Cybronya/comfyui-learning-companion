---
name: image_to_image_sampler_clip_unet_122
type: Image To Image
frequency: 4
level: strong
coverage: 0.9255
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Latent Batch Size, DepthAnythingV2Preprocessor, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, InstructPixToPixConditioning, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【图生图_深度】洗稿丨室内免侵权洗图_1932680836783509505.json, 图片生成/图生图/洗图洗稿丨室内免侵权_1899750578707390466.json, 图片生成/图生图/洗图洗稿丨室内免侵权室内洗图洗稿_1930866047145193474.json, 图片生成/文生图/FLUX深度控制+图生图反推换脸_1897654973545828354.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_122

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【图生图_深度】洗稿丨室内免侵权洗图_1932680836783509505.json、图片生成/图生图/洗图洗稿丨室内免侵权_1899750578707390466.json、图片生成/图生图/洗图洗稿丨室内免侵权室内洗图洗稿_1930866047145193474.json、图片生成/文生图/FLUX深度控制+图生图反推换脸_1897654973545828354.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `MirroredImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ApplyPulidFlux` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `LoraLoader|pysssss` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PulidFluxEvaClipLoader` —— 1/4 个有
- `PulidFluxInsightFaceLoader` —— 1/4 个有
- `PulidFluxModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.65 | 0.5 - 1 | 4 | 70% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.65，观测区间 0.5 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
