---
key: 平台全量/Sandstorm Visual Effect-沙尘暴视觉效果【Context LoRA】_1856603877087891458.json
name: Sandstorm Visual Effect-沙尘暴视觉效果【Context LoRA】_1856603877087891458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Sandstorm Visual Effect-沙尘暴视觉效果【Context LoRA】_1856603877087891458.json
hash: c21814bf937b0e90
coverage: 0.628571
learned_at: 2026-11-14 00:56:56
nodes: [UNETLoader, DualCLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, FluxGuidance, Note, VAEDecode, Label (rgthree), Label (rgthree), Note, PrimitiveNode, PrimitiveNode, PreviewImage, TextCombinerSix, LoraLoader, JjkText, ShowText|pysssss, JjkText, JjkText, TextCombinerTwo, RH_Prompter, ShowText|pysssss, ShowText|pysssss, RH_Prompter, TextCombinerTwo, JjkText, JjkText]
patterns: [lora]
missing: []
parameters: {"lora_name": "sandstorm-visual-effect.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Sandstorm Visual Effect-沙尘暴视觉效果【Context LoRA】_1856603877087891458.json

> 来源文件 `comfyui_library/workflows/平台全量/Sandstorm Visual Effect-沙尘暴视觉效果【Context LoRA】_1856603877087891458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心
- `VAELoader`
- `RandomNoise`
- `BasicScheduler`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `FluxGuidance`
- `Note`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `PreviewImage`
- `TextCombinerSix`
- `LoraLoader` ★核心
- `JjkText`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `RH_Prompter`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RH_Prompter`
- `TextCombinerTwo`
- `JjkText`
- `JjkText`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `sandstorm-visual-effect.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **63%**（22/35）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`TextCombinerSix`、`LoraLoader`、`TextCombinerTwo`、`RH_Prompter`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
