---
key: 图片生成/图生图/Qwen_Image2.1丨姿势迁移_2111276056136208386.json
name: Qwen_Image2.1丨姿势迁移_2111276056136208386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image2.1丨姿势迁移_2111276056136208386.json
hash: 089950b1c4ab0fa1
coverage: 0.76
learned_at: 2026-10-23 11:21:11
nodes: [UNETLoader, EmptySD3LatentImage, TextGenerate, VAELoader, CLIPLoader, BatchImagesNode, CR Text Concatenate, kkGetImage, OpenposePreprocessor, JjkText, QwenImage21Cache, ComfySwitchNode, KSampler, VAEDecode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, TextEncodeQwenImage21, Note, Int, LoadImage, LoadImage, JjkText, SaveImage, PreviewAny]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 853370434082797, "steps": 25}
---

# 图片生成/图生图/Qwen_Image2.1丨姿势迁移_2111276056136208386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image2.1丨姿势迁移_2111276056136208386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `TextGenerate`
- `VAELoader`
- `CLIPLoader`
- `BatchImagesNode`
- `CR Text Concatenate`
- `kkGetImage`
- `OpenposePreprocessor`
- `JjkText`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `Note`
- `Int`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `SaveImage`
- `PreviewAny`

## 关键参数

- `seed` = `853370434082797`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`UNETLoader`、`EmptySD3LatentImage`、`TextGenerate`、`VAELoader`、`CLIPLoader`、`BatchImagesNode`、`CR Text Concatenate`、`kkGetImage`、`OpenposePreprocessor`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`Int`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
