---
key: 图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json
name: Qwen-Image-2.1 参考生图标准版_2104454950465138689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json
hash: 46256ba5bbf217d1
coverage: 0.722222
learned_at: 2026-10-07 02:41:04
nodes: [UNETLoader, CLIPLoader, MarkdownNote, VAELoader, EmptyLatentImage, TextGenerate, PrimitiveStringMultiline, PreviewAny, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, LoadImage, CR Text, MarkdownNote, ResolutionSelector, CLIPLoader]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextGenerate`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `CR Text`
- `MarkdownNote`
- `ResolutionSelector`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerate`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`ResolutionSelector`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
