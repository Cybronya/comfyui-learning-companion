---
key: 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json
name: Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json
hash: c0d4c5f1cccbbbef
coverage: 0.75
learned_at: 2026-10-21 00:43:00
nodes: [CLIPLoader, KSampler, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, MarkdownNote, VAELoader, 孤海注释, UNETLoader, VAEDecode, SaveImage, TextGenerateLTX2Prompt, CLIPLoader, easy showAnything, Note, BatchImagesNode, LoadImage, TextEncodeQwenImage21, MarkdownNote, LoadImage, ResolutionSelector, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 84143219830972, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `VAELoader`
- `孤海注释`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `easy showAnything`
- `Note`
- `BatchImagesNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `MarkdownNote`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `84143219830972`
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

**有卡**：`CLIPLoader`、`KSampler`、`QwenImage21Cache`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`LoadImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
