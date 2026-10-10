---
key: 图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json
name: Qwen Image 2.1 扩图专用工作流_2106034671938260993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图专用工作流_2106034671938260993.json
hash: 44670bbd70c2bb14
coverage: 0.833333
learned_at: 2026-10-10 20:48:05
nodes: [PixaromaLabel, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, QwenImage21Cache, PreviewImage, LoadImage, LoadImage, PixaromaLabel, MarkdownNote, VAEDecode, KSampler, SaveImage, CR Prompt Text, ImagePadKJ, GetImageSize, EmptyLatentImage, ModelAttentionBackend, TextGenerateLTX2Prompt, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 202954546112106, "steps": 40, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **83%**（20/24）

**有卡**：`PixaromaLabel`、`PathchSageAttentionKJ`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`LoadImage`、`VAEDecode`、`KSampler`、`SaveImage`、`ImagePadKJ`、`GetImageSize`、`EmptyLatentImage`、`ModelAttentionBackend`、`TextGenerateLTX2Prompt`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
