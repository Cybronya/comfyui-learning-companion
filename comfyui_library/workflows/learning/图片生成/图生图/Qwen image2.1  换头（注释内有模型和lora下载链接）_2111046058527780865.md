---
key: 图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json
name: Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json
hash: e4e369dbb4f93314
coverage: 0.777778
learned_at: 2026-10-23 11:14:19
nodes: [MarkdownNote, SaveImage, Image Comparer (rgthree), UNETLoader, CLIPLoader, TextEncodeQwenImage21, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, LoadImage, KSampler, ComfySwitchNode, UNETLoader, ResolutionSelector, Note, LoadImage, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1040648285097449, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `KSampler` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `Note`
- `LoadImage`
- `VAELoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1040648285097449`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`SaveImage`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`VAEDecode`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`LoadImage`、`KSampler`、`ResolutionSelector`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
