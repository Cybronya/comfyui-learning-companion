---
key: 平台全量/nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505.json
name: nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505.json
hash: a8b7a613cf43b2b9
coverage: 0.514286
learned_at: 2026-11-14 01:15:33
nodes: [Seed Everywhere, Image Comparer (rgthree), GetNode, SetNode, MarkdownNote, VAEEncode, GetNode, SaveImage, SetNode, SetNode, Prompts Everywhere, GetNode, GetNode, GetNode, ImageStitch, GetNode, ImageStitch, GetNode, ImageStitch, PreviewImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, KSampler (Efficient), SetNode, GetNode, TextEncodeQwenImageEdit, GetNode, TextEncodeQwenImageEditPlus, MarkdownNote, LoadImage, LoadImage, LoadImage, CLIPLoader, CFGNorm, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 927331318286954, "steps": 8}
---

# 平台全量/nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505.json

> 来源文件 `comfyui_library/workflows/平台全量/nunchaku-qwen-image-edit-2509-lightningv2.0 多图修复_1972851463997333505.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（35 个）：
- `Seed Everywhere`
- `Image Comparer (rgthree)`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `VAEEncode` ★核心
- `GetNode`
- `SaveImage`
- `SetNode`
- `SetNode`
- `Prompts Everywhere`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageStitch`
- `GetNode`
- `ImageStitch`
- `GetNode`
- `ImageStitch`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `KSampler (Efficient)` ★核心
- `SetNode`
- `GetNode`
- `TextEncodeQwenImageEdit`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CFGNorm`
- `VAELoader`

## 关键参数

- `seed` = `927331318286954`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **51%**（18/35）

**有卡**：`Seed Everywhere`、`VAEEncode`、`SaveImage`、`Prompts Everywhere`、`ImageStitch`、`ModelSamplingAuraFlow`、`NunchakuQwenImageDiTLoader`、`KSampler (Efficient)`、`TextEncodeQwenImageEdit`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`CLIPLoader`、`CFGNorm`、`VAELoader`

**用到的条目**：VAELoader、CLIPLoader、LoadImage、CFGNorm、KSampler (Efficient)、Seed Everywhere、TextEncodeQwenImageEdit、TextEncodeQwenImageEditPlus
