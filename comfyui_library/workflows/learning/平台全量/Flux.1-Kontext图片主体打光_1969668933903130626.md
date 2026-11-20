---
key: 平台全量/Flux.1-Kontext图片主体打光_1969668933903130626.json
name: Flux.1-Kontext图片主体打光_1969668933903130626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1-Kontext图片主体打光_1969668933903130626.json
hash: aaea3eaa7b063f1f
coverage: 0.846154
learned_at: 2026-11-14 00:28:50
nodes: [VAELoader, ConditioningZeroOut, SaveImage, ReferenceLatent, DualCLIPLoader, RepeatLatentBatch, FluxKontextImageScale, CLIPTextEncode, RH_Translator, TTP_text_mix, ImpactSwitch, ShowText|pysssss, RH_Captioner, TextInput_, Reroute, SaveImage, UNETLoader, LoraLoader, VAEEncode, FluxGuidance, ColorMatch, ImageConcanate, VAEDecode, PreviewImage, KSampler, LoadAndResizeImage]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "触发词（rongtudaguang）.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 595640966208326, "steps": 20, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Flux.1-Kontext图片主体打光_1969668933903130626.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1-Kontext图片主体打光_1969668933903130626.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `SaveImage`
- `ReferenceLatent`
- `DualCLIPLoader`
- `RepeatLatentBatch`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `TTP_text_mix`
- `ImpactSwitch`
- `ShowText|pysssss`
- `RH_Captioner`
- `TextInput_`
- `Reroute`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `ColorMatch`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `LoadAndResizeImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `触发词（rongtudaguang）.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `595640966208326`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`SaveImage`、`ReferenceLatent`、`DualCLIPLoader`、`RepeatLatentBatch`、`FluxKontextImageScale`、`CLIPTextEncode`、`RH_Translator`、`TTP_text_mix`、`RH_Captioner`、`TextInput_`、`UNETLoader`、`LoraLoader`、`VAEEncode`、`FluxGuidance`、`ColorMatch`、`ImageConcanate`、`VAEDecode`、`KSampler`、`LoadAndResizeImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、ReferenceLatent
