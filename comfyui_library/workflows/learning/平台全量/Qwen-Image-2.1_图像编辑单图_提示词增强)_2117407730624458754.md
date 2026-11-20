---
key: 平台全量/Qwen-Image-2.1_图像编辑单图_提示词增强)_2117407730624458754.json
name: Qwen-Image-2.1_图像编辑单图_提示词增强)_2117407730624458754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-2.1_图像编辑单图_提示词增强)_2117407730624458754.json
hash: 3d0c5f435757b345
coverage: 0.882353
learned_at: 2026-11-14 00:51:34
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), QwenImage21Cache, LoadImage, TextEncodeQwenImage21, CLIPLoader, TextGenerate, easy showAnything, UNETLoader, CLIPLoader, TextInput_, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1044687808865631, "steps": 25}
---

# 平台全量/Qwen-Image-2.1_图像编辑单图_提示词增强)_2117407730624458754.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-2.1_图像编辑单图_提示词增强)_2117407730624458754.json`

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

- `seed` = `1044687808865631`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`TextGenerate`、`TextInput_`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
