---
key: 平台全量/Visual Identity Design-视觉识别设计【Context LoRA】_1856562720681103362.json
name: Visual Identity Design-视觉识别设计【Context LoRA】_1856562720681103362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Visual Identity Design-视觉识别设计【Context LoRA】_1856562720681103362.json
hash: fbd4002babb3188a
coverage: 0.642857
learned_at: 2026-11-14 01:03:26
nodes: [CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, FluxGuidance, Label (rgthree), Label (rgthree), Note, UNETLoader, DualCLIPLoader, Note, LoraLoader, JjkText, JjkText, TextCombinerSix, PrimitiveNode, ShowText|pysssss, PrimitiveNode, PreviewImage, JjkText, VAEDecode, JjkText]
patterns: [lora]
missing: []
parameters: {"lora_name": "visual-identity-design.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Visual Identity Design-视觉识别设计【Context LoRA】_1856562720681103362.json

> 来源文件 `comfyui_library/workflows/平台全量/Visual Identity Design-视觉识别设计【Context LoRA】_1856562720681103362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
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
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Note`
- `LoraLoader` ★核心
- `JjkText`
- `JjkText`
- `TextCombinerSix`
- `PrimitiveNode`
- `ShowText|pysssss`
- `PrimitiveNode`
- `PreviewImage`
- `JjkText`
- `VAEDecode` ★核心
- `JjkText`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `visual-identity-design.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **64%**（18/28）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`Label (rgthree)`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`TextCombinerSix`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
