---
key: 图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2115673430904360961.json
name: 诺亚数字人_Qwen_2.1换脸工作流_2115673430904360961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2115673430904360961.json
hash: acbd580a723d3624
coverage: 0.916667
learned_at: 2026-10-30 17:53:57
nodes: [UNETLoader, VAELoader, LoadImage, ImageScaleToTotalPixels, QwenImage21Cache, TextEncodeQwenImage21, KSampler, VAEDecode, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 152963721703624, "steps": 40}
---

# 图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2115673430904360961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2115673430904360961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `SaveImage`

## 关键参数

- `seed` = `152963721703624`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`UNETLoader`、`VAELoader`、`LoadImage`、`ImageScaleToTotalPixels`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
