---
key: 图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json
name: 透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json
hash: 72d769778bba9247
coverage: 0.923077
learned_at: 2026-10-21 03:03:10
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, JjkText, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, SaveImage, SplitImageWithAlpha, MaskToImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1090734849071299, "steps": 50, "width": 1088}
---

# 图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/透明素材生成丨Qwen Image 2.1丨文生图·透明PNG_2112093151107305474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `JjkText`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SplitImageWithAlpha`
- `MaskToImage`
- `SaveImage`

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1090734849071299`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`SplitImageWithAlpha`、`MaskToImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
