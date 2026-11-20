---
name: image_to_image_inpaint_sampler_clip_10
type: Image To Image
frequency: 2
level: weak
coverage: 0.898
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, GrowMask, ImpactGaussianBlurMask, InpaintModelConditioning, InstructPixToPixConditioning, InvertMask (segment anything), KSampler, LayerUtility: PurgeVRAM, LoadImage, MaskBlur+, MaskComposite, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键换人物背景_1895007452121399297.json, 图片生成/图生图/手机壳更换背景_洗图_1911752493666136065.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键换人物背景_1895007452121399297.json、图片生成/图生图/手机壳更换背景_洗图_1911752493666136065.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GrowMask`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `InstructPixToPixConditioning`
- `InvertMask (segment anything)`
- `KSampler`
- `LayerUtility: PurgeVRAM`
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
- `AIO_Preprocessor` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `DepthAnythingPreprocessor` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModel` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.3 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
