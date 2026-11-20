---
key: 图片生成/图生图/Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010.json
name: Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010.json
hash: a027f8e749ce8ff9
coverage: 0.882353
learned_at: 2026-11-02 19:12:51
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), QwenImage21Cache, LoadImage, TextEncodeQwenImage21, CLIPLoader, TextGenerate, easy showAnything, UNETLoader, CLIPLoader, TextInput_, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 834465342237954, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `QwenImage21Cache`
- `LoadImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `TextGenerate`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextInput_`
- `TextInput_`

## 关键参数

- `seed` = `834465342237954`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`TextGenerate`、`TextInput_`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
