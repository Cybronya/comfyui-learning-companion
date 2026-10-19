---
key: 图片生成/文生图/Z-image DetailedEyes Lora权重对比工作流_1994403733771591682.json
name: Z-image DetailedEyes Lora权重对比工作流_1994403733771591682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image DetailedEyes Lora权重对比工作流_1994403733771591682.json
hash: 58459ff258510b96
coverage: 0.970588
learned_at: 2026-10-19 21:32:54
nodes: [CLIPLoader, ConditioningZeroOut, KSampler, VAELoader, easy promptLine, CLIPTextEncode, EmptyLatentImage, LayerUtility: PurgeVRAM, VAEDecode, VAEDecode, Text Concatenate, Seed (rgthree), easy showAnything, RH_LLMAPI_Pro_Node, Image Compare (mtb), CR Prompt Text, SaveImage, KSampler, KSampler, SaveImage, ImageConcanate, VAEDecode, UNETLoader, LoraLoaderModelOnly, ImageConcanate, LayerUtility: PurgeVRAM, SaveImage, CR Prompt Text, LoraLoaderModelOnly, SaveImage, Image Compare (mtb), SaveImage, SaveImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 720384980245694, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-image DetailedEyes Lora权重对比工作流_1994403733771591682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image DetailedEyes Lora权重对比工作流_1994403733771591682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `easy promptLine`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Text Concatenate`
- `Seed (rgthree)`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `Image Compare (mtb)`
- `CR Prompt Text`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Compare (mtb)`
- `SaveImage`
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `720384980245694`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`easy promptLine`、`CLIPTextEncode`、`EmptyLatentImage`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`Text Concatenate`、`Seed (rgthree)`、`RH_LLMAPI_Pro_Node`、`Image Compare (mtb)`、`CR Prompt Text`、`SaveImage`、`ImageConcanate`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
