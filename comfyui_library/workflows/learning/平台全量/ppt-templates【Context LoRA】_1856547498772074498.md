---
key: 平台全量/ppt-templates【Context LoRA】_1856547498772074498.json
name: ppt-templates【Context LoRA】_1856547498772074498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ppt-templates【Context LoRA】_1856547498772074498.json
hash: fbeb850c075efbc7
coverage: 0.540541
learned_at: 2026-11-14 01:15:51
nodes: [TextCombinerTwo, TextCombinerSix, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingFlux, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, BasicGuider, SamplerCustomAdvanced, SaveImage, TextCombinerSix, FluxGuidance, VAEDecode, Label (rgthree), Label (rgthree), Note, UNETLoader, DualCLIPLoader, Note, PrimitiveNode, ShowText|pysssss, JjkText, LoraLoader, JjkText, JjkText, PrimitiveNode, JjkText, ShowText|pysssss, JjkText, JjkText, JjkText, PreviewImage, JjkText, JjkText, JjkText]
patterns: [lora]
missing: []
parameters: {"lora_name": "ppt-templates.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/ppt-templates【Context LoRA】_1856547498772074498.json

> 来源文件 `comfyui_library/workflows/平台全量/ppt-templates【Context LoRA】_1856547498772074498.json`

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
- `Note`
- `PrimitiveNode`
- `ShowText|pysssss`
- `JjkText`
- `LoraLoader` ★核心
- `JjkText`
- `JjkText`
- `PrimitiveNode`
- `JjkText`
- `ShowText|pysssss`
- `JjkText`
- `JjkText`
- `JjkText`
- `PreviewImage`
- `JjkText`
- `JjkText`
- `JjkText`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `ppt-templates.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **54%**（20/37）

**有卡**：`TextCombinerTwo`、`TextCombinerSix`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
