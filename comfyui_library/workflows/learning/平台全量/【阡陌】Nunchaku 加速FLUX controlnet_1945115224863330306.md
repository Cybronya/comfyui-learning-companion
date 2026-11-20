---
key: 平台全量/【阡陌】Nunchaku 加速FLUX controlnet_1945115224863330306.json
name: 【阡陌】Nunchaku 加速FLUX controlnet_1945115224863330306
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Nunchaku 加速FLUX controlnet_1945115224863330306.json
hash: 7e2ee4892026fa8d
coverage: 0.928571
learned_at: 2026-11-14 01:25:57
nodes: [LayerUtility: JoyCaptionBeta1ExtraOptions, ShowText|pysssss, ShowText|pysssss, DeepTranslatorTextNode, LayerUtility: JoyCaptionBeta1, FluxGuidance, ConditioningZeroOut, LayerUtility: LoadJoyCaptionBeta1Model, AIO_Preprocessor, ControlNetLoader, ControlNetApplyAdvanced, VAEDecode, ControlNetLoader, ControlNetApplyAdvanced, ControlNetLoader, ControlNetApplyAdvanced, LoadImage, EmptyLatentImage, KSampler, easy imageSize, SaveImage, NunchakuTextEncoderLoaderV2, VAELoader, CLIPTextEncode, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, AIO_Preprocessor, AIO_Preprocessor]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 205173149987475, "steps": 20, "width": 768}
---

# 平台全量/【阡陌】Nunchaku 加速FLUX controlnet_1945115224863330306.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Nunchaku 加速FLUX controlnet_1945115224863330306.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `LayerUtility: JoyCaptionBeta1`
- `FluxGuidance`
- `ConditioningZeroOut`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `easy imageSize`
- `SaveImage`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `205173149987475`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`LayerUtility: JoyCaptionBeta1ExtraOptions`、`DeepTranslatorTextNode`、`LayerUtility: JoyCaptionBeta1`、`FluxGuidance`、`ConditioningZeroOut`、`LayerUtility: LoadJoyCaptionBeta1Model`、`AIO_Preprocessor`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`VAEDecode`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`easy imageSize`、`SaveImage`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`CLIPTextEncode`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
