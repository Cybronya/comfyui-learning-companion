---
key: 图片生成/图生图/Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010.json
name: Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010.json
hash: 12239b02f31fd88f
coverage: 0.9375
learned_at: 2026-11-02 19:12:52
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), QwenImage21Cache, LoadImage, UNETLoader, CLIPLoader, TextInput_, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1081296144834987, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `QwenImage21Cache`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextInput_`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `1081296144834987`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`LoadImage`、`TextInput_`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
