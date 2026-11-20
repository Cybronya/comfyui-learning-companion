---
key: 图片生成/图生图/Qwen Image 2.1｜批量指令式产品重绘・白底电商图工作流_2116046250889015297.json
name: Qwen Image 2.1｜批量指令式产品重绘・白底电商图工作流_2116046250889015297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1｜批量指令式产品重绘・白底电商图工作流_2116046250889015297.json
hash: a374ab1ed9541dcb
coverage: 0.939394
learned_at: 2026-10-30 23:24:23
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), SplitImageWithAlpha, SplitImageWithAlpha, VAEDecode, KSampler, TextEncodeQwenImage21, QwenImage21Cache, UNETLoader, CLIPLoader, VAELoader, SaveImageWithName, Image Sequence Loader [Dream], SequentialImageLoader, Image Comparer (rgthree), SaveImage, SplitImageWithAlpha, VAEDecode, KSampler, TextEncodeQwenImage21, QwenImage21Cache, UNETLoader, CLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 674428915310598, "steps": 25}
---

# 图片生成/图生图/Qwen Image 2.1｜批量指令式产品重绘・白底电商图工作流_2116046250889015297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1｜批量指令式产品重绘・白底电商图工作流_2116046250889015297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SplitImageWithAlpha`
- `SplitImageWithAlpha`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImageWithName`
- `Image Sequence Loader [Dream]`
- `SequentialImageLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SplitImageWithAlpha`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`

## 关键参数

- `seed` = `674428915310598`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`SplitImageWithAlpha`、`SaveImageWithName`、`Image Sequence Loader [Dream]`、`SequentialImageLoader`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
