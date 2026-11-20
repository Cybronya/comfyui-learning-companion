---
key: 平台全量/Portrait Illustration-肖像插图【Context LoRA】_1856600733977366529.json
name: Portrait Illustration-肖像插图【Context LoRA】_1856600733977366529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Portrait Illustration-肖像插图【Context LoRA】_1856600733977366529.json
hash: 500261cce85bae8a
coverage: 0.675676
learned_at: 2026-11-14 00:48:28
nodes: [DualCLIPLoader, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, FluxGuidance, Note, VAEDecode, Label (rgthree), Label (rgthree), LoraLoader, PreviewImage, JjkText, JjkText, JjkText, ShowText|pysssss, TextCombinerSix, CLIPTextEncode, RH_Prompter, RH_Prompter, TextCombinerTwo, ShowText|pysssss, TextCombinerTwo, TextCombinerTwo, JjkText, JjkText, UNETLoader, Note, ShowText|pysssss, TextCombinerTwo, FluxResolutionNode, JjkText]
patterns: [lora]
missing: []
parameters: {"lora_name": "portrait-illustration.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Portrait Illustration-肖像插图【Context LoRA】_1856600733977366529.json

> 来源文件 `comfyui_library/workflows/平台全量/Portrait Illustration-肖像插图【Context LoRA】_1856600733977366529.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `DualCLIPLoader`
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
- `LoraLoader` ★核心
- `PreviewImage`
- `JjkText`
- `JjkText`
- `JjkText`
- `ShowText|pysssss`
- `TextCombinerSix`
- `CLIPTextEncode` ★核心
- `RH_Prompter`
- `RH_Prompter`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `JjkText`
- `UNETLoader` ★核心
- `Note`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `FluxResolutionNode`
- `JjkText`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `portrait-illustration.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **68%**（25/37）

**有卡**：`DualCLIPLoader`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`LoraLoader`、`TextCombinerSix`、`CLIPTextEncode`、`RH_Prompter`、`TextCombinerTwo`、`UNETLoader`、`FluxResolutionNode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
