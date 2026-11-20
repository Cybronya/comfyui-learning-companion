---
key: 平台全量/Runninghub Oneshot Prompter_1872524884764192770.json
name: Runninghub Oneshot Prompter_1872524884764192770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Runninghub Oneshot Prompter_1872524884764192770.json
hash: 6029c41cde66eedf
coverage: 0.9
learned_at: 2026-11-14 00:54:59
nodes: [VAEDecode, CLIPTextEncode, FluxGuidance, BasicGuider, RandomNoise, EmptyLatentImage, SamplerCustomAdvanced, BasicScheduler, SaveImage, ShowText|pysssss, TextCombinerTwo, RH_Prompter, Label (rgthree), RH_Prompter, TextCombinerTwo, ShowText|pysssss, DualCLIPLoader, TextCombinerTwo, LoraLoader, VAELoader, UNETLoader, KSamplerSelect, Label (rgthree), Label (rgthree), FluxResolutionNode, Label (rgthree), Label (rgthree), JjkText, RH_OneShot_Prompter, Label (rgthree)]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1280, "lora_name": "扁平黑白线稿插画_简约黑白线稿插画.safetensors", "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 平台全量/Runninghub Oneshot Prompter_1872524884764192770.json

> 来源文件 `comfyui_library/workflows/平台全量/Runninghub Oneshot Prompter_1872524884764192770.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `BasicGuider`
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `SaveImage`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `RH_Prompter`
- `Label (rgthree)`
- `RH_Prompter`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `DualCLIPLoader`
- `TextCombinerTwo`
- `LoraLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `FluxResolutionNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `JjkText`
- `RH_OneShot_Prompter`
- `Label (rgthree)`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `lora_name` = `扁平黑白线稿插画_简约黑白线稿插画.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`BasicGuider`、`RandomNoise`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`BasicScheduler`、`SaveImage`、`TextCombinerTwo`、`RH_Prompter`、`Label (rgthree)`、`DualCLIPLoader`、`LoraLoader`、`VAELoader`、`UNETLoader`、`KSamplerSelect`、`FluxResolutionNode`、`RH_OneShot_Prompter`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
