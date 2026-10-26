---
key: 图片生成/图生图/qwen-image-2.1-二次元转真人_2114273703994413058.json
name: qwen-image-2.1-二次元转真人_2114273703994413058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-二次元转真人_2114273703994413058.json
hash: 5a0401038806a286
coverage: 0.887324
learned_at: 2026-10-26 22:04:17
nodes: [CLIPLoader, CLIPLoader, VAELoader, UNETLoader, ProcessString, JDCN_StringToList, ResolutionSelector, ExtractBeforeAfter, LayerUtility: ColorImage V2, BlockifyMask, Mask Fill Holes, PreviewBridge, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAsV2, VOSR2ModelLoader, QwenImage21Cache, BasicGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAELoader, ExtractBeforeAfter, VOSR2Upscale, llama_cpp_parameters, llama_cpp_model_loader, easy positive, easy positive, Seed (rgthree), easy showAnything, llama_cpp_instruct_adv, UNETLoader, ImageScaleToTotalPixelsX, VAELoader, UpscaleModelLoader, UpscaleModelLoader, ImageUpscaleWithModel, Reroute, ImageUpscaleWithModel, EmptyLatentImage, PreviewImage, BasicScheduler, CLIPLoader, VAEDecode, AIO_Preprocessor, easy imageSizeBySide, ExtractBeforeAfter, UNETLoader, ReferenceLatent, VAEEncode, TextGenerateLTX2Prompt, KSampler, ExtractBeforeAfter, CLIPLoader, VAEDecode, TextEncodeQwenImage21, PreviewImage, UNETLoader, easy positive, ImageScaleToTotalPixelsX, ImageConcanate, ImageBlend, SaveImage, PreviewImage, PreviewImage, easy showAnything, LoadImage, CLIPTextEncode, PreviewImage, ColorMatchV2, easy positive, ColorMatchV2]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 215720823243046, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-2.1-二次元转真人_2114273703994413058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1-二次元转真人_2114273703994413058.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ProcessString`
- `JDCN_StringToList`
- `ResolutionSelector`
- `ExtractBeforeAfter`
- `LayerUtility: ColorImage V2`
- `BlockifyMask`
- `Mask Fill Holes`
- `PreviewBridge`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAsV2`
- `VOSR2ModelLoader`
- `QwenImage21Cache`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `ExtractBeforeAfter`
- `VOSR2Upscale`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `easy positive`
- `easy positive`
- `Seed (rgthree)`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixelsX`
- `VAELoader`
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Reroute`
- `ImageUpscaleWithModel`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `BasicScheduler`
- `CLIPLoader`
- `VAEDecode` ★核心
- `AIO_Preprocessor`
- `easy imageSizeBySide`
- `ExtractBeforeAfter`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `ExtractBeforeAfter`
- `CLIPLoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `PreviewImage`
- `UNETLoader` ★核心
- `easy positive`
- `ImageScaleToTotalPixelsX`
- `ImageConcanate`
- `ImageBlend`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ColorMatchV2`
- `easy positive`
- `ColorMatchV2`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `215720823243046`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（63/71）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ProcessString`、`JDCN_StringToList`、`ResolutionSelector`、`ExtractBeforeAfter`、`LayerUtility: ColorImage V2`、`BlockifyMask`、`Mask Fill Holes`、`PreviewBridge`、`LayerUtility: ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`VOSR2ModelLoader`、`QwenImage21Cache`、`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`VOSR2Upscale`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy positive`、`Seed (rgthree)`、`llama_cpp_instruct_adv`、`ImageScaleToTotalPixelsX`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`EmptyLatentImage`、`BasicScheduler`、`VAEDecode`、`AIO_Preprocessor`、`easy imageSizeBySide`、`ReferenceLatent`、`VAEEncode`、`TextGenerateLTX2Prompt`、`KSampler`、`TextEncodeQwenImage21`、`ImageConcanate`、`ImageBlend`、`SaveImage`、`LoadImage`、`CLIPTextEncode`、`ColorMatchV2`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
