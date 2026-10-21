---
key: 图片生成/图生图/qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610.json
name: qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610.json
hash: 76a31b6dcece78ef
coverage: 0.785714
learned_at: 2026-10-21 00:46:20
nodes: [UNETLoader, CLIPLoader, VAELoader, KSamplerSelect, VAEDecode, ManualSigmas, SaveImage, SamplerCustom, ResolutionSelector, EmptyLatentImage, easy showAnything, easy showAnything, TextEncodeQwenImage21, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `ManualSigmas`
- `SaveImage`
- `SamplerCustom` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`VAEDecode`、`ManualSigmas`、`SaveImage`、`SamplerCustom`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader、KSamplerSelect
