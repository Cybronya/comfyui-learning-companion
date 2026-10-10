---
key: 图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json
name: Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json
hash: 3cef85b735f20eae
coverage: 0.833333
learned_at: 2026-10-10 20:48:02
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, VAELoader, EmptyLatentImage, ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, ResolutionSelector, LoadImage, LoadImage, JjkText, Note, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 912445479728351, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `Note`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `912445479728351`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`ResolutionSelector`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
