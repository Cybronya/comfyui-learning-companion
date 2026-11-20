---
key: 平台全量/【阡陌】Nunchaku Flux Upscaler高清放大_1945441313145724929.json
name: 【阡陌】Nunchaku Flux Upscaler高清放大_1945441313145724929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Nunchaku Flux Upscaler高清放大_1945441313145724929.json
hash: 7a0fe59fba331d31
coverage: 0.863636
learned_at: 2026-11-14 01:25:57
nodes: [LayerUtility: JoyCaptionBeta1ExtraOptions, ShowText|pysssss, ShowText|pysssss, DeepTranslatorTextNode, LayerUtility: JoyCaptionBeta1, FluxGuidance, ConditioningZeroOut, LayerUtility: LoadJoyCaptionBeta1Model, SaveImage, NunchakuTextEncoderLoaderV2, CLIPTextEncode, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, ControlNetLoader, KSampler, VAEEncode, VAELoader, ImageScaleBy, LoadImage, VAEDecode, ControlNetApplyAdvanced, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 37294204995519, "steps": 20}
---

# 平台全量/【阡陌】Nunchaku Flux Upscaler高清放大_1945441313145724929.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Nunchaku Flux Upscaler高清放大_1945441313145724929.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `LayerUtility: JoyCaptionBeta1`
- `FluxGuidance`
- `ConditioningZeroOut`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `SaveImage`
- `NunchakuTextEncoderLoaderV2`
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `ControlNetLoader`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `ImageScaleBy`
- `LoadImage`
- `VAEDecode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `37294204995519`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`LayerUtility: JoyCaptionBeta1ExtraOptions`、`DeepTranslatorTextNode`、`LayerUtility: JoyCaptionBeta1`、`FluxGuidance`、`ConditioningZeroOut`、`LayerUtility: LoadJoyCaptionBeta1Model`、`SaveImage`、`NunchakuTextEncoderLoaderV2`、`CLIPTextEncode`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`ControlNetLoader`、`KSampler`、`VAEEncode`、`VAELoader`、`ImageScaleBy`、`LoadImage`、`VAEDecode`、`ControlNetApplyAdvanced`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
