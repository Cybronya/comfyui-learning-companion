---
key: 图片生成/图生图/qwen image 2.1 图编辑_2102212148364668930.json
name: qwen image 2.1 图编辑_2102212148364668930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1 图编辑_2102212148364668930.json
hash: 1f3b473a3b8d7e4a
coverage: 0.866667
learned_at: 2026-10-10 20:48:12
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, VAEDecode, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 112054580236127, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen image 2.1 图编辑_2102212148364668930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1 图编辑_2102212148364668930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `112054580236127`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`VAEDecode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
