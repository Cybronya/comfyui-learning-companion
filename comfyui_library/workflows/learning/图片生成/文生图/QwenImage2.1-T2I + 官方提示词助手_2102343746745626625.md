---
key: 图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json
name: QwenImage2.1-T2I + 官方提示词助手_2102343746745626625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json
hash: f7b7faf9030d1fa7
coverage: 0.789474
learned_at: 2026-10-20 01:51:25
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ResolutionSelector, Any Switch (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline, TextGenerate, TextConcatenator, JsonExtractString, CLIPLoader, ShowAnything|Mie, SaveImageAdvanced, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 0, "steps": 30, "width": 1560}
---

# 图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `TextConcatenator`
- `JsonExtractString`
- `CLIPLoader`
- `ShowAnything|Mie`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1560`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`TextGenerate`、`TextConcatenator`、`JsonExtractString`、`ShowAnything|Mie`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
