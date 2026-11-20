---
key: 平台全量/Portrait Photography-人像摄影【Context LoRA】_1856534151095848961.json
name: Portrait Photography-人像摄影【Context LoRA】_1856534151095848961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Portrait Photography-人像摄影【Context LoRA】_1856534151095848961.json
hash: 76663420e61eaea9
coverage: 0.526316
learned_at: 2026-11-14 00:48:29
nodes: [TextCombinerTwo, TextCombinerSix, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, TextCombinerSix, FluxGuidance, VAEDecode, Label (rgthree), Label (rgthree), Note, UNETLoader, DualCLIPLoader, JjkText, JjkText, PrimitiveNode, ShowText|pysssss, JjkText, JjkText, LoraLoader, PrimitiveNode, JjkText, PreviewImage, JjkText, JjkText, JjkText, JjkText, JjkText, Note, Note, ShowText|pysssss]
patterns: [lora]
missing: []
parameters: {"lora_name": "portrait-photography.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Portrait Photography-人像摄影【Context LoRA】_1856534151095848961.json

> 来源文件 `comfyui_library/workflows/平台全量/Portrait Photography-人像摄影【Context LoRA】_1856534151095848961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `JjkText`
- `JjkText`
- `PrimitiveNode`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`
- `LoraLoader` ★核心
- `PrimitiveNode`
- `JjkText`
- `PreviewImage`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `Note`
- `Note`
- `ShowText|pysssss`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `portrait-photography.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **53%**（20/38）

**有卡**：`TextCombinerTwo`、`TextCombinerSix`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
