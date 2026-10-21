---
key: 图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json
name: Zimage 直出真实感网红图片 林耀3.18_2034176377439653889
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json
hash: ceb07ca2cd45eec7
coverage: 0.863636
learned_at: 2026-10-21 02:56:34
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, KSampler, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, PreviewImage, ImageScaleToTotalPixels, llama_cpp_model_loader, ShowText|pysssss, llama_cpp_instruct_adv, SaveImage, EmptyLatentImage, SeedVR2VideoUpscaler, LoadImage, Image Comparer (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1234, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1234`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`KSampler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VAEDecode`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`SaveImage`、`EmptyLatentImage`、`SeedVR2VideoUpscaler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
