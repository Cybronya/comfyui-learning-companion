---
key: 图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json
name: qwen-image-2.1-姿态迁移_2103296254561308673
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json
hash: a0979b79617473ca
coverage: 0.927273
learned_at: 2026-10-21 00:46:05
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, UNETLoader, UNETLoader, llama_cpp_parameters, BasicScheduler, CLIPLoader, TextGenerateLTX2Prompt, ProcessString, JDCN_StringToList, CLIPTextEncode, VAEEncode, KSampler, RandomNoise, UNETLoader, ColorMatchV2, ResolutionSelector, ExtractBeforeAfter, VAEDecode, SDPoseOODProcessor, SDPoseOODLoader, ImageScaleToTotalPixelsX, Image Comparer (rgthree), SDVN RGBA to RGB, VOSR2ModelLoader, PreviewImage, ImageScaleToTotalPixelsX, llama_cpp_instruct_adv, llama_cpp_model_loader, EmptyLatentImage, SaveImage, PreviewImage, LoadImage, LoadImage, VOSR2Upscale, ExtractBeforeAfter, easy positive, ImageScaleToTotalPixelsX, easy positive, easy showAnything, TextEncodeQwenImage21, ImageBatchMulti, PreviewBridge, ImageScaleToTotalPixelsX, Seed (rgthree)]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 660901167240087, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `llama_cpp_parameters`
- `BasicScheduler`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ProcessString`
- `JDCN_StringToList`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `ColorMatchV2`
- `ResolutionSelector`
- `ExtractBeforeAfter`
- `VAEDecode` ★核心
- `SDPoseOODProcessor`
- `SDPoseOODLoader`
- `ImageScaleToTotalPixelsX`
- `Image Comparer (rgthree)`
- `SDVN RGBA to RGB`
- `VOSR2ModelLoader`
- `PreviewImage`
- `ImageScaleToTotalPixelsX`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `VOSR2Upscale`
- `ExtractBeforeAfter`
- `easy positive`
- `ImageScaleToTotalPixelsX`
- `easy positive`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `ImageBatchMulti`
- `PreviewBridge`
- `ImageScaleToTotalPixelsX`
- `Seed (rgthree)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `660901167240087`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（51/55）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`VAEDecode`、`UNETLoader`、`llama_cpp_parameters`、`BasicScheduler`、`TextGenerateLTX2Prompt`、`ProcessString`、`JDCN_StringToList`、`CLIPTextEncode`、`VAEEncode`、`KSampler`、`RandomNoise`、`ColorMatchV2`、`ResolutionSelector`、`ExtractBeforeAfter`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`ImageScaleToTotalPixelsX`、`SDVN RGBA to RGB`、`VOSR2ModelLoader`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`EmptyLatentImage`、`SaveImage`、`LoadImage`、`VOSR2Upscale`、`easy positive`、`TextEncodeQwenImage21`、`ImageBatchMulti`、`PreviewBridge`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector
