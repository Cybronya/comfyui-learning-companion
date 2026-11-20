---
key: 平台全量/Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082.json
name: Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082.json
hash: 1df3bd1bc8d44ffd
coverage: 0.9375
learned_at: 2026-11-14 01:00:41
nodes: [LoraLoader, IPAdapterUnifiedLoader, CheckpointLoaderSimple, ControlNetLoader, PreviewImage, ControlNetApplyAdvanced, KSampler, EmptyLatentImage, VAEDecode, SaveImage, DepthAnythingPreprocessor, LoadImage, CLIPTextEncode, IPAdapterAdvanced, CLIPTextEncode, LoadImage]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 2, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1344, "lora_name": "MJ52.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 1382617123997, "steps": 8, "strength_clip": 1, "strength_model": 1, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082.json

> 来源文件 `comfyui_library/workflows/平台全量/Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（16 个）：
- `LoraLoader` ★核心
- `IPAdapterUnifiedLoader`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `DepthAnythingPreprocessor`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `IPAdapterAdvanced`
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `MJ52.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `controlnet_strength` = `1`
- `seed` = `1382617123997`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `768`
- `height` = `1344`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`LoraLoader`、`IPAdapterUnifiedLoader`、`CheckpointLoaderSimple`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`DepthAnythingPreprocessor`、`LoadImage`、`CLIPTextEncode`、`IPAdapterAdvanced`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
