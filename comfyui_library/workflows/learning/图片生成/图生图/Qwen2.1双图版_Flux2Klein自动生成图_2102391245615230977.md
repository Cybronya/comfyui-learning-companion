---
key: 图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json
name: Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json
hash: 03995900a9a0804f
coverage: 0.6
learned_at: 2026-10-10 20:48:09
nodes: [CLIPTextEncode, VAEDecode, VAELoader, CLIPLoader, KSampler, LoraLoader, Seed (rgthree), EmptyFlux2LatentImage, CLIPTextEncode, UNETLoader, LayerUtility: ImageReelComposit, VAEDecode, easy setNode, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageReel, TextEncodeQwenImage21, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, PreviewImage, easy setNode, VAEDecode, SaveImage, easy setNode, Seed (rgthree), KSampler, SaveImage, CR Prompt Text, ResolutionSelector, TextGenerateLTX2Prompt, easy showAnything, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, LoadImage, KSampler, TextGenerateLTX2Prompt, EmptyLatentImage, ShowText|pysssss, GetNode, CR Prompt Text, ResolutionSelector, BatchImagesNode, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, GetNode, EmptyLatentImage, ComfySwitchNode, LoadImage, PreviewAny, TextGenerateLTX2Prompt, CLIPLoader, CLIPLoader, CLIPLoader, LayerUtility: ImageReel, SaveImage, LayerUtility: ImageReelComposit, KSampler, LoadImage, Note, SaveImage, Fast Groups Bypasser (rgthree), LoadImage, ResolutionSelector, CR Prompt Text]
patterns: [text_to_image, lora]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, easy setNode, easy setNode, easy setNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, Seed (rgthree), Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "lora_name": "flux2-klein\\flux-2-klein-9b_细节增加,0.4~0.8.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 26180273275258, "steps": 20, "strength_clip": 1, "strength_model": 0.4, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `LoraLoader` ★核心
- `Seed (rgthree)`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `PreviewImage`
- `easy setNode`
- `VAEDecode` ★核心
- `SaveImage`
- `easy setNode`
- `Seed (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `CR Prompt Text`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `GetNode`
- `CR Prompt Text`
- `ResolutionSelector`
- `BatchImagesNode`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `LayerUtility: ImageReel`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `KSampler` ★核心
- `LoadImage`
- `Note`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `26180273275258`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `flux2-klein\flux-2-klein-9b_细节增加,0.4~0.8.safetensors`
- `strength_model` = `0.4`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（45/75）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`KSampler`、`LoraLoader`、`EmptyFlux2LatentImage`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`SaveImage`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`QwenImage21Cache`、`LoadImage`、`BatchImagesNode`

**缺卡**（12）：`LayerUtility: ImageReel`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReelComposit`、`easy setNode`、`easy setNode`、`easy setNode`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
