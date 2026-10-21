---
key: 图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json
name: Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json
hash: bb250ebbb4fc2ac9
coverage: 0.894118
learned_at: 2026-10-21 00:42:37
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, VAELoader, CLIPLoader, CLIPLoader, VAELoader, VAEDecode, UNETLoader, UNETLoader, llama_cpp_parameters, BasicScheduler, CLIPLoader, TextGenerateLTX2Prompt, ProcessString, JDCN_StringToList, CLIPTextEncode, VAEEncode, KSampler, RandomNoise, UNETLoader, ColorMatchV2, ExtractBeforeAfter, ResolutionSelector, ExtractBeforeAfter, VAEDecode, SDPoseOODProcessor, SDPoseOODLoader, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, Image Comparer (rgthree), SDVN RGBA to RGB, VOSR2ModelLoader, PreviewImage, ImageScaleToTotalPixelsX, llama_cpp_instruct_adv, llama_cpp_model_loader, EmptyLatentImage, VOSR2Upscale, SaveImage, PreviewImage, Seed (rgthree), easy showAnything, TextEncodeQwenImage21, PreviewBridge, easy positive, easy positive, ImageScaleToTotalPixelsX, ImageBatchMulti, easy showAnything, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
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
- `ExtractBeforeAfter`
- `ResolutionSelector`
- `ExtractBeforeAfter`
- `VAEDecode` ★核心
- `SDPoseOODProcessor`
- `SDPoseOODLoader`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `Image Comparer (rgthree)`
- `SDVN RGBA to RGB`
- `VOSR2ModelLoader`
- `PreviewImage`
- `ImageScaleToTotalPixelsX`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `EmptyLatentImage` ★核心
- `VOSR2Upscale`
- `SaveImage`
- `PreviewImage`
- `Seed (rgthree)`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `PreviewBridge`
- `easy positive`
- `easy positive`
- `ImageScaleToTotalPixelsX`
- `ImageBatchMulti`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（76/85）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`VAEDecode`、`UNETLoader`、`llama_cpp_parameters`、`BasicScheduler`、`TextGenerateLTX2Prompt`、`ProcessString`、`JDCN_StringToList`、`CLIPTextEncode`、`VAEEncode`、`KSampler`、`RandomNoise`、`ColorMatchV2`、`ExtractBeforeAfter`、`ResolutionSelector`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`ImageScaleToTotalPixelsX`、`SDVN RGBA to RGB`、`VOSR2ModelLoader`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`EmptyLatentImage`、`VOSR2Upscale`、`SaveImage`、`Seed (rgthree)`、`TextEncodeQwenImage21`、`PreviewBridge`、`easy positive`、`ImageBatchMulti`、`LoadImage`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
