---
key: 图片生成/图生图/Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657.json
name: Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657.json
hash: 747f0c81fca5d915
coverage: 0.597561
learned_at: 2026-10-23 11:31:11
nodes: [SetNode, CLIPLoader, GetNode, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAEDecode, LayerUtility: PurgeVRAM V2, SetNode, SetNode, VAELoader, GetNode, LayerUtility: PurgeVRAM V2, AIO_Preprocessor, easy showAnything, AIO_Preprocessor, GetNode, CannyEdgePreprocessor, easy imagePixelPerfect, Note, UNETLoader, SetNode, GetNode, ModelPatchLoader, SetNode, CR Prompt Text, Text Concatenate, Text Concatenate, easy showAnything, Note, Note, Note, GetNode, Note, easy seed, Note, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, SetNode, easy showAnything, easy anythingIndexSwitch, PreviewImage, PreviewImage, PreviewImage, Qwen3_VQA, LatentUpscaleBy, CLIPTextEncode, easy cleanGpuUsed, GetImageSize+, CLIPTextEncode, ModelSamplingFlux, UpscaleModelLoader, VAELoader, UltimateSDUpscale, UNETLoader, DualCLIPLoader, RH_Captioner, SDXLPromptStyler, Image Comparer (rgthree), LoraLoader, SaveImage, VAEDecode, Reroute, LoadImage, LoadImage, PreviewImage, KSampler, easy cleanGpuUsed, llama_cpp_parameters, GetNode, llama_cpp_model_loader, SetNode, easy anythingIndexSwitch, llama_cpp_instruct_adv, ShowText|pysssss, CR Prompt Text, QwenImageDiffsynthControlnet, SaveImage, MarkdownNote, Note, Note]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.7000000000000002, "height": 512, "lora_name": "FLUX_实拍家装风格_FLUX_实拍现代风室内家居.safetensors", "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 8932, "steps": 10, "strength_clip": 1, "strength_model": 0.6, "width": 512}
---

# 图片生成/图生图/Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `AIO_Preprocessor`
- `easy showAnything`
- `AIO_Preprocessor`
- `GetNode`
- `CannyEdgePreprocessor`
- `easy imagePixelPerfect`
- `Note`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `ModelPatchLoader`
- `SetNode`
- `CR Prompt Text`
- `Text Concatenate`
- `Text Concatenate`
- `easy showAnything`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `Note`
- `easy seed`
- `Note`
- `GetNode`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Qwen3_VQA`
- `LatentUpscaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `GetImageSize+`
- `CLIPTextEncode` ★核心
- `ModelSamplingFlux`
- `UpscaleModelLoader`
- `VAELoader`
- `UltimateSDUpscale`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `RH_Captioner`
- `SDXLPromptStyler`
- `Image Comparer (rgthree)`
- `LoraLoader` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Reroute`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `llama_cpp_parameters`
- `GetNode`
- `llama_cpp_model_loader`
- `SetNode`
- `easy anythingIndexSwitch`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `CR Prompt Text`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `MarkdownNote`
- `Note`
- `Note`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `8932`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.7000000000000002`
- `lora_name` = `FLUX_实拍家装风格_FLUX_实拍现代风室内家居.safetensors`
- `strength_model` = `0.6`
- `strength_clip` = `1`

## 知识

覆盖率 **60%**（49/82）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAELoader`、`AIO_Preprocessor`、`CannyEdgePreprocessor`、`easy imagePixelPerfect`、`UNETLoader`、`ModelPatchLoader`、`CR Prompt Text`、`Text Concatenate`、`easy seed`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`Qwen3_VQA`、`LatentUpscaleBy`、`easy cleanGpuUsed`、`GetImageSize+`、`ModelSamplingFlux`、`UpscaleModelLoader`、`UltimateSDUpscale`、`DualCLIPLoader`、`RH_Captioner`、`SDXLPromptStyler`、`LoraLoader`、`SaveImage`、`LoadImage`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`QwenImageDiffsynthControlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
