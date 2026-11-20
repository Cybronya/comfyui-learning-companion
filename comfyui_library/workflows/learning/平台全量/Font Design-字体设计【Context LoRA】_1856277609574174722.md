---
key: 平台全量/Font Design-字体设计【Context LoRA】_1856277609574174722.json
name: Font Design-字体设计【Context LoRA】_1856277609574174722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Font Design-字体设计【Context LoRA】_1856277609574174722.json
hash: 68993c61ad0da759
coverage: 0.540541
learned_at: 2026-11-14 00:30:42
nodes: [TextCombinerTwo, TextCombinerSix, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, TextCombinerSix, FluxGuidance, VAEDecode, Label (rgthree), Label (rgthree), Note, UNETLoader, DualCLIPLoader, LoraLoader, Note, JjkText, ShowText|pysssss, JjkText, JjkText, PrimitiveNode, PrimitiveNode, ShowText|pysssss, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, PreviewImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "ppt-templates.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Font Design-字体设计【Context LoRA】_1856277609574174722.json

> 来源文件 `comfyui_library/workflows/平台全量/Font Design-字体设计【Context LoRA】_1856277609574174722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `TextCombinerTwo`
- `TextCombinerSix`
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
- `TextCombinerSix`
- `FluxGuidance`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `Note`
- `JjkText`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`
- `PrimitiveNode`
- `PrimitiveNode`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `ppt-templates.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **54%**（20/37）

**有卡**：`TextCombinerTwo`、`TextCombinerSix`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
