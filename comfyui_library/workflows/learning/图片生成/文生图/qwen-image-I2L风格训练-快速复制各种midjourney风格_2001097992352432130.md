---
key: 图片生成/文生图/qwen-image-I2L风格训练-快速复制各种midjourney风格_2001097992352432130.json
name: qwen-image-I2L风格训练-快速复制各种midjourney风格_2001097992352432130
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-I2L风格训练-快速复制各种midjourney风格_2001097992352432130.json
hash: 2dba2a516d36edb0
coverage: 0.789474
learned_at: 2026-10-19 21:47:20
nodes: [LoadImage, PreviewAny, LoadImage, LoadImage, LoadImage, LoadImage, ImageTile+, ImageFromBatch+, SeedVR2VideoUpscaler, easy cleanGpuUsed, RunningHub_ImageQwenI2L_LoraGenerator, VAELoader, CLIPTextEncode, CLIPTextEncode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageBatchMulti, CLIPLoader, VAEDecode, easy showAnything, easy showAnything, LoadImage, SaveImage, LoadImage, UNETLoader, LoraLoaderModelOnly, PreviewBridge, EmptyLatentImage, LoraLoaderModelOnly, AILab_QwenVL, Note, easy ifElse, PreviewBridge, PrimitiveNode, Note, KSampler, Note, RunningHub_ImageQwenI2L_Loader(Style)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 4520, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image-I2L风格训练-快速复制各种midjourney风格_2001097992352432130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-I2L风格训练-快速复制各种midjourney风格_2001097992352432130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LoadImage`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageTile+`
- `ImageFromBatch+`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `RunningHub_ImageQwenI2L_LoraGenerator`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageBatchMulti`
- `CLIPLoader`
- `VAEDecode` ★核心
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewBridge`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL`
- `Note`
- `easy ifElse`
- `PreviewBridge`
- `PrimitiveNode`
- `Note`
- `KSampler` ★核心
- `Note`
- `RunningHub_ImageQwenI2L_Loader(Style)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `4520`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **79%**（30/38）

**有卡**：`LoadImage`、`ImageTile+`、`ImageFromBatch+`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`RunningHub_ImageQwenI2L_LoraGenerator`、`VAELoader`、`CLIPTextEncode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageBatchMulti`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`PreviewBridge`、`EmptyLatentImage`、`AILab_QwenVL`、`KSampler`、`RunningHub_ImageQwenI2L_Loader(Style)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
