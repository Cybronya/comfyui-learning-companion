---
key: 平台全量/Home Decoration-家居装饰【Context LoRA】_1856281624013836289.json
name: Home Decoration-家居装饰【Context LoRA】_1856281624013836289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Home Decoration-家居装饰【Context LoRA】_1856281624013836289.json
hash: 2f79011c5495b9d5
coverage: 0.555556
learned_at: 2026-11-14 00:32:04
nodes: [TextCombinerTwo, TextCombinerSix, JjkText, UNETLoader, LoraLoader, DualCLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, TextCombinerSix, FluxGuidance, JjkText, JjkText, ShowText|pysssss, Note, VAEDecode, Label (rgthree), Label (rgthree), Note, JjkText, JjkText, PrimitiveNode, PrimitiveNode, JjkText, JjkText, JjkText, JjkText, JjkText, PreviewImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "film-storyboard.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Home Decoration-家居装饰【Context LoRA】_1856281624013836289.json

> 来源文件 `comfyui_library/workflows/平台全量/Home Decoration-家居装饰【Context LoRA】_1856281624013836289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `TextCombinerTwo`
- `TextCombinerSix`
- `JjkText`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
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
- `TextCombinerSix`
- `FluxGuidance`
- `JjkText`
- `JjkText`
- `ShowText|pysssss`
- `Note`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `JjkText`
- `JjkText`
- `PrimitiveNode`
- `PrimitiveNode`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `film-storyboard.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **56%**（20/36）

**有卡**：`TextCombinerTwo`、`TextCombinerSix`、`UNETLoader`、`LoraLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
