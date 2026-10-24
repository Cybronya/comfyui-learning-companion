---
key: 图片生成/图生图/Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634.json
name: Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634.json
hash: e2c036fe39dbf3cb
coverage: 0.875
learned_at: 2026-10-23 10:57:59
nodes: [DualCLIPLoader, ConditioningZeroOut, GetImageSize+, ImageRemoveAlpha+, PreviewImage, ImageRemoveAlpha+, KSamplerSelect, VAEEncode, ControlNetApplyAdvanced, ICLightApplyMaskGrey, Reroute, LayerUtility: CropByMask V3, TextInput_, TextInput_, RH_Captioner, Text Concatenate (JPS), ImageRemoveAlpha+, ImageRemoveAlpha+, SetUnionControlNetType, SetUnionControlNetType, CLIPVisionEncode, AdvancedVisionLoader, ImageRemoveAlpha+, FluxGuidance, BasicGuider, StyleModelLoader, RH_Captioner, PreviewImage, CLIPTextEncode, InvertMask, GrowMaskWithBlur, MaskPreview+, MaskPreview+, GrowMaskWithBlur, MaskPreview+, SamplerCustomAdvanced, SubtractMask, SetLatentNoiseMask, ImageCompositeMasked, VAELoader, VAEEncode, SamplerCustomAdvanced, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), BasicScheduler, RandomNoise, AIO_Preprocessor, AIO_Preprocessor, Image Comparer (rgthree), BasicScheduler, JWImageResizeByLongerSide, ControlNetLoader, ControlNetApplyAdvanced, LayerMask: RmBgUltra V2, PreviewImage, JWImageResizeByLongerSide, ImageConcanate, VAEDecode, PreviewImage, ImageConcanate, ImageConcanate, VAEDecode, SaveImage, StyleModelApply, StyleModelApply, CLIPVisionEncode, UNETLoader, PixelPerfectResolution, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.4000000000000001}
---

# 图片生成/图生图/Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Krea + ControlNet Union + Redux 人物换背景｜一致性_1951497437942853634.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `GetImageSize+`
- `ImageRemoveAlpha+`
- `PreviewImage`
- `ImageRemoveAlpha+`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ICLightApplyMaskGrey`
- `Reroute`
- `LayerUtility: CropByMask V3`
- `TextInput_`
- `TextInput_`
- `RH_Captioner`
- `Text Concatenate (JPS)`
- `ImageRemoveAlpha+`
- `ImageRemoveAlpha+`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `CLIPVisionEncode`
- `AdvancedVisionLoader`
- `ImageRemoveAlpha+`
- `FluxGuidance`
- `BasicGuider`
- `StyleModelLoader`
- `RH_Captioner`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `InvertMask`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `MaskPreview+`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `SamplerCustomAdvanced` ★核心
- `SubtractMask`
- `SetLatentNoiseMask`
- `ImageCompositeMasked`
- `VAELoader`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `BasicScheduler`
- `RandomNoise`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `Image Comparer (rgthree)`
- `BasicScheduler`
- `JWImageResizeByLongerSide`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `LayerMask: RmBgUltra V2`
- `PreviewImage`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageConcanate`
- `ImageConcanate`
- `VAEDecode` ★核心
- `SaveImage`
- `StyleModelApply`
- `StyleModelApply`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `PixelPerfectResolution`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.4000000000000001`

## 知识

覆盖率 **88%**（63/72）

**有卡**：`DualCLIPLoader`、`ConditioningZeroOut`、`GetImageSize+`、`ImageRemoveAlpha+`、`KSamplerSelect`、`VAEEncode`、`ControlNetApplyAdvanced`、`ICLightApplyMaskGrey`、`LayerUtility: CropByMask V3`、`TextInput_`、`RH_Captioner`、`Text Concatenate (JPS)`、`SetUnionControlNetType`、`CLIPVisionEncode`、`AdvancedVisionLoader`、`FluxGuidance`、`BasicGuider`、`StyleModelLoader`、`CLIPTextEncode`、`InvertMask`、`GrowMaskWithBlur`、`MaskPreview+`、`SamplerCustomAdvanced`、`SubtractMask`、`SetLatentNoiseMask`、`ImageCompositeMasked`、`VAELoader`、`BasicScheduler`、`RandomNoise`、`AIO_Preprocessor`、`JWImageResizeByLongerSide`、`ControlNetLoader`、`LayerMask: RmBgUltra V2`、`ImageConcanate`、`VAEDecode`、`SaveImage`、`StyleModelApply`、`UNETLoader`、`PixelPerfectResolution`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
