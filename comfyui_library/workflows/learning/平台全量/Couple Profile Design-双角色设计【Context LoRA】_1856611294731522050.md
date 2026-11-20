---
key: 平台全量/Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050.json
name: Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050.json
hash: 2780ceae8de5211a
coverage: 0.578947
learned_at: 2026-11-14 00:23:00
nodes: [Label (rgthree), Label (rgthree), Note, Note, JjkText, JjkText, JjkText, TextCombinerSix, ShowText|pysssss, PrimitiveNode, PrimitiveNode, UNETLoader, DualCLIPLoader, LoraLoader, EmptySD3LatentImage, ModelSamplingFlux, RandomNoise, CLIPTextEncode, FluxGuidance, BasicGuider, SamplerCustomAdvanced, VAEDecode, KSamplerSelect, VAELoader, BasicScheduler, SaveImage, JjkText, RH_Prompter, RH_Prompter, JjkText, JjkText, ShowText|pysssss, TextCombinerTwo, TextCombinerTwo, ShowText|pysssss, JjkText, JjkText, PreviewImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "couple-profile.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050.json

> 来源文件 `comfyui_library/workflows/平台全量/Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `Note`
- `JjkText`
- `JjkText`
- `JjkText`
- `TextCombinerSix`
- `ShowText|pysssss`
- `PrimitiveNode`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `SaveImage`
- `JjkText`
- `RH_Prompter`
- `RH_Prompter`
- `JjkText`
- `JjkText`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `couple-profile.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **58%**（22/38）

**有卡**：`Label (rgthree)`、`TextCombinerSix`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`RandomNoise`、`CLIPTextEncode`、`FluxGuidance`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`SaveImage`、`RH_Prompter`、`TextCombinerTwo`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
