---
key: 图片生成/文生图/Flux-t2i+i2i+Lora-2025.10.22_1995696940283203585.json
name: Flux-t2i+i2i+Lora-2025.10.22_1995696940283203585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux-t2i+i2i+Lora-2025.10.22_1995696940283203585.json
hash: ca9e4fe341665889
coverage: 0.692308
learned_at: 2026-10-19 21:32:31
nodes: [KSamplerSelect, BasicScheduler, BasicGuider, EmptyLatentImage, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), easy showAnything, VAEEncode, SetNode, GetNode, GetNode, SetNode, CLIPTextEncodeFlux, easy imageSave, GetNode, GetNode, SetNode, VAEDecode, SamplerCustomAdvanced, RandomNoise, GetNode, GetNode, SetNode, Note Plus (mtb), GoogleTranslateTextNode, TextInput_, TextInput_, TextInput_, TextInput_, TextInput_, TextInput_, TextInput_, text-util-join-text, SetNode, SetNode, VAELoader, Anything Everywhere, UNETLoader, DualCLIPLoader, Label (rgthree), Label (rgthree), LoraLoader, Fast Groups Bypasser (rgthree), 孤海图像组合批次, LoadImage, Reroute, ImageResize+]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "krea 超级模特.safetensors", "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 图片生成/文生图/Flux-t2i+i2i+Lora-2025.10.22_1995696940283203585.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux-t2i+i2i+Lora-2025.10.22_1995696940283203585.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `EmptyLatentImage` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `easy showAnything`
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncodeFlux` ★核心
- `easy imageSave`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note Plus (mtb)`
- `GoogleTranslateTextNode`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `text-util-join-text`
- `SetNode`
- `SetNode`
- `VAELoader`
- `Anything Everywhere`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoraLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `孤海图像组合批次`
- `LoadImage`
- `Reroute`
- `ImageResize+`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `krea 超级模特.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **69%**（36/52）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`EmptyLatentImage`、`Label (rgthree)`、`VAEEncode`、`CLIPTextEncodeFlux`、`easy imageSave`、`VAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`Note Plus (mtb)`、`GoogleTranslateTextNode`、`TextInput_`、`text-util-join-text`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`孤海图像组合批次`、`LoadImage`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、KSamplerSelect、SamplerCustomAdvanced、CLIPTextEncodeFlux
