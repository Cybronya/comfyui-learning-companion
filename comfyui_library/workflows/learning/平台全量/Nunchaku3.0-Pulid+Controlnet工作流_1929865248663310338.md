---
key: 平台全量/Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338.json
name: Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338.json
hash: 908c306735bc319a
coverage: 0.925926
learned_at: 2026-11-14 00:47:12
nodes: [KSamplerSelect, NunchakuTextEncoderLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ControlNetApplyAdvanced, ModelSamplingFlux, BasicGuider, RandomNoise, BasicScheduler, EmptySD3LatentImage, NunchakuPulidApply, NunchakuPulidLoader, VAELoader, ImageConcatMulti, AIO_Preprocessor, ControlNetLoader, LoadImage, PreviewImage, PreviewImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, SamplerCustomAdvanced, VAEDecode, SaveImage, LoadImage, SetUnionControlNetType]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6000000000000001}
---

# 平台全量/Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338.json

> 来源文件 `comfyui_library/workflows/平台全量/Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `KSamplerSelect` ★核心
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced` ★核心
- `ModelSamplingFlux`
- `BasicGuider`
- `RandomNoise`
- `BasicScheduler`
- `EmptySD3LatentImage`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `VAELoader`
- `ImageConcatMulti`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `SetUnionControlNetType`

## 关键参数

- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`KSamplerSelect`、`NunchakuTextEncoderLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`ControlNetApplyAdvanced`、`ModelSamplingFlux`、`BasicGuider`、`RandomNoise`、`BasicScheduler`、`EmptySD3LatentImage`、`NunchakuPulidApply`、`NunchakuPulidLoader`、`VAELoader`、`ImageConcatMulti`、`AIO_Preprocessor`、`ControlNetLoader`、`LoadImage`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`SetUnionControlNetType`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType
