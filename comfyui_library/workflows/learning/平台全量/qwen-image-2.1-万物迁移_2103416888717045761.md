---
key: 平台全量/qwen-image-2.1-万物迁移_2103416888717045761.json
name: qwen-image-2.1-万物迁移_2103416888717045761
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image-2.1-万物迁移_2103416888717045761.json
hash: d7b45e7ad4ccc6d7
coverage: 0.932203
learned_at: 2026-11-14 01:16:14
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, UNETLoader, UNETLoader, llama_cpp_parameters, BasicScheduler, CLIPLoader, TextGenerateLTX2Prompt, ProcessString, JDCN_StringToList, easy positive, CLIPTextEncode, VAEEncode, KSampler, RandomNoise, ColorMatchV2, ResolutionSelector, ExtractBeforeAfter, VOSR2ModelLoader, VOSR2Upscale, ImageScaleToTotalPixelsX, Image Comparer (rgthree), BlockifyMask, PreviewBridge, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ColorImage V2, Mask Fill Holes, VOSR2ModelLoader, VAEDecode, SDVN RGBA to RGB, SaveImage, VOSR2Upscale, llama_cpp_model_loader, UNETLoader, Seed (rgthree), llama_cpp_instruct_adv, EmptyLatentImage, ImageBatchMulti, TextEncodeQwenImage21, LoadImage, ExtractBeforeAfter, LoadImage, PreviewImage, PreviewImage, easy positive, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, easy showAnything]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 449608257040063, "steps": 25, "width": 1024}
---

# 平台全量/qwen-image-2.1-万物迁移_2103416888717045761.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image-2.1-万物迁移_2103416888717045761.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
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
- `easy positive`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `RandomNoise`
- `ColorMatchV2`
- `ResolutionSelector`
- `ExtractBeforeAfter`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `ImageScaleToTotalPixelsX`
- `Image Comparer (rgthree)`
- `BlockifyMask`
- `PreviewBridge`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ColorImage V2`
- `Mask Fill Holes`
- `VOSR2ModelLoader`
- `VAEDecode` ★核心
- `SDVN RGBA to RGB`
- `SaveImage`
- `VOSR2Upscale`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `Seed (rgthree)`
- `llama_cpp_instruct_adv`
- `EmptyLatentImage` ★核心
- `ImageBatchMulti`
- `TextEncodeQwenImage21`
- `LoadImage`
- `ExtractBeforeAfter`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `easy positive`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `easy showAnything`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `449608257040063`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（55/59）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`VAEDecode`、`UNETLoader`、`llama_cpp_parameters`、`BasicScheduler`、`TextGenerateLTX2Prompt`、`ProcessString`、`JDCN_StringToList`、`easy positive`、`CLIPTextEncode`、`VAEEncode`、`KSampler`、`RandomNoise`、`ColorMatchV2`、`ResolutionSelector`、`ExtractBeforeAfter`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ImageScaleToTotalPixelsX`、`BlockifyMask`、`PreviewBridge`、`LayerUtility: ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ColorImage V2`、`Mask Fill Holes`、`SDVN RGBA to RGB`、`SaveImage`、`llama_cpp_model_loader`、`Seed (rgthree)`、`llama_cpp_instruct_adv`、`EmptyLatentImage`、`ImageBatchMulti`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、ResolutionSelector
