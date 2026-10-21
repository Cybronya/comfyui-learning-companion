---
key: 图片生成/图生图/qwen image 2.1 10图编辑_2105493076268634114.json
name: qwen image 2.1 10图编辑_2105493076268634114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1 10图编辑_2105493076268634114.json
hash: 29866db7e804ef67
coverage: 0.238462
learned_at: 2026-10-21 00:46:00
nodes: [ResolutionSelector, MarkdownNote, LoadImage, LoadImage, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveStringMultiline, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, PrimitiveBoolean, VAEDecode, SaveImage, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, TextEncodeQwenImage21, Reroute, PrimitiveInt, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 538818331299475, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen image 2.1 10图编辑_2105493076268634114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1 10图编辑_2105493076268634114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（130 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SaveImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImage21`
- `Reroute`
- `PrimitiveInt`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `538818331299475`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **24%**（31/130）

**有卡**：`ResolutionSelector`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`ComfyMathExpression`、`PrimitiveBoolean`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
