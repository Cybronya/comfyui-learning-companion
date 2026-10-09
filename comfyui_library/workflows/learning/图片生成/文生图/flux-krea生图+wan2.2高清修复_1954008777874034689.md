---
key: 图片生成/文生图/flux-krea生图+wan2.2高清修复_1954008777874034689.json
name: flux-krea生图+wan2.2高清修复_1954008777874034689.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux-krea生图+wan2.2高清修复_1954008777874034689.json
hash: fe83c8ae8a452290
coverage: 0.815789
learned_at: 2026-10-07 23:17:48
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, KSamplerSelect, FluxGuidance, BasicGuider, SamplerCustomAdvanced, RandomNoise, BasicScheduler, VAELoader, VAEEncode, VAEDecode, CLIPLoader, VAELoader, LoraLoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStarAndInit, Reroute, Image Comparer (rgthree), LoraLoader, CLIPTextEncode, SaveImage, VAEDecode, LoraLoader, UNETLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, ImageUpscaleWithModel, EmptyLatentImage, CR Text, CR Text Concatenate, CR Text, UpscaleModelLoader, SaveImage, easy seed]
patterns: [text_to_image, lora]
missing: [CR Text, CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.4000000000000001, "height": 768, "lora_name": "flux-lora-风景.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 326546842441735, "steps": 12, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002, "width": 1280}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/flux-krea生图+wan2.2高清修复_1954008777874034689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1954008777874034689.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicScheduler`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `Reroute`
- `Image Comparer (rgthree)`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageUpscaleWithModel`
- `EmptyLatentImage` ★核心
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `UpscaleModelLoader`
- `SaveImage`
- `easy seed`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `flux-lora-风景.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `326546842441735`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`
- `width` = `1280`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`KSamplerSelect`、`FluxGuidance`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicScheduler`、`VAELoader`、`VAEEncode`、`VAEDecode`、`CLIPLoader`、`LoraLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`SaveImage`、`KSampler`、`ImageUpscaleWithModel`、`EmptyLatentImage`、`UpscaleModelLoader`

**缺卡**（5）：`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
