---
key: 平台全量/一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105.json
name: 一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105.json
hash: cc9038afc988beae
coverage: 0.714286
learned_at: 2026-11-14 01:30:08
nodes: [CLIPTextEncode, PreviewImage, FluxGuidance, Anything Everywhere, ConditioningZeroOut, PreviewImage, SetUnionControlNetType, Anything Everywhere, ShowText|pysssss, StringFunction|pysssss, KSampler (Efficient), EmptySD3LatentImage, NunchakuTextEncoderLoaderV2, JJC_JoyCaption, GoogleTranslateTextNode, ControlNetApplySD3, NunchakuFluxLoraLoader, AIO_Preprocessor, LoadImage, Note, ControlNetLoader, NunchakuFluxLoraLoader, VAELoader, Anything Everywhere, Anything Everywhere, NunchakuFluxDiTLoader, LayerFilter: HDREffects, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1061054777003517, "steps": 25}
---

# 平台全量/一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Process → Output → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `FluxGuidance`
- `Anything Everywhere`
- `ConditioningZeroOut`
- `PreviewImage`
- `SetUnionControlNetType`
- `Anything Everywhere`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `KSampler (Efficient)` ★核心
- `EmptySD3LatentImage`
- `NunchakuTextEncoderLoaderV2`
- `JJC_JoyCaption`
- `GoogleTranslateTextNode`
- `ControlNetApplySD3` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `Note`
- `ControlNetLoader`
- `NunchakuFluxLoraLoader` ★核心
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `NunchakuFluxDiTLoader`
- `LayerFilter: HDREffects`
- `SaveImage`

## 关键参数

- `seed` = `1061054777003517`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`SetUnionControlNetType`、`StringFunction|pysssss`、`KSampler (Efficient)`、`EmptySD3LatentImage`、`NunchakuTextEncoderLoaderV2`、`JJC_JoyCaption`、`GoogleTranslateTextNode`、`ControlNetApplySD3`、`NunchakuFluxLoraLoader`、`AIO_Preprocessor`、`LoadImage`、`ControlNetLoader`、`VAELoader`、`NunchakuFluxDiTLoader`、`LayerFilter: HDREffects`、`SaveImage`

**用到的条目**：VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplySD3、ControlNetLoader、SetUnionControlNetType、FluxGuidance
