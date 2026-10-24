---
key: 图片生成/图生图/Nunchaku3.0 明星洗图｜快速出图_1936991256188735489.json
name: Nunchaku3.0 明星洗图｜快速出图_1936991256188735489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku3.0 明星洗图｜快速出图_1936991256188735489.json
hash: 034e2e049257de30
coverage: 0.740741
learned_at: 2026-10-23 11:10:04
nodes: [CLIPTextEncode, PreviewImage, FluxGuidance, Anything Everywhere, ConditioningZeroOut, PreviewImage, SetUnionControlNetType, Anything Everywhere, ShowText|pysssss, StringFunction|pysssss, KSampler (Efficient), EmptySD3LatentImage, NunchakuTextEncoderLoaderV2, JJC_JoyCaption, GoogleTranslateTextNode, ControlNetApplySD3, NunchakuFluxLoraLoader, AIO_Preprocessor, ControlNetLoader, NunchakuFluxLoraLoader, VAELoader, Anything Everywhere, Anything Everywhere, NunchakuFluxDiTLoader, LayerFilter: HDREffects, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1061054777003517, "steps": 25}
---

# 图片生成/图生图/Nunchaku3.0 明星洗图｜快速出图_1936991256188735489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku3.0 明星洗图｜快速出图_1936991256188735489.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Process → Output → Other

**节点**（27 个）：
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
- `ControlNetLoader`
- `NunchakuFluxLoraLoader` ★核心
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `NunchakuFluxDiTLoader`
- `LayerFilter: HDREffects`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `1061054777003517`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`SetUnionControlNetType`、`StringFunction|pysssss`、`KSampler (Efficient)`、`EmptySD3LatentImage`、`NunchakuTextEncoderLoaderV2`、`JJC_JoyCaption`、`GoogleTranslateTextNode`、`ControlNetApplySD3`、`NunchakuFluxLoraLoader`、`AIO_Preprocessor`、`ControlNetLoader`、`VAELoader`、`NunchakuFluxDiTLoader`、`LayerFilter: HDREffects`、`SaveImage`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、SetUnionControlNetType、ControlNetApplySD3、FluxGuidance
