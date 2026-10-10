---
key: 图片生成/图生图/Qwen image 2.1图片编辑_2102302751672848386.json
name: Qwen image 2.1图片编辑_2102302751672848386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑_2102302751672848386.json
hash: 900871b4dcf9f32b
coverage: 0.896552
learned_at: 2026-10-10 20:48:08
nodes: [UNETLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, LoadImage, LoadImage, TextGenerateLTX2Prompt, easy showAnything, CLIPLoader, QwenImage21Cache, KSampler, VAEDecode, SaveImageAdvanced, ComfySwitchNode, ResolutionSelector, TextInput_, SaveImage, BatchImagesNode, EmptyLatentImage, LoadImage, GetImageSize, TextEncodeQwenImage21, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图片编辑_2102302751672848386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑_2102302751672848386.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `CLIPLoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `ResolutionSelector`
- `TextInput_`
- `SaveImage`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `GetImageSize`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`UNETLoader`、`VAELoader`、`LoadImage`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`ResolutionSelector`、`TextInput_`、`SaveImage`、`BatchImagesNode`、`EmptyLatentImage`、`GetImageSize`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
