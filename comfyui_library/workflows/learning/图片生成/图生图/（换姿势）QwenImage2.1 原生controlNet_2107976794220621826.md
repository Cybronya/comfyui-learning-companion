---
key: 图片生成/图生图/（换姿势）QwenImage2.1 原生controlNet_2107976794220621826.json
name: （换姿势）QwenImage2.1 原生controlNet_2107976794220621826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（换姿势）QwenImage2.1 原生controlNet_2107976794220621826.json
hash: 06aa4f407da5b1dd
coverage: 0.703704
learned_at: 2026-10-21 00:57:13
nodes: [MarkdownNote, MarkdownNote, QwenImage21Cache, CLIPLoader, VAELoader, ComfySwitchNode, TextGenerate, UNETLoader, JjkText, Note, OpenposePreprocessor, VAEDecode, JjkText, CR Text Concatenate, BatchImagesNode, kkGetImage, TextEncodeQwenImage21, CLIPLoader, EmptySD3LatentImage, SaveImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, PreviewAny, LoadImage, LoadImage, Int, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 476744003474762, "steps": 25}
---

# 图片生成/图生图/（换姿势）QwenImage2.1 原生controlNet_2107976794220621826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（换姿势）QwenImage2.1 原生controlNet_2107976794220621826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `MarkdownNote`
- `MarkdownNote`
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `ComfySwitchNode`
- `TextGenerate`
- `UNETLoader` ★核心
- `JjkText`
- `Note`
- `OpenposePreprocessor`
- `VAEDecode` ★核心
- `JjkText`
- `CR Text Concatenate`
- `BatchImagesNode`
- `kkGetImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `SaveImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `Int`
- `PreviewImage`

## 关键参数

- `seed` = `476744003474762`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`TextGenerate`、`UNETLoader`、`OpenposePreprocessor`、`VAEDecode`、`CR Text Concatenate`、`BatchImagesNode`、`kkGetImage`、`TextEncodeQwenImage21`、`EmptySD3LatentImage`、`SaveImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
