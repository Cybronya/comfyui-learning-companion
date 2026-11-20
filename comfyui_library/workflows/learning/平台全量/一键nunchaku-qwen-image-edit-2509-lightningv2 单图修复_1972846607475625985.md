---
key: 平台全量/一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985.json
name: 一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985.json
hash: d68e268147c79de5
coverage: 0.56
learned_at: 2026-11-14 01:27:20
nodes: [Seed Everywhere, Prompts Everywhere, GetNode, SetNode, GetNode, ImageStitch, MarkdownNote, GetNode, SetNode, VAEEncode, GetNode, GetNode, PreviewImage, ModelSamplingAuraFlow, SaveImage, Image Comparer (rgthree), KSampler (Efficient), TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, LoadImage, CFGNorm, CLIPLoader, VAELoader, NunchakuQwenImageDiTLoader, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 927331318286954, "steps": 8}
---

# 平台全量/一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985.json

> 来源文件 `comfyui_library/workflows/平台全量/一键nunchaku-qwen-image-edit-2509-lightningv2 单图修复_1972846607475625985.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（25 个）：
- `Seed Everywhere`
- `Prompts Everywhere`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageStitch`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)` ★核心
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `NunchakuQwenImageDiTLoader`
- `MarkdownNote`

## 关键参数

- `seed` = `927331318286954`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **56%**（14/25）

**有卡**：`Seed Everywhere`、`Prompts Everywhere`、`ImageStitch`、`VAEEncode`、`ModelSamplingAuraFlow`、`SaveImage`、`KSampler (Efficient)`、`TextEncodeQwenImageEdit`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`CFGNorm`、`CLIPLoader`、`VAELoader`、`NunchakuQwenImageDiTLoader`

**用到的条目**：VAELoader、CLIPLoader、LoadImage、CFGNorm、KSampler (Efficient)、Seed Everywhere、TextEncodeQwenImageEdit、TextEncodeQwenImageEditPlus
