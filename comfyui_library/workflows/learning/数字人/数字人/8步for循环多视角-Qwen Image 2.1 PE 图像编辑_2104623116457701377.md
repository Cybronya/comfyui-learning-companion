---
key: 数字人/数字人/8步for循环多视角-Qwen Image 2.1 PE 图像编辑_2104623116457701377.json
name: 8步for循环多视角-Qwen Image 2.1 PE 图像编辑_2104623116457701377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/8步for循环多视角-Qwen Image 2.1 PE 图像编辑_2104623116457701377.json
hash: 40368cc4be0fad63
coverage: 0.925926
learned_at: 2026-10-19 00:40:58
nodes: [VAELoader, EmptyLatentImage, CLIPLoader, CR Prompt Text, QwenPERewriteT8, easy showAnything, ComfySwitchNode, TextEncodeQwenImage21, KSampler, UNETLoader, LoadImage, ResolutionSelector, UNETLoader, CLIPLoader, Lora Loader Stack (rgthree), CR Prompt Text, GetItemFromList, ShowAnything|Mie, easy lengthAnything, ShowAnything|Mie, HAIGC_SaveImagesToZip, VAEDecode, easy forLoopStart, easy batchAnything, easy forLoopEnd, Text Multiline, easy promptList]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 299943655373541, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/8步for循环多视角-Qwen Image 2.1 PE 图像编辑_2104623116457701377.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/8步for循环多视角-Qwen Image 2.1 PE 图像编辑_2104623116457701377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `easy showAnything`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Lora Loader Stack (rgthree)`
- `CR Prompt Text`
- `GetItemFromList`
- `ShowAnything|Mie`
- `easy lengthAnything`
- `ShowAnything|Mie`
- `HAIGC_SaveImagesToZip`
- `VAEDecode` ★核心
- `easy forLoopStart`
- `easy batchAnything`
- `easy forLoopEnd`
- `Text Multiline`
- `easy promptList`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `299943655373541`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`CR Prompt Text`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`LoadImage`、`ResolutionSelector`、`Lora Loader Stack (rgthree)`、`GetItemFromList`、`ShowAnything|Mie`、`easy lengthAnything`、`HAIGC_SaveImagesToZip`、`VAEDecode`、`easy forLoopStart`、`easy batchAnything`、`easy forLoopEnd`、`Text Multiline`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
