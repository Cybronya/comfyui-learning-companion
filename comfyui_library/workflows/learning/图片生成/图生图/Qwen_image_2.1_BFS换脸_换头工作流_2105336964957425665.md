---
key: 图片生成/图生图/Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665.json
name: Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665.json
hash: 047820ab5dac21e5
coverage: 0.833333
learned_at: 2026-10-21 00:44:02
nodes: [KSampler, QwenImage21Cache, TextGenerate, Reroute, 忽略多组孤海, VAEDecode, ImageConcatMulti, BatchImagesNode, MuyeTextEditOutput, CLIPLoader, MuyeTextEditOutput, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, SaveImage, PreviewImage, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, Reroute, Reroute, Reroute, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, SplitImageWithAlpha, VOSR2ModelLoader, VOSR2Upscale, SaveImage, LoadImageGoohai, LoadImageGoohai, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 137511438017800, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerate`
- `Reroute`
- `忽略多组孤海`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `BatchImagesNode`
- `MuyeTextEditOutput`
- `CLIPLoader`
- `MuyeTextEditOutput`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `Reroute`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `SplitImageWithAlpha`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `SaveImage`
- `LoadImageGoohai`
- `LoadImageGoohai`
- `PreviewImage`

## 关键参数

- `seed` = `137511438017800`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`KSampler`、`QwenImage21Cache`、`TextGenerate`、`忽略多组孤海`、`VAEDecode`、`ImageConcatMulti`、`BatchImagesNode`、`MuyeTextEditOutput`、`CLIPLoader`、`LoadImage`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`SplitImageWithAlpha`、`VOSR2ModelLoader`、`VOSR2Upscale`、`LoadImageGoohai`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
