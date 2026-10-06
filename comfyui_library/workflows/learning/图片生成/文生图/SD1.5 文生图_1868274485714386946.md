---
key: 图片生成/文生图/SD1.5 文生图_1868274485714386946.json
name: SD1.5 文生图_1868274485714386946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5 文生图_1868274485714386946.json
hash: 5d1ec0e38aba351d
coverage: 0.42029
learned_at: 2026-10-07 03:05:16
nodes: [Reroute, DWPreprocessor, PreviewImage, LineArtPreprocessor, Zoe-DepthMapPreprocessor, PreviewImage, ControlNetApplyAdvanced, Canny, PreviewImage, ControlNetApplyAdvanced, M-LSDPreprocessor, PreviewImage, ControlNetApplyAdvanced, PreviewImage, ControlNetApplyAdvanced, ControlNetApplyAdvanced, Reroute, VAEDecode, ControlNetApplyAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, WD14Tagger|pysssss, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Reroute, StringFunction|pysssss, CheckpointLoaderSimple, LoraLoader, Reroute, IPAdapterModelLoader, CLIPVisionLoader, IPAdapterAdvanced, Mute / Bypass Repeater (rgthree), ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, DeepTranslatorTextNode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), ControlNetLoader, Fast Bypasser (rgthree), Fast Bypasser (rgthree), KSampler, Fast Bypasser (rgthree), SaveImage, EmptyLatentImage, LoadImage, LoadImage, Fast Bypasser (rgthree), easy showAnything, easy showAnything, Text Concatenate (JPS), CLIPTextEncode]
patterns: [text_to_image, lora]
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), M-LSDPreprocessor, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), StringFunction|pysssss, Text Concatenate (JPS), WD14Tagger|pysssss, Zoe-DepthMapPreprocessor]
parameters: {"batch_size": 4, "cfg": 2, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 768, "lora_name": "露珠花朵 __ SD1.5_V1.0.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 85704773157185, "steps": 30, "strength_clip": 1, "strength_model": 0.8, "width": 512}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `M-LSDPreprocessor` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Zoe-DepthMapPreprocessor` 仅有 ControlNet 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/SD1.5 文生图_1868274485714386946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5 文生图_1868274485714386946.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（69 个）：
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
- `Reroute`
- `VAEDecode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `WD14Tagger|pysssss`
- `Mute / Bypass Repeater (rgthree)`
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
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `Reroute`
- `IPAdapterModelLoader`
- `CLIPVisionLoader`
- `IPAdapterAdvanced`
- `Mute / Bypass Repeater (rgthree)`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `ControlNetLoader`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `KSampler` ★核心
- `Fast Bypasser (rgthree)`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `easy showAnything`
- `easy showAnything`
- `Text Concatenate (JPS)`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`
- `lora_name` = `露珠花朵 __ SD1.5_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `seed` = `85704773157185`
- `steps` = `30`
- `cfg` = `2`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `512`
- `height` = `768`
- `batch_size` = `4`

## 知识

覆盖率 **42%**（29/69）

**有卡**：`DWPreprocessor`、`LineArtPreprocessor`、`ControlNetApplyAdvanced`、`Canny`、`VAEDecode`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoader`、`IPAdapterModelLoader`、`CLIPVisionLoader`、`IPAdapterAdvanced`、`ControlNetLoader`、`DeepTranslatorTextNode`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`LoadImage`

**缺卡**（23）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`M-LSDPreprocessor`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`StringFunction|pysssss`、`Text Concatenate (JPS)`、`WD14Tagger|pysssss`、`Zoe-DepthMapPreprocessor`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `M-LSDPreprocessor` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Zoe-DepthMapPreprocessor` 仅有 ControlNet 的通用知识，没有该节点自己的说明
