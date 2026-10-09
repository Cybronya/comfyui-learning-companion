---
key: 图片生成/文生图/WAN2.2 真实系文生图【可测lora】_1957992470980210690.json
name: WAN2.2 真实系文生图【可测lora】_1957992470980210690.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2 真实系文生图【可测lora】_1957992470980210690.json
hash: f6a83df5ec389ff3
coverage: 0.857143
learned_at: 2026-10-07 23:31:18
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, UNETLoader, UpscaleModelLoader, ImageUpscaleWithModel, VAEDecode, VAEDecode, ImageScaleBy, VAEEncode, VAEDecode, CR Text Concatenate, ShowText, CLIPLoader, VAELoader, Anything Everywhere3, PrimitiveStringMultiline, PreviewImage, SaveImage, SaveImage, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, KSampler, KSampler, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage]
patterns: [text_to_image]
missing: [CR Text Concatenate]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.25000000000000006, "height": 960, "sampler_name": "euler", "scheduler": "beta", "seed": 666, "steps": 10, "width": 1280}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/WAN2.2 真实系文生图【可测lora】_1957992470980210690.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1957992470980210690.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CR Text Concatenate`
- `ShowText`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `666`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.25000000000000006`
- `width` = `1280`
- `height` = `960`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`ShowText`、`CLIPLoader`、`VAELoader`、`SaveImage`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`

**缺卡**（1）：`CR Text Concatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
