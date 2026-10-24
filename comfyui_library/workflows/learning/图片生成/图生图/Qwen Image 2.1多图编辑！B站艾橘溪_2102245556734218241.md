---
key: 图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json
name: Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json
hash: 94199c9ab82c43f4
coverage: 0.869565
learned_at: 2026-10-23 11:12:55
nodes: [MarkdownNote, CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, ResolutionSelector, LoadImage, LoadImage, QwenImage21Cache, KSampler, SaveImage, SaveImage, easy imageConcat, easy imageConcat, easy imageConcat, JjkText, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 40511518867650, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `MarkdownNote`
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `JjkText`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `40511518867650`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`SaveImage`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
