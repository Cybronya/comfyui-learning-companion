---
key: 图片生成/图生图/Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634.json
name: Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634.json
hash: 7bc26dd17b201630
coverage: 0.773723
learned_at: 2026-10-23 11:12:39
nodes: [TextEncodeQwenImage21, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyLatentImage, ResolutionSelector, SetNode, GetNode, SeedVR2Conditioning, VAEEncodeTiled, KSampler, VAEDecodeTiled, ResizeImageMaskNode, SeedVR2Preprocess, GetNode, SeedVR2PostProcessing, SaveImage, VAEDecode, GetNode, GetNode, EmptyLatentImage, KSampler, VAEDecode, GetNode, ResizeImageMaskNode, SeedVR2Preprocess, GetNode, SeedVR2Conditioning, VAEEncodeTiled, KSampler, VAEDecodeTiled, SeedVR2PostProcessing, SaveImage, KSampler, QwenImage21Cache, LoadImage, GetNode, SaveImageAdvanced, SaveImageAdvanced, SetNode, SetNode, GetNode, GetNode, EmptyLatentImage, QwenImage21Cache, VAEDecode, SaveImageAdvanced, GetNode, ResizeImageMaskNode, SeedVR2Preprocess, GetNode, SeedVR2Conditioning, VAEEncodeTiled, KSampler, VAEDecodeTiled, SeedVR2PostProcessing, SaveImage, KSampler, GetNode, ModelAttentionBackend, TextEncodeQwenImage21, CLIPLoader, VAELoader, UNETLoader, VAELoader, UNETLoader, PrimitiveStringMultiline, LoraLoaderModelOnly, llama_cpp_parameters, llama_cpp_model_loader, ResolutionSelector, LoadImage, LoadImage, LoadImage, llama_cpp_instruct_adv, TextEncodeQwenImage21, ShowText|pysssss, QwenImage21Cache, XB_BatchImages, llama_cpp_parameters, XB_BatchImages, llama_cpp_model_loader, ShowText|pysssss, PrimitiveStringMultiline, llama_cpp_instruct_adv, LoadImage, Reroute, Reroute, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Comfyui_Image_Proportional_Scaling, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（137 个）：
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `SetNode`
- `GetNode`
- `SeedVR2Conditioning`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `ResizeImageMaskNode`
- `SeedVR2Preprocess`
- `GetNode`
- `SeedVR2PostProcessing`
- `SaveImage`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `ResizeImageMaskNode`
- `SeedVR2Preprocess`
- `GetNode`
- `SeedVR2Conditioning`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `SaveImage`
- `KSampler` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `GetNode`
- `SaveImageAdvanced`
- `SaveImageAdvanced`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `GetNode`
- `ResizeImageMaskNode`
- `SeedVR2Preprocess`
- `GetNode`
- `SeedVR2Conditioning`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `SaveImage`
- `KSampler` ★核心
- `GetNode`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `QwenImage21Cache`
- `XB_BatchImages`
- `llama_cpp_parameters`
- `XB_BatchImages`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Comfyui_Image_Proportional_Scaling`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

## 知识

覆盖率 **77%**（106/137）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`SeedVR2Conditioning`、`VAEEncodeTiled`、`KSampler`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`SeedVR2Preprocess`、`SeedVR2PostProcessing`、`SaveImage`、`VAEDecode`、`QwenImage21Cache`、`LoadImage`、`SaveImageAdvanced`、`ModelAttentionBackend`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`Comfyui_Image_Proportional_Scaling`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
