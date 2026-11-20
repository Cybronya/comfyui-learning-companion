---
key: 平台全量/SD3.5 文生图_1873755295695425537.json
name: SD3.5 文生图_1873755295695425537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SD3.5 文生图_1873755295695425537.json
hash: 0093a341fa47d012
coverage: 0.888889
learned_at: 2026-11-14 00:56:05
nodes: [Joy_caption, Joy_caption_load, StringFunction|pysssss, LoadImage, CLIPTextEncodeFlux, CLIPTextEncode, Text Concatenate (JPS), easy showAnything, VAEDecode, EmptySD3LatentImage, easy showAnything, SaveImage, KSampler, ModelSamplingSD3, DeepTranslatorTextNode, TripleCLIPLoader, CheckpointLoaderSimple, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 5, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 625573022635547, "steps": 35}
---

# 平台全量/SD3.5 文生图_1873755295695425537.json

> 来源文件 `comfyui_library/workflows/平台全量/SD3.5 文生图_1873755295695425537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `Joy_caption`
- `Joy_caption_load`
- `StringFunction|pysssss`
- `LoadImage`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate (JPS)`
- `easy showAnything`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `easy showAnything`
- `SaveImage`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `DeepTranslatorTextNode`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `625573022635547`
- `steps` = `35`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`Joy_caption`、`Joy_caption_load`、`StringFunction|pysssss`、`LoadImage`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`Text Concatenate (JPS)`、`VAEDecode`、`EmptySD3LatentImage`、`SaveImage`、`KSampler`、`ModelSamplingSD3`、`DeepTranslatorTextNode`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、TripleCLIPLoader
