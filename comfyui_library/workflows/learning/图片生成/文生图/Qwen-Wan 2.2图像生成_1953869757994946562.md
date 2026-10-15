---
key: 图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json
name: Qwen-Wan 2.2图像生成_1953869757994946562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json
hash: 62cef0998b177f8d
coverage: 0.903226
learned_at: 2026-10-15 22:27:20
nodes: [CLIPLoader, ModelSamplingAuraFlow, KSampler, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, PathchSageAttentionKJ, JWStringConcat, CLIPTextEncode, CLIPTextEncode, ClownsharKSampler_Beta, VAELoader, Textbox, EmptySD3LatentImage, LatentUpscaleBy, PreviewImage, SaveImage, Note, easy cleanGpuUsed, VAEDecode, VAEDecode, ImageStitch, PreviewImage, Textbox, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": 0.30000000000000004, "seed": 0.5000000000000001, "steps": "beta57"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `JWStringConcat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `VAELoader`
- `Textbox`
- `EmptySD3LatentImage`
- `LatentUpscaleBy`
- `PreviewImage`
- `SaveImage`
- `Note`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `PreviewImage`
- `Textbox`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `0.5000000000000001`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `0.30000000000000004`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`KSampler`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAELoader`、`JWStringConcat`、`ClownsharKSampler_Beta`、`Textbox`、`EmptySD3LatentImage`、`LatentUpscaleBy`、`SaveImage`、`easy cleanGpuUsed`、`VAEDecode`、`ImageStitch`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ClownsharKSampler_Beta、LatentUpscaleBy

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
