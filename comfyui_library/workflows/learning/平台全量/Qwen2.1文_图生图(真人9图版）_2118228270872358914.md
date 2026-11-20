---
key: 平台全量/Qwen2.1文_图生图(真人9图版）_2118228270872358914.json
name: Qwen2.1文_图生图(真人9图版）_2118228270872358914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.1文_图生图(真人9图版）_2118228270872358914.json
hash: 81e54a1de09e0a92
coverage: 0.933333
learned_at: 2026-11-14 00:52:23
nodes: [ConditioningZeroOut, VAELoader, KSampler, easy clearCacheAll, easy saveText, VAEDecode, TextEncodeQwenImage21, TextGenerate, LoadImage, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ResolutionSelector, PreviewImage, PreviewAny, EmptyLatentImage, CLIPLoader, CLIPLoader, StringConstantMultiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextInput_]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 495531483484533, "steps": 40, "width": 1024}
---

# 平台全量/Qwen2.1文_图生图(真人9图版）_2118228270872358914.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.1文_图生图(真人9图版）_2118228270872358914.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `KSampler` ★核心
- `easy clearCacheAll`
- `easy saveText`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `TextGenerate`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `PreviewImage`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `StringConstantMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextInput_`

## 关键参数

- `seed` = `495531483484533`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`KSampler`、`easy clearCacheAll`、`easy saveText`、`VAEDecode`、`TextEncodeQwenImage21`、`TextGenerate`、`LoadImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`StringConstantMultiline`、`TextInput_`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
