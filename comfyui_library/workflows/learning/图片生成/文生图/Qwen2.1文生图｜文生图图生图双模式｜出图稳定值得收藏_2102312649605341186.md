---
key: 图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json
name: Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json
hash: d90bc97d1bb2911f
coverage: 0.481481
learned_at: 2026-10-07 02:28:39
nodes: [VAELoader, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, SaveImage, SetNode, EmptyLatentImage, GetNode, SetNode, CLIPLoader, UNETLoader, GetNode, TextEncodeQwenImage21, GetNode, SetNode, TextGenerate, SetNode, KSampler, CLIPLoader, StringConstantMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 741320868460022, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SaveImage`
- `SetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `TextGenerate`
- `SetNode`
- `KSampler` ★核心
- `CLIPLoader`
- `StringConstantMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `741320868460022`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（13/27）

**有卡**：`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`TextGenerate`、`KSampler`、`StringConstantMultiline`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector
