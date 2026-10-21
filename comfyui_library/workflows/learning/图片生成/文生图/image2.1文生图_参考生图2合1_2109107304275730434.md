---
key: 图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json
name: image2.1文生图_参考生图2合1_2109107304275730434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json
hash: b1ded7c191724e06
coverage: 0.966667
learned_at: 2026-10-21 02:57:08
nodes: [SaveImage, LoraLoaderModelOnly, QwenImage21Cache, KSampler, EmptyLatentImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, BatchImagesNode, TextGenerateLTX2Prompt, LoadImage, TextEncodeQwenImage21, llama_cpp_model_loader, easy showAnything, VAEDecode, CLIPLoader, VAELoader, LoraLoaderModelOnly, SaveImageAdvanced, llama_cpp_instruct_adv, UNETLoader, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 386634098772849, "steps": 20, "width": 1024}
---

# 图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `TextEncodeQwenImage21`
- `llama_cpp_model_loader`
- `easy showAnything`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImageAdvanced`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `386634098772849`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`SaveImage`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImageAdvanced`、`llama_cpp_instruct_adv`、`UNETLoader`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
