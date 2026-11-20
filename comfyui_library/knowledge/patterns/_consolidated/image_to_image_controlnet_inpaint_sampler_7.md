---
name: image_to_image_controlnet_inpaint_sampler_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.8505
common_nodes: [BBoxesToSAM2, CFGNorm, CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, DownloadAndLoadQwenModel, ImageConcanate, InpaintPreprocessor, JjkText, KSampler, LayerMask: MaskPreview, LayerMask: SAM2Ultra, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, QwenVLDetection, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 自动识别去水印_1969309373392711681.json, 图片生成/图生图/Qwen Image 自动识别遮罩重绘_1969288725123506177.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image 自动识别去水印_1969309373392711681.json、图片生成/图生图/Qwen Image 自动识别遮罩重绘_1969288725123506177.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxesToSAM2`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DownloadAndLoadQwenModel`
- `ImageConcanate`
- `InpaintPreprocessor`
- `JjkText`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: SAM2Ultra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenVLDetection`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateShapeMask` —— 1/2 个有
- `GetMaskSizeAndCount` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `MaskBoundingBox+` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
