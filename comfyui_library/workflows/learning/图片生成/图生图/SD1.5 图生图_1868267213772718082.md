---
key: 图片生成/图生图/SD1.5 图生图_1868267213772718082.json
name: SD1.5 图生图_1868267213772718082
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5 图生图_1868267213772718082.json
hash: a45f10647c17a2df
coverage: 0.742857
learned_at: 2026-10-23 11:23:31
nodes: [Reroute, DWPreprocessor, PreviewImage, LineArtPreprocessor, Zoe-DepthMapPreprocessor, PreviewImage, ControlNetApplyAdvanced, Canny, PreviewImage, ControlNetApplyAdvanced, M-LSDPreprocessor, PreviewImage, ControlNetApplyAdvanced, PreviewImage, ControlNetApplyAdvanced, ControlNetApplyAdvanced, VAEEncode, CLIPTextEncode, Reroute, Reroute, VAEDecode, SaveImage, ControlNetApplyAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LatentUpscaleBy, CLIPTextEncode, WD14Tagger|pysssss, Reroute, Mute / Bypass Repeater (rgthree), easy showAnything, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Reroute, StringFunction|pysssss, LoadImage, Text Concatenate (JPS), CheckpointLoaderSimple, LoraLoader, Reroute, IPAdapterModelLoader, CLIPVisionLoader, IPAdapterAdvanced, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), KSampler, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, DeepTranslatorTextNode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), ControlNetLoader, Fast Bypasser (rgthree), Fast Bypasser (rgthree)]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 2, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 0.6, "lora_name": "露珠花朵 __ SD1.5_V1.0.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1071975265509578, "steps": 30, "strength_clip": 1, "strength_model": 0.8}
---

# 图片生成/图生图/SD1.5 图生图_1868267213772718082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5 图生图_1868267213772718082.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `Reroute`
- `DWPreprocessor`
- `PreviewImage`
- `LineArtPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `Canny`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `M-LSDPreprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LatentUpscaleBy`
- `CLIPTextEncode` ★核心
- `WD14Tagger|pysssss`
- `Reroute`
- `Mute / Bypass Repeater (rgthree)`
- `easy showAnything`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Reroute`
- `StringFunction|pysssss`
- `LoadImage`
- `Text Concatenate (JPS)`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `Reroute`
- `IPAdapterModelLoader`
- `CLIPVisionLoader`
- `IPAdapterAdvanced`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `KSampler` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `ControlNetLoader`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`

**识别到的模式**：image_to_image、lora

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`
- `lora_name` = `露珠花朵 __ SD1.5_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `seed` = `1071975265509578`
- `steps` = `30`
- `cfg` = `2`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.6`

## 知识

覆盖率 **74%**（52/70）

**有卡**：`DWPreprocessor`、`LineArtPreprocessor`、`Zoe-DepthMapPreprocessor`、`ControlNetApplyAdvanced`、`Canny`、`M-LSDPreprocessor`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`LatentUpscaleBy`、`WD14Tagger|pysssss`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`StringFunction|pysssss`、`LoadImage`、`Text Concatenate (JPS)`、`CheckpointLoaderSimple`、`LoraLoader`、`IPAdapterModelLoader`、`CLIPVisionLoader`、`IPAdapterAdvanced`、`KSampler`、`ControlNetLoader`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、Canny
