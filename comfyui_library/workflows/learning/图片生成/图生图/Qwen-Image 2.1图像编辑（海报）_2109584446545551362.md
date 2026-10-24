---
key: 图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json
name: Qwen-Image 2.1图像编辑（海报）_2109584446545551362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json
hash: 6102bb7a35cba10b
coverage: 0.8125
learned_at: 2026-10-23 11:16:20
nodes: [QwenPERewriteT8, CLIPLoader, easy showAnything, ShowText|pysssss, VAELoader, UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, KSampler, SaveImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 835383662285149, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `QwenPERewriteT8`
- `CLIPLoader`
- `easy showAnything`
- `ShowText|pysssss`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `835383662285149`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`QwenPERewriteT8`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
