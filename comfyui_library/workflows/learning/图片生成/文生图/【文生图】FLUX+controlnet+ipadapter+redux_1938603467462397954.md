---
key: 【文生图】FLUX+controlnet+ipadapter+redux_1938603467462397954.json
name: 【文生图】FLUX+controlnet+ipadapter+redux_1938603467462397954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【文生图】FLUX+controlnet+ipadapter+redux_1938603467462397954.json
hash: a318cd63c0a15e4f
coverage: 0.96
learned_at: 2026-10-10 20:59:31
nodes: [OpenposePreprocessor, ControlNetLoader, CLIPVisionLoader, StyleModelLoader, ReduxAdvanced, ControlNetApplyAdvanced, AIO_Preprocessor, ControlNetApplyAdvanced, UNETLoader, DualCLIPLoader, CLIPTextEncode, LoraLoader, SaveImage, CLIPTextEncodeFlux, VAEDecode, GetImageSize, EmptyLatentImage, VAELoader, LoadImage, IPAdapterFluxLoader, ApplyIPAdapterFlux, KSampler //Inspire, RH_Translator, LoraLoader, LoadImage]
patterns: [lora]
missing: [KSampler //Inspire]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "height": 1600, "lora_name": "动漫男生青春校园心动白月光小说推文_V1.0.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 478294621246577, "steps": 8, "strength_clip": 1, "strength_model": 0.8, "width": 1200}
discoveries: [核心节点 `KSampler //Inspire` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 【文生图】FLUX+controlnet+ipadapter+redux_1938603467462397954.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【文生图】FLUX+controlnet+ipadapter+redux_1938603467462397954.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `OpenposePreprocessor`
- `ControlNetLoader`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `ReduxAdvanced`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `SaveImage`
- `CLIPTextEncodeFlux` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `LoadImage`
- `IPAdapterFluxLoader`
- `ApplyIPAdapterFlux`
- `KSampler //Inspire` ★核心
- `RH_Translator`
- `LoraLoader` ★核心
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `lora_name` = `动漫男生青春校园心动白月光小说推文_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`
- `seed` = `478294621246577`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`OpenposePreprocessor`、`ControlNetLoader`、`CLIPVisionLoader`、`StyleModelLoader`、`ReduxAdvanced`、`ControlNetApplyAdvanced`、`AIO_Preprocessor`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`LoraLoader`、`SaveImage`、`CLIPTextEncodeFlux`、`VAEDecode`、`GetImageSize`、`EmptyLatentImage`、`VAELoader`、`LoadImage`、`IPAdapterFluxLoader`、`ApplyIPAdapterFlux`、`RH_Translator`

**缺卡**（1）：`KSampler //Inspire`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 学习发现

- 核心节点 `KSampler //Inspire` 仅有 KSampler 的通用知识，没有该节点自己的说明
