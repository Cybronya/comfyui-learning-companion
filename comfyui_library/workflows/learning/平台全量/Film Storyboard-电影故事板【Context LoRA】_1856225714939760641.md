---
key: 平台全量/Film Storyboard-电影故事板【Context LoRA】_1856225714939760641.json
name: Film Storyboard-电影故事板【Context LoRA】_1856225714939760641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Film Storyboard-电影故事板【Context LoRA】_1856225714939760641.json
hash: c682b0f4cb593a78
coverage: 0.567568
learned_at: 2026-11-14 00:26:41
nodes: [TextCombinerTwo, TextCombinerSix, JjkText, JjkText, JjkText, UNETLoader, DualCLIPLoader, CLIPTextEncode, KSamplerSelect, VAELoader, RandomNoise, SaveImage, TextCombinerSix, FluxGuidance, ShowText|pysssss, Note, VAEDecode, Label (rgthree), Label (rgthree), Note, JjkText, BasicScheduler, JjkText, PrimitiveNode, ModelSamplingFlux, SamplerCustomAdvanced, BasicGuider, JjkText, LoraLoader, JjkText, JjkText, JjkText, JjkText, EmptySD3LatentImage, PreviewImage, PatchModelAddDownscale, PrimitiveNode]
patterns: [lora]
missing: []
parameters: {"lora_name": "film-storyboard.safetensors", "strength_clip": 1, "strength_model": 0.65}
---

# 平台全量/Film Storyboard-电影故事板【Context LoRA】_1856225714939760641.json

> 来源文件 `comfyui_library/workflows/平台全量/Film Storyboard-电影故事板【Context LoRA】_1856225714939760641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `TextCombinerTwo`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `JjkText`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `RandomNoise`
- `SaveImage`
- `TextCombinerSix`
- `FluxGuidance`
- `ShowText|pysssss`
- `Note`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `JjkText`
- `BasicScheduler`
- `JjkText`
- `PrimitiveNode`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `JjkText`
- `LoraLoader` ★核心
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `EmptySD3LatentImage`
- `PreviewImage`
- `PatchModelAddDownscale`
- `PrimitiveNode`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `film-storyboard.safetensors`
- `strength_model` = `0.65`
- `strength_clip` = `1`

## 知识

覆盖率 **57%**（21/37）

**有卡**：`TextCombinerTwo`、`TextCombinerSix`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`Label (rgthree)`、`BasicScheduler`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`BasicGuider`、`LoraLoader`、`EmptySD3LatentImage`、`PatchModelAddDownscale`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
