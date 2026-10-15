---
key: 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json
name: QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json
hash: f39407d2547d2699
coverage: 0.789474
learned_at: 2026-10-15 22:27:24
nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, PrimitiveStringMultiline, VAEDecode, TextConcatenator, TextGenerate, CLIPLoader, JsonExtractString, VAELoader, Any Switch (rgthree), UNETLoader, SaveImageAdvanced, SaveImage, ShowAnything|Mie, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 0, "steps": 30, "width": 1560}
---

# 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `TextConcatenator`
- `TextGenerate`
- `CLIPLoader`
- `JsonExtractString`
- `VAELoader`
- `Any Switch (rgthree)`
- `UNETLoader` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `ShowAnything|Mie`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

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

**有卡**：`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`VAEDecode`、`TextConcatenator`、`TextGenerate`、`JsonExtractString`、`VAELoader`、`UNETLoader`、`SaveImageAdvanced`、`SaveImage`、`ShowAnything|Mie`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
