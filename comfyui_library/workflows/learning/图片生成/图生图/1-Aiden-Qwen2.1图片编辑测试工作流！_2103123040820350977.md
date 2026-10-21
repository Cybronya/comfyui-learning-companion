---
key: 图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json
name: 1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json
hash: 91e3cbb4902c20cd
coverage: 0.780488
learned_at: 2026-10-21 00:38:21
nodes: [孤海注释, MarkdownNote, 孤海注释, 孤海注释, PreviewImage, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, KSampler, QwenImage21Cache, 忽略多组孤海, LoadImage, LoadImage, LoadImage, 孤海注释, CLIPLoader, BatchImagesNode, EmptyLatentImage, UNETLoader, PrimitiveBoolean, ResolutionSelector, TextGenerate, easy positive, JoinStrings, LoadImage, easy positive, CLIPLoader, ShowText|pysssss, TextEncodeQwenImage21, ComfySwitchNode, VAELoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageConcatMulti, ModelPreviewOverrideKJ, PreviewImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 210, "steps": 25, "width": 1024}
---

# 图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/1-Aiden-Qwen2.1图片编辑测试工作流！_2103123040820350977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `孤海注释`
- `MarkdownNote`
- `孤海注释`
- `孤海注释`
- `PreviewImage`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `KSampler` ★核心
- `QwenImage21Cache`
- `忽略多组孤海`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `ResolutionSelector`
- `TextGenerate`
- `easy positive`
- `JoinStrings`
- `LoadImage`
- `easy positive`
- `CLIPLoader`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageConcatMulti`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `210`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（32/41）

**有卡**：`忽略多组孤海`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`UNETLoader`、`PrimitiveBoolean`、`ResolutionSelector`、`TextGenerate`、`easy positive`、`JoinStrings`、`TextEncodeQwenImage21`、`VAELoader`、`ImageScaleToTotalPixels`、`ImageConcatMulti`、`ModelPreviewOverrideKJ`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
