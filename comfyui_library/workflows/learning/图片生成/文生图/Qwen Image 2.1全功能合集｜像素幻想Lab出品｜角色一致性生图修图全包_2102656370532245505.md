---
key: 图片生成/文生图/Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505.json
name: Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505.json
hash: e640b8068d75e914
coverage: 0.763636
learned_at: 2026-10-07 02:16:56
nodes: [KSampler, VAEDecode, EmptyLatentImage, KSampler, ResolutionSelector, Mask Fill Holes, SAM3_Detect, GrowMask, DrawMaskOnImage, PreviewImage, KSampler, VAEDecode, Mask Fill Holes, GrowMask, VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, ResolutionSelector, EmptyLatentImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PreviewImage, Fast Groups Bypasser (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyLatentImage, GetImageSize, TextEncodeQwenImage21, TextEncodeQwenImage21, DrawMaskOnImage, ComfySwitchNode, KSampler, TextEncodeQwenImage21, PreviewImage, ResolutionSelector, VAEDecode, ComfySwitchNode, SaveImage, CR Text, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, EmptyLatentImage, LoadImage, SaveImage, LayerUtility: ImageReel, LoadImage, CheckpointLoaderSimple, CLIPTextEncode, TextEncodeQwenImage21, SaveImage, Anything Everywhere3, UNETLoader, CLIPLoader, VAELoader, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, RHLLMChatNode, PreviewAny, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, Mask Fill Holes, Mask Fill Holes]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `Mask Fill Holes`
- `SAM3_Detect`
- `GrowMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `KSampler` ★核心
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
- `DrawMaskOnImage`
- `ComfySwitchNode`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `PreviewImage`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `ComfySwitchNode`
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
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `RHLLMChatNode`
- `PreviewAny`
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

覆盖率 **76%**（84/110）

**有卡**：`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`SAM3_Detect`、`GrowMask`、`DrawMaskOnImage`、`SaveImage`、`GetImageSize`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RHLLMChatNode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

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
