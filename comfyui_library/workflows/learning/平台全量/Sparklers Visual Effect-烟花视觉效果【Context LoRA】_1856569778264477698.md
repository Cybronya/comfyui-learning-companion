---
key: 平台全量/Sparklers Visual Effect-烟花视觉效果【Context LoRA】_1856569778264477698.json
name: Sparklers Visual Effect-烟花视觉效果【Context LoRA】_1856569778264477698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Sparklers Visual Effect-烟花视觉效果【Context LoRA】_1856569778264477698.json
hash: 9cafbdf06154375e
coverage: 0.628571
learned_at: 2026-11-14 01:00:49
nodes: [UNETLoader, DualCLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, FluxGuidance, Note, VAEDecode, Label (rgthree), Label (rgthree), Note, PrimitiveNode, PrimitiveNode, PreviewImage, LoraLoader, ShowText|pysssss, TextCombinerSix, JjkText, JjkText, JjkText, TextCombinerTwo, ShowText|pysssss, RH_Prompter, TextCombinerTwo, RH_Prompter, ShowText|pysssss, JjkText, JjkText]
patterns: [lora]
missing: []
parameters: {"lora_name": "sparklers-visual-effect.safetensors", "strength_clip": 1, "strength_model": 0.85}
---

# 平台全量/Sparklers Visual Effect-烟花视觉效果【Context LoRA】_1856569778264477698.json

> 来源文件 `comfyui_library/workflows/平台全量/Sparklers Visual Effect-烟花视觉效果【Context LoRA】_1856569778264477698.json`

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
- `LoraLoader` ★核心
- `ShowText|pysssss`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `RH_Prompter`
- `TextCombinerTwo`
- `RH_Prompter`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `sparklers-visual-effect.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `1`

## 知识

覆盖率 **63%**（22/35）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`LoraLoader`、`TextCombinerSix`、`TextCombinerTwo`、`RH_Prompter`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
