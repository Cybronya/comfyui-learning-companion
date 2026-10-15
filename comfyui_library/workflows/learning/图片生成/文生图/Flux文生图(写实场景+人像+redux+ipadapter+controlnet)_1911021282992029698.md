---
key: 图片生成/文生图/Flux文生图(写实场景+人像+redux+ipadapter+controlnet)_1911021282992029698.json
name: Flux文生图(写实场景+人像+redux+ipadapter+controlnet)_1911021282992029698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux文生图(写实场景+人像+redux+ipadapter+controlnet)_1911021282992029698.json
hash: b53ffd582ac3024b
coverage: 0.857143
learned_at: 2026-10-10 20:58:37
nodes: [IPAdapterFluxLoader, StyleModelLoader, CLIPVisionLoader, LoadImage, SaveImage, TextCombinerTwo, JjkText, RH_Prompter, JjkText, ShowText|pysssss, CLIPTextEncode, ReduxAdvanced, ApplyIPAdapterFlux, KSamplerSelect, ModelSamplingFlux, RandomNoise, EmptyLatentImage, SamplerCustomAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicGuider, FluxGuidance, SetUnionControlNetType, DepthAnythingV2Preprocessor, DualCLIPLoader, Anything Everywhere, UNETLoader, Anything Everywhere, Anything Everywhere, VAEDecode, ControlNetLoader, ControlNetLoader, ControlNetApplyAdvanced, SetUnionControlNetType, OpenposePreprocessor, LoadImage, PyraCannyPreprocessor, SetUnionControlNetType, ControlNetApplyAdvanced, ControlNetLoader, ControlNetApplyAdvanced, Fast Groups Bypasser (rgthree), Int, Int, Int, VAELoader, BasicScheduler]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.6000000000000001, "height": 1280, "width": 952}
---

# 图片生成/文生图/Flux文生图(写实场景+人像+redux+ipadapter+controlnet)_1911021282992029698.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux文生图(写实场景+人像+redux+ipadapter+controlnet)_1911021282992029698.json`

## 结构

**节点**（49 个）：
- `IPAdapterFluxLoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LoadImage`
- `SaveImage`
- `TextCombinerTwo`
- `JjkText`
- `RH_Prompter`
- `JjkText`
- `ShowText|pysssss`
- `CLIPTextEncode`
- `ReduxAdvanced`
- `ApplyIPAdapterFlux`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `EmptyLatentImage`
- `SamplerCustomAdvanced`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `BasicGuider`
- `FluxGuidance`
- `SetUnionControlNetType`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `Anything Everywhere`
- `UNETLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAEDecode`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetApplyAdvanced`
- `SetUnionControlNetType`
- `OpenposePreprocessor`
- `LoadImage`
- `PyraCannyPreprocessor`
- `SetUnionControlNetType`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ControlNetApplyAdvanced`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `Int`
- `Int`
- `VAELoader`
- `BasicScheduler`

## 关键参数

- `batch_size` = `1`
- `controlnet_strength` = `0.6000000000000001`
- `height` = `1280`
- `width` = `952`

## 知识

覆盖率 **86%**（42/49）

**有卡**：`IPAdapterFluxLoader`、`StyleModelLoader`、`CLIPVisionLoader`、`LoadImage`、`SaveImage`、`TextCombinerTwo`、`JjkText`、`RH_Prompter`、`ShowText|pysssss`、`CLIPTextEncode`、`ReduxAdvanced`、`ApplyIPAdapterFlux`、`KSamplerSelect`、`ModelSamplingFlux`、`RandomNoise`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`BasicGuider`、`FluxGuidance`、`SetUnionControlNetType`、`DepthAnythingV2Preprocessor`、`DualCLIPLoader`、`Anything Everywhere`、`UNETLoader`、`VAEDecode`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`OpenposePreprocessor`、`PyraCannyPreprocessor`
