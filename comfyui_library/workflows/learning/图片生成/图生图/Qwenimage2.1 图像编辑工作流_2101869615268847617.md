---
key: 图片生成/图生图/Qwenimage2.1 图像编辑工作流_2101869615268847617.json
name: Qwenimage2.1 图像编辑工作流_2101869615268847617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwenimage2.1 图像编辑工作流_2101869615268847617.json
hash: f9b43f5b5699b6a6
coverage: 0.72093
learned_at: 2026-10-21 00:44:03
nodes: [CLIPLoader, TextGenerateLTX2Prompt, VAEDecode, UNETLoader, TextEncodeQwenImage21, VAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, StringConcatenate, easy showAnything, EmptyLatentImage, ComfySwitchNode, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, NanFengH3LimitImageLongEdge, BatchImagesNode, Reroute, SaveImage, ResolutionSelector, SaveImageAdvanced, CLIPLoader, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveBoolean, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 35242610328570, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwenimage2.1 图像编辑工作流_2101869615268847617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwenimage2.1 图像编辑工作流_2101869615268847617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `StringConcatenate`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `NanFengH3LimitImageLongEdge`
- `BatchImagesNode`
- `Reroute`
- `SaveImage`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `CLIPLoader`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `35242610328570`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **72%**（31/43）

**有卡**：`CLIPLoader`、`TextGenerateLTX2Prompt`、`VAEDecode`、`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`StringConcatenate`、`EmptyLatentImage`、`NanFengH3LimitImageLongEdge`、`BatchImagesNode`、`SaveImage`、`ResolutionSelector`、`SaveImageAdvanced`、`KSampler`、`LoadImage`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
