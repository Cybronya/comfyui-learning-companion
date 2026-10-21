---
key: 图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json
name: qwen image 2.1多图编辑_2101819535304253442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json
hash: 214f45cbbe26d38f
coverage: 0.75
learned_at: 2026-10-21 00:46:01
nodes: [CLIPLoader, KSampler, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, MarkdownNote, VAELoader, 孤海注释, UNETLoader, VAEDecode, SaveImage, LoadImage, LoadImage, LoadImage, TextGenerateLTX2Prompt, CLIPLoader, easy showAnything, Note, BatchImagesNode, CR Text, LoadImage, TextEncodeQwenImage21, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 829820744253248, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `VAELoader`
- `孤海注释`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `easy showAnything`
- `Note`
- `BatchImagesNode`
- `CR Text`
- `LoadImage`
- `TextEncodeQwenImage21`
- `MarkdownNote`

## 关键参数

- `seed` = `829820744253248`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（18/24）

**有卡**：`CLIPLoader`、`KSampler`、`QwenImage21Cache`、`EmptyLatentImage`、`ResolutionSelector`、`VAELoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`CR Text`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
