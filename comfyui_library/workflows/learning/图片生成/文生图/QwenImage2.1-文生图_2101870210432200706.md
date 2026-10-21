---
key: 图片生成/文生图/QwenImage2.1-文生图_2101870210432200706.json
name: QwenImage2.1-文生图_2101870210432200706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage2.1-文生图_2101870210432200706.json
hash: da01a09ac3368944
coverage: 0.866667
learned_at: 2026-10-20 01:51:25
nodes: [TextEncodeQwenImage21, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, easy showAnything, KSampler, VAEDecode, SaveImageAdvanced, TextGenerateLTX2Prompt, Text, ResolutionSelector, Note, SaveImage, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/QwenImage2.1-文生图_2101870210432200706.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage2.1-文生图_2101870210432200706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `TextGenerateLTX2Prompt`
- `Text`
- `ResolutionSelector`
- `Note`
- `SaveImage`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`TextGenerateLTX2Prompt`、`Text`、`ResolutionSelector`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
