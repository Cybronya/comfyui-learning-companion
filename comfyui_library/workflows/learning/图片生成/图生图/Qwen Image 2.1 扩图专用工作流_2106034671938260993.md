---
key: 图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json
name: Qwen Image 2.1 扩图专用工作流_2106034671938260993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json
hash: 44670bbd70c2bb14
coverage: 0.916667
learned_at: 2026-10-15 22:25:11
nodes: [PixaromaLabel, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, QwenImage21Cache, PreviewImage, LoadImage, LoadImage, PixaromaLabel, MarkdownNote, VAEDecode, KSampler, SaveImage, CR Prompt Text, ImagePadKJ, GetImageSize, EmptyLatentImage, ModelAttentionBackend, TextGenerateLTX2Prompt, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 202954546112106, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `PixaromaLabel`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `PixaromaLabel`
- `MarkdownNote`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CR Prompt Text`
- `ImagePadKJ`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `ModelAttentionBackend`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `202954546112106`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`PixaromaLabel`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`LoadImage`、`VAEDecode`、`KSampler`、`SaveImage`、`CR Prompt Text`、`ImagePadKJ`、`GetImageSize`、`EmptyLatentImage`、`ModelAttentionBackend`、`TextGenerateLTX2Prompt`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
