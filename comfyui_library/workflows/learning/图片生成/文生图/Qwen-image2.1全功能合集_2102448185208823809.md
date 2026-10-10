---
key: Qwen-image2.1全功能合集_2102448185208823809.json
name: Qwen-image2.1全功能合集_2102448185208823809
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1全功能合集_2102448185208823809.json
hash: 745ee0da687417f9
coverage: 0.616438
learned_at: 2026-10-10 20:59:05
nodes: [Mask Fill Holes, GrowMask, DrawMaskOnImage, KSampler, VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, SaveImage, LayerUtility: ImageReel, UNETLoader, CLIPLoader, VAELoader, LoadImage, Anything Everywhere3, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewAny, TextEncodeQwenImage21, KSampler, VAEDecode, MarkdownNote, MarkdownNote, MarkdownNote, KSampler, VAEDecode, TextEncodeQwenImage21, llama_cpp_model_loader, CR Text, llama_cpp_instruct_adv, PreviewAny, EmptyLatentImage, ResolutionSelector, ResolutionSelector, Fast Groups Bypasser (rgthree), EmptyLatentImage, GetImageSize, EmptyLatentImage, CR Text, MarkdownNote, ComfySwitchNode, SaveImage, ResolutionSelector, RHLLMChatNode, SaveImage, CLIPTextEncode, CheckpointLoaderSimple, SAM3_Detect, Mask Fill Holes, GrowMask, DrawMaskOnImage, PreviewImage, LoadImage, VAEDecode, LayerUtility: ImageReelComposit, TextEncodeQwenImage21, ComfySwitchNode, MarkdownNote, LayerUtility: ImageReel, PreviewImage, PreviewImage, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), 孤海注释]
patterns: [text_to_image]
missing: [CR Text, CR Text, LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, Mask Fill Holes, Mask Fill Holes]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9528, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识]
---

# Qwen-image2.1全功能合集_2102448185208823809.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1全功能合集_2102448185208823809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `Mask Fill Holes`
- `GrowMask`
- `DrawMaskOnImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `llama_cpp_model_loader`
- `CR Text`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `CR Text`
- `MarkdownNote`
- `ComfySwitchNode`
- `SaveImage`
- `ResolutionSelector`
- `RHLLMChatNode`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `SAM3_Detect`
- `Mask Fill Holes`
- `GrowMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `LoadImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `MarkdownNote`
- `LayerUtility: ImageReel`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `9528`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **62%**（45/73）

**有卡**：`GrowMask`、`DrawMaskOnImage`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`GetImageSize`、`RHLLMChatNode`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`SAM3_Detect`

**缺卡**（8）：`CR Text`、`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReelComposit`、`Mask Fill Holes`、`Mask Fill Holes`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
