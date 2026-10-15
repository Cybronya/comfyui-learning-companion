---
key: 图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json
name: Qwen-Wan 2.2图像生成_1953869757994946562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json
hash: 62cef0998b177f8d
coverage: 0.870968
learned_at: 2026-10-10 20:59:04
nodes: [CLIPLoader, ModelSamplingAuraFlow, KSampler, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, PathchSageAttentionKJ, JWStringConcat, CLIPTextEncode, CLIPTextEncode, ClownsharKSampler_Beta, VAELoader, Textbox, EmptySD3LatentImage, LatentUpscaleBy, PreviewImage, SaveImage, Note, easy cleanGpuUsed, VAEDecode, VAEDecode, ImageStitch, PreviewImage, Textbox, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": 0.30000000000000004, "seed": 0.5000000000000001, "steps": "beta57"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Wan 2.2图像生成_1953869757994946562.json`

## 结构

**节点**（31 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `KSampler`
- `PathchSageAttentionKJ`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `JWStringConcat`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `VAELoader`
- `Textbox`
- `EmptySD3LatentImage`
- `LatentUpscaleBy`
- `PreviewImage`
- `SaveImage`
- `Note`
- `easy cleanGpuUsed`
- `VAEDecode`
- `VAEDecode`
- `ImageStitch`
- `PreviewImage`
- `Textbox`
- `UnetLoaderGGUF`
- `UnetLoaderGGUF`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`

## 关键参数

- `cfg` = `4`
- `denoise` = `1.0000000000000002`
- `sampler_name` = `-1`
- `scheduler` = `0.30000000000000004`
- `seed` = `0.5000000000000001`
- `steps` = `beta57`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`KSampler`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAELoader`、`JWStringConcat`、`ClownsharKSampler_Beta`、`Textbox`、`EmptySD3LatentImage`、`LatentUpscaleBy`、`PreviewImage`、`SaveImage`、`Note`、`easy cleanGpuUsed`、`VAEDecode`、`ImageStitch`、`UnetLoaderGGUF`

**缺卡**（1）：`easy cleanGpuUsed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
