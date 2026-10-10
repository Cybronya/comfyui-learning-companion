---
key: Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122.json
name: Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122.json
hash: 1135c8f343ed176c
coverage: 0.729167
learned_at: 2026-10-10 20:58:51
nodes: [Mask Fill Holes, GrowMask, DrawMaskOnImage, KSampler, VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, SaveImage, LayerUtility: ImageReel, UNETLoader, CLIPLoader, VAELoader, LoadImage, Anything Everywhere3, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewAny, TextEncodeQwenImage21, KSampler, VAEDecode, KSampler, VAEDecode, TextEncodeQwenImage21, llama_cpp_model_loader, CR Text, llama_cpp_instruct_adv, PreviewAny, EmptyLatentImage, ResolutionSelector, ResolutionSelector, Fast Groups Bypasser (rgthree), EmptyLatentImage, GetImageSize, EmptyLatentImage, CR Text, ComfySwitchNode, SaveImage, ResolutionSelector, RHLLMChatNode, SaveImage, CLIPTextEncode, CheckpointLoaderSimple, SAM3_Detect, Mask Fill Holes, GrowMask, DrawMaskOnImage, PreviewImage, LoadImage, VAEDecode, LayerUtility: ImageReelComposit, TextEncodeQwenImage21, ComfySwitchNode, LayerUtility: ImageReel, PreviewImage, PreviewImage, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, Mask Fill Holes, Mask Fill Holes]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
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
- `LayerUtility: ImageReel`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
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

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **73%**（70/96）

**有卡**：`GrowMask`、`DrawMaskOnImage`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`GetImageSize`、`RHLLMChatNode`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`SAM3_Detect`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**缺卡**（8）：`CR Text`、`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReelComposit`、`Mask Fill Holes`、`Mask Fill Holes`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
