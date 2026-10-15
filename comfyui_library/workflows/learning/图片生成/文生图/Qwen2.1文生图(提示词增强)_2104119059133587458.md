---
key: 图片生成/文生图/Qwen2.1文生图(提示词增强)_2104119059133587458.json
name: Qwen2.1文生图(提示词增强)_2104119059133587458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图(提示词增强)_2104119059133587458.json
hash: 33ee7e1917432f21
coverage: 0.933333
learned_at: 2026-10-10 20:59:06
nodes: [ConditioningZeroOut, VAELoader, CLIPLoader, VAEDecode, EmptyLatentImage, KSampler, TextGenerate, CLIPLoader, easy clearCacheAll, TextEncodeQwenImage21, SaveImage, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, StringConstantMultiline]
patterns: []
missing: [easy clearCacheAll]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1031030167875879, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen2.1文生图(提示词增强)_2104119059133587458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图(提示词增强)_2104119059133587458.json`

## 结构

**节点**（15 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode`
- `EmptyLatentImage`
- `KSampler`
- `TextGenerate`
- `CLIPLoader`
- `easy clearCacheAll`
- `TextEncodeQwenImage21`
- `SaveImage`
- `ResolutionSelector`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `StringConstantMultiline`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1031030167875879`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`TextGenerate`、`easy clearCacheAll`、`TextEncodeQwenImage21`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（1）：`easy clearCacheAll`

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
