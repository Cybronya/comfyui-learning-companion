---
name: unknown_workflow_controlnet_sampler_clip_37
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [AIO_Preprocessor, AdvancedVisionLoader, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, GetImageSize+, GrowMaskWithBlur, ICLightApplyMaskGrey, Image Comparer (rgthree), ImageCompositeMasked, ImageConcanate, ImageRemoveAlpha+, InvertMask, JWImageResizeByLongerSide, KSamplerSelect, LayerMask: RmBgUltra V2, LayerUtility: CropByMask V3, LoadImage, MaskPreview+, PixelPerfectResolution, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, SetUnionControlNetType, StyleModelApply, StyleModelLoader, SubtractMask, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634.json, 平台全量/Flux controlnet Union 2.0 + Redux 512换背景_1915445797230411777.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634.json、平台全量/Flux controlnet Union 2.0 + Redux 512换背景_1915445797230411777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AdvancedVisionLoader`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `ICLightApplyMaskGrey`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageRemoveAlpha+`
- `InvertMask`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LayerMask: RmBgUltra V2`
- `LayerUtility: CropByMask V3`
- `LoadImage`
- `MaskPreview+`
- `PixelPerfectResolution`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetUnionControlNetType`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.4 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
