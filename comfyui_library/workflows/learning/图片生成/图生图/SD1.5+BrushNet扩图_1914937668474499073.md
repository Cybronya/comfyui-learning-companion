---
key: 图片生成/图生图/SD1.5+BrushNet扩图_1914937668474499073.json
name: SD1.5+BrushNet扩图_1914937668474499073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5+BrushNet扩图_1914937668474499073.json
hash: 54dfd2a2bd8294df
coverage: 0.818182
learned_at: 2026-10-23 11:23:32
nodes: [SaveImage, Reroute, scale, Joy_caption_two_load, CLIPTextEncode, BrushNetLoader, VAEDecode, Joy_caption_two, ShowText|pysssss, PowerPaint, PowerPaintCLIPLoader, WD14Tagger|pysssss, EmptyImage, KSampler, CheckpointLoaderSimple, CLIPTextEncode, ShowText|pysssss, LoadImage, ImagePadForOutpaint, PreviewImage, ImageConcatMulti, GetImageSize]
patterns: []
missing: []
parameters: {"cfg": 5, "checkpoint": "realisticVisionV60B1_v51VAE(1).safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 697576546433932, "steps": 20}
---

# 图片生成/图生图/SD1.5+BrushNet扩图_1914937668474499073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5+BrushNet扩图_1914937668474499073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `SaveImage`
- `Reroute`
- `scale`
- `Joy_caption_two_load`
- `CLIPTextEncode` ★核心
- `BrushNetLoader`
- `VAEDecode` ★核心
- `Joy_caption_two`
- `ShowText|pysssss`
- `PowerPaint`
- `PowerPaintCLIPLoader`
- `WD14Tagger|pysssss`
- `EmptyImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `LoadImage`
- `ImagePadForOutpaint`
- `PreviewImage`
- `ImageConcatMulti`
- `GetImageSize`

## 关键参数

- `seed` = `697576546433932`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `realisticVisionV60B1_v51VAE(1).safetensors`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`SaveImage`、`scale`、`Joy_caption_two_load`、`CLIPTextEncode`、`BrushNetLoader`、`VAEDecode`、`Joy_caption_two`、`PowerPaint`、`PowerPaintCLIPLoader`、`WD14Tagger|pysssss`、`EmptyImage`、`KSampler`、`CheckpointLoaderSimple`、`LoadImage`、`ImagePadForOutpaint`、`ImageConcatMulti`、`GetImageSize`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、PowerPaintCLIPLoader、GetImageSize、GetImageSize
