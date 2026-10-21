---
key: 图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json
name: Qwen image 2.1-图生图-V1_2101853390769840130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json
hash: 2765ab43c0b70b65
coverage: 0.896552
learned_at: 2026-10-21 00:42:56
nodes: [CLIPLoader, QwenImage21Cache, TextEncodeQwenImage21, ComfySwitchNode, KSampler, EmptyLatentImage, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ZNGB_ImageBatchMulti, UNETLoader, CLIPLoader, UNETLoader, CLIPLoader, VAEDecode, SaveImage, ResolutionSelector, StringConcatenate, PrimitiveStringMultiline, easy showAnything, TextGenerateLTX2Prompt, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 566759212454655, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ZNGB_ImageBatchMulti`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `566759212454655`
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

**有卡**：`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`LoadImage`、`ZNGB_ImageBatchMulti`、`UNETLoader`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`StringConcatenate`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
