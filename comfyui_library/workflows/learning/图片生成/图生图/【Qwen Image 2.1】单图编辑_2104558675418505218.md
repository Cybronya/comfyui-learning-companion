---
key: 图片生成/图生图/【Qwen Image 2.1】单图编辑_2104558675418505218.json
name: 【Qwen Image 2.1】单图编辑_2104558675418505218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】单图编辑_2104558675418505218.json
hash: dd165da922ef0689
coverage: 0.809524
learned_at: 2026-10-21 00:46:37
nodes: [UNETLoader, QwenImage21Cache, Anything Everywhere3, VAEDecode, TextEncodeQwenImage21, LoadImage, EmptyLatentImage, ShowText|pysssss, CR Prompt Text, ResolutionSelector, KSampler, CLIPLoader, CR Text Concatenate, JjkText, CLIPLoader, VAELoader, TextGenerate, ComfySwitchNode, SaveImage, Seed (rgthree), ResizeLongestToNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 186845512634662, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【Qwen Image 2.1】单图编辑_2104558675418505218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】单图编辑_2104558675418505218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `CR Prompt Text`
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `CR Text Concatenate`
- `JjkText`
- `CLIPLoader`
- `VAELoader`
- `TextGenerate`
- `ComfySwitchNode`
- `SaveImage`
- `Seed (rgthree)`
- `ResizeLongestToNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `186845512634662`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`EmptyLatentImage`、`CR Prompt Text`、`ResolutionSelector`、`KSampler`、`CLIPLoader`、`CR Text Concatenate`、`VAELoader`、`TextGenerate`、`SaveImage`、`Seed (rgthree)`、`ResizeLongestToNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
