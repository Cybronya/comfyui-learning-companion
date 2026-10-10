---
key: Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json
name: Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json
hash: 782d7c52837ce0ba
coverage: 0.681818
learned_at: 2026-10-10 20:59:00
nodes: [ResolutionSelector, MarkdownNote, MarkdownNote, QwenImage21Cache, UnetLoaderGGUF, Any Switch (rgthree), VAELoader, MarkdownNote, LoraLoaderModelOnly, CLIPLoader, ImageScaleBy, KSampler, VAEDecode, Image Comparer (rgthree), EmptyLatentImage, ComfySwitchNode, Fast Groups Bypasser (rgthree), UNETLoader, LoadImage, TextEncodeQwenImage21, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 767525193598061, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `QwenImage21Cache`
- `UnetLoaderGGUF` ★核心
- `Any Switch (rgthree)`
- `VAELoader`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageScaleBy`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `767525193598061`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`ResolutionSelector`、`QwenImage21Cache`、`UnetLoaderGGUF`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageScaleBy`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
