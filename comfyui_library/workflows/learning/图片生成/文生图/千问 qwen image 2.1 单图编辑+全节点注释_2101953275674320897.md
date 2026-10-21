---
key: 图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json
name: 千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json
hash: cdbb3fe4f81fe208
coverage: 0.472222
learned_at: 2026-10-20 01:52:18
nodes: [VAEDecode, TextEncodeQwenImage21, ComfySwitchNode, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, LoadImage, KSampler, EmptyLatentImage, ResolutionSelector, CLIPLoader, CLIPLoader, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, TextGenerateLTX2Prompt, Note, CR Prompt Text, Note, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 456905900029783, "steps": 40, "width": 1024}
---

# 图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `LoadImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `CLIPLoader`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `Note`
- `CR Prompt Text`
- `Note`
- `SaveImage`

## 关键参数

- `seed` = `456905900029783`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（17/36）

**有卡**：`VAEDecode`、`TextEncodeQwenImage21`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`LoadImage`、`KSampler`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPLoader`、`CR Text`、`TextGenerateLTX2Prompt`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
