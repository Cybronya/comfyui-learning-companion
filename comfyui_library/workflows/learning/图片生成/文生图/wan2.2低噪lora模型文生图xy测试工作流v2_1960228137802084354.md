---
key: 图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json
name: wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json
hash: 8a742e69d4b89981
coverage: 0.555556
learned_at: 2026-10-15 22:27:58
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, easy showAnything, GetNode, JoinStrings, SetNode, GetNode, GetNode, GetNode, CLIPLoader, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, VAEDecode, PMRF, JoinStrings, GetNode, easy convertAnything, easy convertAnything, AddLabel, SetNode, EmptyLatentImage, GetNode, GetNode, VAEDecode, JoinStrings, Text, SetNode, SetNode, GetNode, GetNode, AddLabel, ReActorImageDublicator, GetNode, KSampler, GetNode, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, VAEDecode, JoinStrings, easy convertAnything, GetNode, KSampler, AddLabel, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, VAEDecode, JoinStrings, easy convertAnything, GetNode, GetNode, KSampler, SaveImage, Note, Note, Lora Loader, SetNode, GetNode, Seed_, GetNode, KSampler, SetNode, SetNode, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, Create Grid Image from Batch, easy rangeFloat, UNETLoader, JjkText, LoadImage, ConstrainImage|pysssss, GetImageSize, JWInteger, JWInteger, Lora Loader, AddLabel, Note, Lora Loader, PreviewImage, VAELoader, SetNode, RH_Captioner, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, VAEDecode, JoinStrings, easy convertAnything, GetNode, GetNode, KSampler, GetNode, GetNode, Note, Lora Loader, AddLabel, ImpactMakeImageList, easy imageListToImageBatch, PreviewImage, Int]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1054444916599011, "steps": 10, "width": 512}
---

# 图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（135 个）：
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `GetNode`
- `JoinStrings`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `PMRF`
- `JoinStrings`
- `GetNode`
- `easy convertAnything`
- `easy convertAnything`
- `AddLabel`
- `SetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `JoinStrings`
- `Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `ReActorImageDublicator`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `JoinStrings`
- `easy convertAnything`
- `GetNode`
- `KSampler` ★核心
- `AddLabel`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `JoinStrings`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `SaveImage`
- `Note`
- `Note`
- `Lora Loader`
- `SetNode`
- `GetNode`
- `Seed_`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Create Grid Image from Batch`
- `easy rangeFloat`
- `UNETLoader` ★核心
- `JjkText`
- `LoadImage`
- `ConstrainImage|pysssss`
- `GetImageSize`
- `JWInteger`
- `JWInteger`
- `Lora Loader`
- `AddLabel`
- `Note`
- `Lora Loader`
- `PreviewImage`
- `VAELoader`
- `SetNode`
- `RH_Captioner`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `JoinStrings`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `Note`
- `Lora Loader`
- `AddLabel`
- `ImpactMakeImageList`
- `easy imageListToImageBatch`
- `PreviewImage`
- `Int`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `1054444916599011`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **56%**（75/135）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`JoinStrings`、`CLIPLoader`、`VAEDecode`、`PMRF`、`easy convertAnything`、`AddLabel`、`EmptyLatentImage`、`Text`、`ReActorImageDublicator`、`KSampler`、`SaveImage`、`Lora Loader`、`Seed_`、`Create Grid Image from Batch`、`easy rangeFloat`、`UNETLoader`、`LoadImage`、`ConstrainImage|pysssss`、`GetImageSize`、`JWInteger`、`VAELoader`、`RH_Captioner`、`ImpactMakeImageList`、`easy imageListToImageBatch`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
