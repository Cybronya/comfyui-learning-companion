---
key: 图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json
name: Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json
hash: d90bc97d1bb2911f
coverage: 0.481481
learned_at: 2026-10-10 20:59:07
nodes: [VAELoader, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, SaveImage, SetNode, EmptyLatentImage, GetNode, SetNode, CLIPLoader, UNETLoader, GetNode, TextEncodeQwenImage21, GetNode, SetNode, TextGenerate, SetNode, KSampler, CLIPLoader, StringConstantMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 741320868460022, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json`

## 结构

**节点**（27 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `VAEDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SaveImage`
- `SetNode`
- `EmptyLatentImage`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `TextGenerate`
- `SetNode`
- `KSampler`
- `CLIPLoader`
- `StringConstantMultiline`
- `ResolutionSelector`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `741320868460022`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **48%**（13/27）

**有卡**：`VAELoader`、`SetNode`、`VAEDecode`、`GetNode`、`ConditioningZeroOut`、`SaveImage`、`EmptyLatentImage`
