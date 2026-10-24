---
name: text_to_image_controlnet_inpaint_upscale_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.838
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DeepTranslatorTextNode, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImageCrop+, ImageScaleToMegapixels, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, KSamplerSelect, LayerMask: RmBgUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, LoraLoaderModelOnly, MaskPreview+, PreviewImage, RMBG, RandomNoise, ReduxAdvanced, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea 电商图生图｜图像精修_1951118464054439937.json, 图片生成/文生图/flux krea电商文生图+图生图修复+放大+万物迁移+kontext 万物迁移_1951101157949251586.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux Krea 电商图生图｜图像精修_1951118464054439937.json、图片生成/文生图/flux krea电商文生图+图生图修复+放大+万物迁移+kontext 万物迁移_1951101157949251586.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageCrop+`
- `ImageScaleToMegapixels`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: RmBgUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `RMBG`
- `RandomNoise`
- `ReduxAdvanced`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy makeImageForICLora`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.13 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| 宽度 | 1480 | - | 2 | 100% |
| 高度 | 1208 | - | 2 | 100% |
| LoRA 模型强度 | 0.7 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.13，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1480，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1208，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
