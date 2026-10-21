---
key: 图片生成/图生图/Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921.json
name: Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921.json
hash: cf12400d340aa2b0
coverage: 0.642105
learned_at: 2026-10-21 00:42:39
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, EmptyLatentImage, GetNode, SetNode, Any Switch (rgthree), SetNode, SetNode, SetNode, SAM3_Detect, GrowMaskWithBlur, ShowText|pysssss, KSampler, CheckpointLoaderSimple, AILab_MaskExtractor, Seed (rgthree), ComfySwitchNode, Image Comparer (rgthree), GetNode, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, GetNode, Fast Groups Bypasser (rgthree), QwenImage21Cache, CLIPLoader, UNETLoader, VAELoader, GetNode, SetNode, GetNode, LoraLoaderModelOnly, PrimitiveStringMultiline, CLIPTextEncode, LoadAndResizeImage, VOSR2ModelLoader, VOSR2Upscale, Image Comparer (rgthree), easy cleanGpuUsed, SeedVR2Conditioning, UNETLoader, VAELoader, SeedVR2Preprocess, SeedVR2PostProcessing, VAEEncodeTiled, KSampler, Image Comparer (rgthree), SaveImage, VAEDecodeTiled, ResizeImageMaskNode, SaveImage, Fast Groups Bypasser (rgthree), SetNode, LoadAndResizeImage, GetNode, GetNode, TextEncodeQwenImage21, PreviewImage, SetNode, GetNode, VAEDecode, SaveImage, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SAM3_Detect`
- `GrowMaskWithBlur`
- `ShowText|pysssss`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `AILab_MaskExtractor`
- `Seed (rgthree)`
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `QwenImage21Cache`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `LoadAndResizeImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `SeedVR2Conditioning`
- `UNETLoader` ★核心
- `VAELoader`
- `SeedVR2Preprocess`
- `SeedVR2PostProcessing`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecodeTiled` ★核心
- `ResizeImageMaskNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LoadAndResizeImage`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
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

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **64%**（61/95）

**有卡**：`EmptyLatentImage`、`SAM3_Detect`、`GrowMaskWithBlur`、`KSampler`、`CheckpointLoaderSimple`、`AILab_MaskExtractor`、`Seed (rgthree)`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`QwenImage21Cache`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadAndResizeImage`、`VOSR2ModelLoader`、`VOSR2Upscale`、`easy cleanGpuUsed`、`SeedVR2Conditioning`、`SeedVR2Preprocess`、`SeedVR2PostProcessing`、`VAEEncodeTiled`、`SaveImage`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`TextEncodeQwenImage21`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
