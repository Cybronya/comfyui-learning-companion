---
key: 图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json
name: Qwen-Image-2.1 动漫转真人_2108914677098045442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json
hash: e1a0e89286a7fecf
coverage: 0.882353
learned_at: 2026-10-23 11:16:25
nodes: [CLIPLoader, VAELoader, UNETLoader, SaveImage, Image Comparer (rgthree), EmptyLatentImage, GetImageSize, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenImage21Cache, KSampler, VAEDecode, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 124453274490372, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `124453274490372`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`、`EmptyLatentImage`、`GetImageSize`、`ResolutionSelector`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
