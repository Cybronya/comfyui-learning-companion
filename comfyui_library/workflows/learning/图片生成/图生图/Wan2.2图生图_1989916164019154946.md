---
key: 图片生成/图生图/Wan2.2图生图_1989916164019154946.json
name: Wan2.2图生图_1989916164019154946
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2图生图_1989916164019154946.json
hash: 4728d9cb0ef01010
coverage: 0.9
learned_at: 2026-10-23 11:28:20
nodes: [VAEEncode, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, Qwen3_VQA, QZ_ResolutionPreset, CLIPTextEncode, ImageResizeKJv2, KSampler, JoinStrings, Text, easy showAnything, PreviewImage, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 237638318937506, "steps": 10}
---

# 图片生成/图生图/Wan2.2图生图_1989916164019154946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2图生图_1989916164019154946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `QZ_ResolutionPreset`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `KSampler` ★核心
- `JoinStrings`
- `Text`
- `easy showAnything`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `237638318937506`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAEEncode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`Qwen3_VQA`、`QZ_ResolutionPreset`、`ImageResizeKJv2`、`KSampler`、`JoinStrings`、`Text`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
