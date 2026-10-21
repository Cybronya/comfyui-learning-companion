---
key: 图片生成/图生图/Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370.json
name: Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370.json
hash: d347d77960ea2953
coverage: 0.857143
learned_at: 2026-10-21 00:42:04
nodes: [LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, MuyeTextEditOutput, MuyeTextEditOutput, TextGenerate, BatchImagesNode, ResolutionSelector, UNETLoader, EmptyLatentImage, LoadImageGoohai, LoadImageGoohai, QwenImage21Cache, Reroute, Reroute, KSampler, VAEDecode, ImageConcatMulti, VOSR2Upscale, VOSR2ModelLoader, 忽略多组孤海, Reroute, TextEncodeQwenImage21, SaveImage, SaveImage, PreviewImage, PreviewImage, SaveImage, LoadImage, SplitImageWithAlpha]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 102665075987859, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `TextGenerate`
- `BatchImagesNode`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LoadImageGoohai`
- `LoadImageGoohai`
- `QwenImage21Cache`
- `Reroute`
- `Reroute`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `忽略多组孤海`
- `Reroute`
- `TextEncodeQwenImage21`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `SplitImageWithAlpha`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `102665075987859`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`LoadImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`MuyeTextEditOutput`、`TextGenerate`、`BatchImagesNode`、`ResolutionSelector`、`UNETLoader`、`EmptyLatentImage`、`LoadImageGoohai`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`ImageConcatMulti`、`VOSR2Upscale`、`VOSR2ModelLoader`、`忽略多组孤海`、`TextEncodeQwenImage21`、`SaveImage`、`SplitImageWithAlpha`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
