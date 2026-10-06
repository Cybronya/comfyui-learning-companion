---
key: 图片生成/文生图/Qwen2.1文_图生图(提示词增强)_2106902512568717313.json
name: Qwen2.1文_图生图(提示词增强)_2106902512568717313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文_图生图(提示词增强)_2106902512568717313.json
hash: 5c9150c4d60a7f3a
coverage: 0.809524
learned_at: 2026-10-06 22:39:00
nodes: [ConditioningZeroOut, VAELoader, KSampler, easy clearCacheAll, easy saveText, VAEDecode, TextEncodeQwenImage21, TextGenerate, LoadImage, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ResolutionSelector, PreviewImage, PreviewAny, EmptyLatentImage, CLIPLoader, CLIPLoader, StringConstantMultiline]
patterns: []
missing: [easy clearCacheAll, easy saveText]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 415955680930716, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen2.1文_图生图(提示词增强)_2106902512568717313.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文_图生图(提示词增强)_2106902512568717313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
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

## 关键参数

- `seed` = `415955680930716`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`TextGenerate`、`LoadImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`StringConstantMultiline`

**缺卡**（2）：`easy clearCacheAll`、`easy saveText`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
