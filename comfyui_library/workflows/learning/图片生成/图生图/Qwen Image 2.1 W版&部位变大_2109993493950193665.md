---
key: 图片生成/图生图/Qwen Image 2.1 W版&部位变大_2109993493950193665.json
name: Qwen Image 2.1 W版&部位变大_2109993493950193665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 W版&部位变大_2109993493950193665.json
hash: 23fe19ff754891ee
coverage: 0.705263
learned_at: 2026-10-23 11:12:39
nodes: [TextEncodeQwenImage21, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyLatentImage, ResolutionSelector, MarkdownNote, SetNode, GetNode, SeedVR2Conditioning, VAEEncodeTiled, KSampler, VAEDecodeTiled, ResizeImageMaskNode, SeedVR2Preprocess, GetNode, SeedVR2PostProcessing, SaveImage, VAEDecode, GetNode, GetNode, EmptyLatentImage, KSampler, VAEDecode, GetNode, ResizeImageMaskNode, SeedVR2Preprocess, GetNode, SeedVR2Conditioning, VAEEncodeTiled, KSampler, VAEDecodeTiled, SeedVR2PostProcessing, SaveImage, KSampler, QwenImage21Cache, LoadImage, GetNode, SaveImageAdvanced, SaveImageAdvanced, SetNode, SetNode, GetNode, GetNode, EmptyLatentImage, QwenImage21Cache, VAEDecode, SaveImageAdvanced, GetNode, ResizeImageMaskNode, SeedVR2Preprocess, GetNode, SeedVR2Conditioning, VAEEncodeTiled, KSampler, VAEDecodeTiled, SeedVR2PostProcessing, SaveImage, KSampler, GetNode, ModelAttentionBackend, TextEncodeQwenImage21, CLIPLoader, VAELoader, UNETLoader, VAELoader, UNETLoader, PrimitiveStringMultiline, LoraLoaderModelOnly, llama_cpp_parameters, llama_cpp_model_loader, ResolutionSelector, LoadImage, LoadImage, LoadImage, llama_cpp_instruct_adv, TextEncodeQwenImage21, ShowText|pysssss, QwenImage21Cache, XB_BatchImages, llama_cpp_parameters, XB_BatchImages, llama_cpp_model_loader, ShowText|pysssss, PrimitiveStringMultiline, llama_cpp_instruct_adv, LoadImage, Reroute, Reroute, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Comfyui_Image_Proportional_Scaling, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 269904760751773, "steps": 25, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 W版&部位变大_2109993493950193665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 W版&部位变大_2109993493950193665.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `269904760751773`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（67/95）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`SeedVR2Conditioning`、`VAEEncodeTiled`、`KSampler`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`SeedVR2Preprocess`、`SeedVR2PostProcessing`、`SaveImage`、`VAEDecode`、`QwenImage21Cache`、`LoadImage`、`SaveImageAdvanced`、`ModelAttentionBackend`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`Comfyui_Image_Proportional_Scaling`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
