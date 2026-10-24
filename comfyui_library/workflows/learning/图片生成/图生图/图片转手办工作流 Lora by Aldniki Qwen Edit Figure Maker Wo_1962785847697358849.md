---
key: 图片生成/图生图/图片转手办工作流 Lora by Aldniki Qwen Edit Figure Maker Wo_1962785847697358849.json
name: 图片转手办工作流 Lora by Aldniki Qwen Edit Figure Maker Wo_1962785847697358849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片转手办工作流 Lora by Aldniki Qwen Edit Figure Maker Wo_1962785847697358849.json
hash: 07110fac78a9c05c
coverage: 0.903226
learned_at: 2026-10-23 12:41:49
nodes: [VAELoader, ImageScaleBy, UpscaleModelLoader, VAEEncode, ModelSamplingAuraFlow, ModelSamplingAuraFlow, TextEncodeQwenImageEdit, CFGNorm, ImageUpscaleWithModel, VAEEncode, ImageScaleToTotalPixels, CFGNorm, Text Multiline, Text Multiline, Text Multiline, UnetLoaderGGUF, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler (Efficient), Text Multiline, TextEncodeQwenImageEdit, KSampler (Efficient), CLIPLoader, easy anythingIndexSwitch, Note, LoadImage, SaveImage, Image Comparer (rgthree), PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 1491, "steps": 8}
---

# 图片生成/图生图/图片转手办工作流 Lora by Aldniki Qwen Edit Figure Maker Wo_1962785847697358849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片转手办工作流 Lora by Aldniki Qwen Edit Figure Maker Wo_1962785847697358849.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（31 个）：
- `VAELoader`
- `ImageScaleBy`
- `UpscaleModelLoader`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEdit`
- `CFGNorm`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `CFGNorm`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `UnetLoaderGGUF` ★核心
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler (Efficient)` ★核心
- `Text Multiline`
- `TextEncodeQwenImageEdit`
- `KSampler (Efficient)` ★核心
- `CLIPLoader`
- `easy anythingIndexSwitch`
- `Note`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

## 关键参数

- `seed` = `1491`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`VAELoader`、`ImageScaleBy`、`UpscaleModelLoader`、`VAEEncode`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEdit`、`CFGNorm`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`Text Multiline`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`KSampler (Efficient)`、`CLIPLoader`、`easy anythingIndexSwitch`、`LoadImage`、`SaveImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、KSampler (Efficient)、TextEncodeQwenImageEdit、VAEEncode
