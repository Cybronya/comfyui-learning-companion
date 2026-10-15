---
key: 图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json
name: wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json
hash: 8a742e69d4b89981
coverage: 0.459259
learned_at: 2026-10-10 20:59:27
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, easy showAnything, GetNode, JoinStrings, SetNode, GetNode, GetNode, GetNode, CLIPLoader, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, VAEDecode, PMRF, JoinStrings, GetNode, easy convertAnything, easy convertAnything, AddLabel, SetNode, EmptyLatentImage, GetNode, GetNode, VAEDecode, JoinStrings, Text, SetNode, SetNode, GetNode, GetNode, AddLabel, ReActorImageDublicator, GetNode, KSampler, GetNode, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, VAEDecode, JoinStrings, easy convertAnything, GetNode, KSampler, AddLabel, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, VAEDecode, JoinStrings, easy convertAnything, GetNode, GetNode, KSampler, SaveImage, Note, Note, Lora Loader, SetNode, GetNode, Seed_, GetNode, KSampler, SetNode, SetNode, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, Create Grid Image from Batch, easy rangeFloat, UNETLoader, JjkText, LoadImage, ConstrainImage|pysssss, GetImageSize, JWInteger, JWInteger, Lora Loader, AddLabel, Note, Lora Loader, PreviewImage, VAELoader, SetNode, RH_Captioner, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, VAEDecode, JoinStrings, easy convertAnything, GetNode, GetNode, KSampler, GetNode, GetNode, Note, Lora Loader, AddLabel, ImpactMakeImageList, easy imageListToImageBatch, PreviewImage, Int]
patterns: [text_to_image]
missing: [ConstrainImage|pysssss, Create Grid Image from Batch, easy convertAnything, easy convertAnything, easy convertAnything, easy convertAnything, easy convertAnything, easy imageListToImageBatch, easy rangeFloat, Lora Loader, Lora Loader, Lora Loader, Lora Loader]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1054444916599011, "steps": 10, "width": 512}
discoveries: [次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Create Grid Image from Batch` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy rangeFloat` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json`

## 结构

**节点**（135 个）：
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `easy showAnything`
- `GetNode`
- `JoinStrings`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `SetNode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `PMRF`
- `JoinStrings`
- `GetNode`
- `easy convertAnything`
- `easy convertAnything`
- `AddLabel`
- `SetNode`
- `EmptyLatentImage`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `JoinStrings`
- `Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `ReActorImageDublicator`
- `GetNode`
- `KSampler`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `JoinStrings`
- `easy convertAnything`
- `GetNode`
- `KSampler`
- `AddLabel`
- `GetNode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `JoinStrings`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `KSampler`
- `SaveImage`
- `Note`
- `Note`
- `Lora Loader`
- `SetNode`
- `GetNode`
- `Seed_`
- `GetNode`
- `KSampler`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Create Grid Image from Batch`
- `easy rangeFloat`
- `UNETLoader`
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
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `JoinStrings`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `KSampler`
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

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1054444916599011`
- `steps` = `10`
- `width` = `512`

## 知识

覆盖率 **46%**（62/135）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`easy showAnything`、`GetNode`、`JoinStrings`、`SetNode`、`CLIPLoader`、`VAEDecode`、`PMRF`、`easy convertAnything`、`AddLabel`、`EmptyLatentImage`、`Text`、`ReActorImageDublicator`、`KSampler`

**缺卡**（13）：`ConstrainImage|pysssss`、`Create Grid Image from Batch`、`easy convertAnything`、`easy convertAnything`、`easy convertAnything`、`easy convertAnything`、`easy convertAnything`、`easy imageListToImageBatch`、`easy rangeFloat`、`Lora Loader`、`Lora Loader`、`Lora Loader`、`Lora Loader`

## 学习发现

- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Create Grid Image from Batch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy rangeFloat` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Lora Loader` 仅有 LoRA 的通用知识，没有该节点自己的说明
