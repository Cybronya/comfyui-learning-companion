---
key: 图片生成/图生图/❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210.json
name: ❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210.json
hash: f159143dc9321f72
coverage: 0.46789
learned_at: 2026-10-23 11:47:43
nodes: [PrimitiveStringMultiline, SomethingToString, Fast Groups Bypasser (rgthree), SetNode, easy cleanGpuUsed, ProcessString, GetNode, SetNode, PathchSageAttentionKJ, EmptyLatentImage, ModelSamplingAuraFlow, Fast Groups Bypasser (rgthree), SetNode, Any Switch (rgthree), ImageScale, SetNode, TTP_Image_Tile_Batch, GetNode, GetNode, TTP_Tile_image_size, SetNode, TTP_Image_Assy, GetNode, SeedVR2LoadDiTModel, QwenImage21Cache, CLIPTextEncode, CLIPLoader, GetNode, SetNode, GetNode, Any Switch (rgthree), GetNode, Any Switch (rgthree), GetNode, Any Switch (rgthree), SetNode, GetNode, easy imageSize, SeedVR2LoadVAEModel, Fast Groups Bypasser (rgthree), GetNode, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VAELoader, SaveImage, SetNode, GetNode, GetNode, GetNode, ImageUpscaleWithModel, SetNode, UpscaleModelLoader, GetNode, Fast Groups Bypasser (rgthree), easy int, MarkdownNote, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, Image Comparer (rgthree), GetNode, GetNode, PlaySound|pysssss, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, Mute / Bypass Repeater (rgthree), ModelPreviewOverrideKJ, UNETLoader, easy showAnything, SetNode, GetNode, SetNode, Any Switch (rgthree), GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, VAEDecode, VAEEncode, GetNode, ModelPreviewOverrideKJ, ColorMatchV2, MarkdownNote, KSampler, easy showAnything, easy promptLine, SaveImage, CLIPLoader, LoraLoaderModelOnly, UNETLoader, LoadImage, ModelPatchTorchSettings, ResolutionSelector, ComfySwitchNode, VAEDecode, Image Comparer (rgthree), SeedVR2VideoUpscaler, easy imageSizeBySide, PreviewImage, KSampler, VAELoader, TextEncodeQwenImage21]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.15000000000000002, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 214322074389599, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（109 个）：
- `PrimitiveStringMultiline`
- `SomethingToString`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `easy cleanGpuUsed`
- `ProcessString`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `ImageScale`
- `SetNode`
- `TTP_Image_Tile_Batch`
- `GetNode`
- `GetNode`
- `TTP_Tile_image_size`
- `SetNode`
- `TTP_Image_Assy`
- `GetNode`
- `SeedVR2LoadDiTModel`
- `QwenImage21Cache`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`
- `easy imageSize`
- `SeedVR2LoadVAEModel`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SaveImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageUpscaleWithModel`
- `SetNode`
- `UpscaleModelLoader`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `easy int`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `PlaySound|pysssss`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `Mute / Bypass Repeater (rgthree)`
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `ModelPreviewOverrideKJ`
- `ColorMatchV2`
- `MarkdownNote`
- `KSampler` ★核心
- `easy showAnything`
- `easy promptLine`
- `SaveImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `ModelPatchTorchSettings`
- `ResolutionSelector`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `easy imageSizeBySide`
- `PreviewImage`
- `KSampler` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `214322074389599`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **47%**（51/109）

**有卡**：`SomethingToString`、`easy cleanGpuUsed`、`ProcessString`、`PathchSageAttentionKJ`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`ImageScale`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`QwenImage21Cache`、`CLIPTextEncode`、`CLIPLoader`、`easy imageSize`、`SeedVR2LoadVAEModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`SaveImage`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy int`、`PlaySound|pysssss`、`ImageScaleToTotalPixels`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`Mute / Bypass Repeater (rgthree)`、`ModelPreviewOverrideKJ`、`UNETLoader`、`VAEDecode`、`VAEEncode`、`ColorMatchV2`、`KSampler`、`easy promptLine`、`LoraLoaderModelOnly`、`LoadImage`、`ModelPatchTorchSettings`、`ResolutionSelector`、`SeedVR2VideoUpscaler`、`easy imageSizeBySide`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
