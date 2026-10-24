---
key: 图片生成/图生图/产品融图 Qwen-Image-2.1_2109928283633700866.json
name: 产品融图 Qwen-Image-2.1_2109928283633700866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/产品融图 Qwen-Image-2.1_2109928283633700866.json
hash: 3dd2bf101a58c3d6
coverage: 0.75
learned_at: 2026-10-23 12:07:56
nodes: [UNETLoader, QwenImage21Cache, CLIPLoader, VAELoader, KSampler, MUTOU_SmartAspectRatio, easy showAnything, PrimitiveStringMultiline, Text Dictionary Convert, easy showAnything, Text Dictionary Get, EmptyLatentImage, ResolutionSelector, LoadImage, SaveImage, VAEDecode, Image Comparer (rgthree), TextEncodeQwenImage21, LoraLoaderModelOnly, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1064347882119989, "steps": 40, "width": 1024}
---

# 图片生成/图生图/产品融图 Qwen-Image-2.1_2109928283633700866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/产品融图 Qwen-Image-2.1_2109928283633700866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `MUTOU_SmartAspectRatio`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `Text Dictionary Convert`
- `easy showAnything`
- `Text Dictionary Get`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1064347882119989`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`KSampler`、`MUTOU_SmartAspectRatio`、`Text Dictionary Convert`、`Text Dictionary Get`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
