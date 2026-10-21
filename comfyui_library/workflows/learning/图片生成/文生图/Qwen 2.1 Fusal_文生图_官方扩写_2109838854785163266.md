---
key: 图片生成/文生图/Qwen 2.1 Fusal_文生图_官方扩写_2109838854785163266.json
name: Qwen 2.1 Fusal_文生图_官方扩写_2109838854785163266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 2.1 Fusal_文生图_官方扩写_2109838854785163266.json
hash: 08bc06a27d9c320f
coverage: 0.85
learned_at: 2026-10-21 02:54:01
nodes: [INTConstant, Note, CLIPLoader, StringConstantMultiline, TextGenerate, StringConstant, JoinStrings, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, Note, SaveImage, PreviewAny, ResolutionSelector, StringConstantMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1184, "sampler_name": "euler", "scheduler": "simple", "seed": 20261011, "steps": 40, "width": 896}
---

# 图片生成/文生图/Qwen 2.1 Fusal_文生图_官方扩写_2109838854785163266.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 2.1 Fusal_文生图_官方扩写_2109838854785163266.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `INTConstant`
- `Note`
- `CLIPLoader`
- `StringConstantMultiline`
- `TextGenerate`
- `StringConstant`
- `JoinStrings`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Note`
- `SaveImage`
- `PreviewAny`
- `ResolutionSelector`
- `StringConstantMultiline`

## 关键参数

- `width` = `896`
- `height` = `1184`
- `batch_size` = `1`
- `seed` = `20261011`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`INTConstant`、`CLIPLoader`、`StringConstantMultiline`、`TextGenerate`、`StringConstant`、`JoinStrings`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
