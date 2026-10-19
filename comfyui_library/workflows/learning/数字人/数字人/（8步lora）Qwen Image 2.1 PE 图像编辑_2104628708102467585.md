---
key: 数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json
name: （8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json
hash: b3f01b198769620b
coverage: 0.925926
learned_at: 2026-10-19 00:41:14
nodes: [VAELoader, ResolutionSelector, QwenPERewriteT8, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAEDecode, CLIPLoader, UNETLoader, QwenImage21Cache, easy showAnything, LoadImage, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, SaveImage, easy cleanGpuUsed, UNETLoader, CLIPLoader, Lora Loader Stack (rgthree), KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 992591369913489, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `VAELoader`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `easy showAnything`
- `LoadImage`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Lora Loader Stack (rgthree)`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `992591369913489`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`VAELoader`、`ResolutionSelector`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`LoadImage`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`CR Prompt Text`、`EmptyLatentImage`、`SaveImage`、`easy cleanGpuUsed`、`Lora Loader Stack (rgthree)`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
