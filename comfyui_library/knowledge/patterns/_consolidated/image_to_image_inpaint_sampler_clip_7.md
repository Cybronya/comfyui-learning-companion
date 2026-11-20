---
name: image_to_image_inpaint_sampler_clip_7
type: Image To Image
frequency: 4
level: strong
coverage: 0.89825
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMask, ImpactGaussianBlurMask, InpaintModelConditioning, InstructPixToPixConditioning, InvertMask (segment anything), KSampler, LoadImage, MaskBlur+, MaskComposite, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键换人物背景_1895007452121399297.json, 图片生成/图生图/手机壳更换背景_洗图_1911752493666136065.json, 平台全量/FLUX Redux一键换背景_1915211541673873409.json, 平台全量/Flux换背景_在线生图_1897953978448039938.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换人物背景_1895007452121399297.json、图片生成/图生图/手机壳更换背景_洗图_1911752493666136065.json、平台全量/FLUX Redux一键换背景_1915211541673873409.json、平台全量/Flux换背景_在线生图_1897953978448039938.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMask`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `InstructPixToPixConditioning`
- `InvertMask (segment anything)`
- `KSampler`
- `LoadImage`
- `MaskBlur+`
- `MaskComposite`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `Florence2ModelLoader` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `LayerMask: BiRefNetUltraV2` —— 3/4 个有
- `LayerMask: LoadBiRefNetModel` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `StyleModelApply` —— 3/4 个有
- `StyleModelLoader` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `DepthAnythingPreprocessor` —— 1/4 个有
- `DepthAnything_V2` —— 1/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/4 个有
- `LoraLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.3 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
