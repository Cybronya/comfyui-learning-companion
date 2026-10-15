---
key: 图片生成/图生图/Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873.json
name: Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873.json
hash: efa335346cf53eab
coverage: 0.769231
learned_at: 2026-10-15 22:25:26
nodes: [MarkdownNote, Note, CLIPLoader, VAELoader, QwenImage21Cache, CLIPLoader, LoadImage, StringConstantMultiline, KSampler, easy seed, UNETLoader, StringReplace, StringConstantMultiline, TextGenerate, BatchImagesNode, VAEDecode, StringFunction|pysssss, PreviewAny, PreviewAny, EmptyLatentImage, Image Comparer (rgthree), ResolutionSelector, ComfySwitchNode, LoadImage, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 372980352069668, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `MarkdownNote`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `CLIPLoader`
- `LoadImage`
- `StringConstantMultiline`
- `KSampler` ★核心
- `easy seed`
- `UNETLoader` ★核心
- `StringReplace`
- `StringConstantMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `StringFunction|pysssss`
- `PreviewAny`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `ComfySwitchNode`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `372980352069668`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoadImage`、`StringConstantMultiline`、`KSampler`、`easy seed`、`UNETLoader`、`StringReplace`、`TextGenerate`、`BatchImagesNode`、`VAEDecode`、`StringFunction|pysssss`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
