---
key: 图片生成/文生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json
name: Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json
hash: a0aeb294950d6d68
coverage: 0.72973
learned_at: 2026-10-20 01:51:20
nodes: [VAEDecode, EmptyLatentImage, ResolutionSelector, Mask Fill Holes, SAM3_Detect, GrowMask, DrawMaskOnImage, PreviewImage, VAEDecode, Mask Fill Holes, GrowMask, VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, ResolutionSelector, EmptyLatentImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PreviewImage, Fast Groups Bypasser (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyLatentImage, GetImageSize, TextEncodeQwenImage21, TextEncodeQwenImage21, MarkdownNote, DrawMaskOnImage, MarkdownNote, ComfySwitchNode, TextEncodeQwenImage21, PreviewImage, ResolutionSelector, VAEDecode, ComfySwitchNode, MarkdownNote, MarkdownNote, SaveImage, CR Text, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, EmptyLatentImage, LoadImage, SaveImage, LayerUtility: ImageReel, LoadImage, CheckpointLoaderSimple, CLIPTextEncode, TextEncodeQwenImage21, SaveImage, CLIPLoader, VAELoader, Image Comparer (rgthree), MarkdownNote, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, CR Text, RHLLMChatNode, PreviewAny, UNETLoader, Anything Everywhere3, LoraLoaderModelOnly, KSampler, KSampler, KSampler, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 291690707736552, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `Mask Fill Holes`
- `SAM3_Detect`
- `GrowMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `Mask Fill Holes`
- `GrowMask`
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `MarkdownNote`
- `DrawMaskOnImage`
- `MarkdownNote`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImage`
- `CR Text`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `CR Text`
- `RHLLMChatNode`
- `PreviewAny`
- `UNETLoader` ★核心
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `291690707736552`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（54/74）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`Mask Fill Holes`、`SAM3_Detect`、`GrowMask`、`DrawMaskOnImage`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`SaveImage`、`GetImageSize`、`TextEncodeQwenImage21`、`CR Text`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`RHLLMChatNode`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode
