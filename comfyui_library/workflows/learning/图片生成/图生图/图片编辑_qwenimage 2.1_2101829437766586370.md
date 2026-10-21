---
key: 图片生成/图生图/图片编辑_qwenimage 2.1_2101829437766586370.json
name: 图片编辑_qwenimage 2.1_2101829437766586370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑_qwenimage 2.1_2101829437766586370.json
hash: 584d34fe76c08ee5
coverage: 0.923077
learned_at: 2026-10-21 00:51:25
nodes: [VAELoader, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, SaveImageAdvanced, SaveImage, KSampler, UNETLoader, TextEncodeQwenImage21, easy showAnything, EmptyLatentImage, CLIPLoader, BatchImagesNode, LoadImage, LoadImage, ResolutionSelector, TextGenerateLTX2Prompt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 50, "width": 1024}
---

# 图片生成/图生图/图片编辑_qwenimage 2.1_2101829437766586370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑_qwenimage 2.1_2101829437766586370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `SaveImageAdvanced`
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `888`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`SaveImageAdvanced`、`SaveImage`、`KSampler`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`BatchImagesNode`、`LoadImage`、`ResolutionSelector`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
