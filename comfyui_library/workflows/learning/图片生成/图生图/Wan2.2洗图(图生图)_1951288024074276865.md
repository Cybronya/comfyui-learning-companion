---
key: 图片生成/图生图/Wan2.2洗图(图生图)_1951288024074276865.json
name: Wan2.2洗图(图生图)_1951288024074276865
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2洗图(图生图)_1951288024074276865.json
hash: 803b0d12ef36c37e
coverage: 0.96875
learned_at: 2026-10-23 11:28:24
nodes: [VAELoader, Note, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, VAEEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, PDIMAGE_LongerSize, VAEDecode, SaveImage, VAEDecode, ModelSamplingSD3, PMRF, CLIPLoader, KSampler, SaveImage, LoadImage, CLIPTextEncode, Bjornulf_TextToStringAndSeed, PDIMAGE_LongerSize, SaveImage, ImageConcanate, CLIPTextEncode, SaveImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.30000000000000004, "sampler_name": "dpmpp_sde", "scheduler": "simple", "seed": 497163970725457, "steps": 20}
---

# 图片生成/图生图/Wan2.2洗图(图生图)_1951288024074276865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2洗图(图生图)_1951288024074276865.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `PMRF`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Bjornulf_TextToStringAndSeed`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAEEncode`、`PDIMAGE_LongerSize`、`VAEDecode`、`SaveImage`、`PMRF`、`CLIPLoader`、`KSampler`、`LoadImage`、`CLIPTextEncode`、`Bjornulf_TextToStringAndSeed`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
