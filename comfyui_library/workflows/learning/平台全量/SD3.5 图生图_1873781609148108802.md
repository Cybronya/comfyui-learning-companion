---
key: 平台全量/SD3.5 图生图_1873781609148108802.json
name: SD3.5 图生图_1873781609148108802
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SD3.5 图生图_1873781609148108802.json
hash: 763a7c85115a9c73
coverage: 0.9
learned_at: 2026-11-14 00:56:04
nodes: [Joy_caption, Joy_caption_load, StringFunction|pysssss, CLIPTextEncodeFlux, CLIPTextEncode, Text Concatenate (JPS), VAEDecode, easy showAnything, SaveImage, LoadImage, VAEEncode, KSampler, ModelSamplingSD3, ConstrainImage|pysssss, DeepTranslatorTextNode, TripleCLIPLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LoadImage, easy showAnything]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 5, "checkpoint": "sd3.5_large.safetensors", "denoise": 0.65, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 39882636982378, "steps": 35}
---

# 平台全量/SD3.5 图生图_1873781609148108802.json

> 来源文件 `comfyui_library/workflows/平台全量/SD3.5 图生图_1873781609148108802.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Joy_caption`
- `Joy_caption_load`
- `StringFunction|pysssss`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate (JPS)`
- `VAEDecode` ★核心
- `easy showAnything`
- `SaveImage`
- `LoadImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `ConstrainImage|pysssss`
- `DeepTranslatorTextNode`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `39882636982378`
- `steps` = `35`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.65`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`Joy_caption`、`Joy_caption_load`、`StringFunction|pysssss`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`Text Concatenate (JPS)`、`VAEDecode`、`SaveImage`、`LoadImage`、`VAEEncode`、`KSampler`、`ModelSamplingSD3`、`ConstrainImage|pysssss`、`DeepTranslatorTextNode`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、VAEEncode
