---
key: 图片生成/文生图/Qwen-image2.1全功能合集_2103043228093206529.json
name: Qwen-image2.1全功能合集_2103043228093206529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1全功能合集_2103043228093206529.json
hash: 564d3f8595e6c795
coverage: 0.616438
learned_at: 2026-10-10 20:59:05
nodes: [KSampler, VAEDecode, EmptyLatentImage, KSampler, ResolutionSelector, Mask Fill Holes, SAM3_Detect, GrowMask, DrawMaskOnImage, PreviewImage, KSampler, VAEDecode, Mask Fill Holes, GrowMask, VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, ResolutionSelector, EmptyLatentImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PreviewImage, Fast Groups Bypasser (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyLatentImage, GetImageSize, TextEncodeQwenImage21, TextEncodeQwenImage21, MarkdownNote, DrawMaskOnImage, MarkdownNote, ComfySwitchNode, KSampler, TextEncodeQwenImage21, PreviewImage, ResolutionSelector, VAEDecode, ComfySwitchNode, MarkdownNote, MarkdownNote, SaveImage, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, EmptyLatentImage, SaveImage, LayerUtility: ImageReel, LoadImage, CheckpointLoaderSimple, CLIPTextEncode, TextEncodeQwenImage21, SaveImage, Anything Everywhere3, UNETLoader, CLIPLoader, VAELoader, Image Comparer (rgthree), MarkdownNote, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, CR Text, RHLLMChatNode, PreviewAny, LoadImage, CR Text]
patterns: [text_to_image]
missing: [CR Text, CR Text, LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, Mask Fill Holes, Mask Fill Holes]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9527, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-image2.1全功能合集_2103043228093206529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1全功能合集_2103043228093206529.json`

## 结构

**节点**（73 个）：
- `KSampler`
- `VAEDecode`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `Mask Fill Holes`
- `SAM3_Detect`
- `GrowMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `KSampler`
- `VAEDecode`
- `Mask Fill Holes`
- `GrowMask`
- `VAEDecode`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `ResolutionSelector`
- `EmptyLatentImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage`
- `GetImageSize`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `MarkdownNote`
- `DrawMaskOnImage`
- `MarkdownNote`
- `ComfySwitchNode`
- `KSampler`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `ResolutionSelector`
- `VAEDecode`
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImage`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `EmptyLatentImage`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LoadImage`
- `CheckpointLoaderSimple`
- `CLIPTextEncode`
- `TextEncodeQwenImage21`
- `SaveImage`
- `Anything Everywhere3`
- `UNETLoader`
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
- `LoadImage`
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `9527`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **62%**（45/73）

**有卡**：`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`Mask Fill Holes`、`SAM3_Detect`、`GrowMask`、`DrawMaskOnImage`、`PreviewImage`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`Fast Groups Bypasser (rgthree)`、`SaveImage`、`GetImageSize`、`TextEncodeQwenImage21`、`MarkdownNote`、`ComfySwitchNode`、`PreviewAny`、`llama_cpp_model_loader`

**缺卡**（8）：`CR Text`、`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReelComposit`、`Mask Fill Holes`、`Mask Fill Holes`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
