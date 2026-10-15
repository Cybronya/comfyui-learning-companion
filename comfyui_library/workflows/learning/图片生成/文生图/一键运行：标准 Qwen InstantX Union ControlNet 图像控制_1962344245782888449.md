---
key: 图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json
name: 一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json
hash: ba5c0e6b613dd3a1
coverage: 0.740741
learned_at: 2026-10-15 22:28:08
nodes: [LayerFilter: HDREffects, Anything Everywhere, Anything Everywhere, Anything Everywhere, SetUnionControlNetType, Seed Everywhere, UNETLoader, ModelSamplingAuraFlow, Prompts Everywhere, AIO_Preprocessor, PreviewImage, ControlNetApplySD3, LoadImage, LoraLoaderModelOnly, VAEEncode, ControlNetLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, StringConstantMultiline, PreviewImage, VAELoader, PreviewImage, KSampler (Efficient), KSampler (Efficient), SaveImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1, "denoise": 0.5000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 451677997825500, "steps": 20}
---

# 图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Output → Other

**节点**（27 个）：
- `LayerFilter: HDREffects`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `SetUnionControlNetType`
- `Seed Everywhere`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `Prompts Everywhere`
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ControlNetLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `StringConstantMultiline`
- `PreviewImage`
- `VAELoader`
- `PreviewImage`
- `KSampler (Efficient)` ★核心
- `KSampler (Efficient)` ★核心
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `451677997825500`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LayerFilter: HDREffects`、`SetUnionControlNetType`、`Seed Everywhere`、`UNETLoader`、`ModelSamplingAuraFlow`、`Prompts Everywhere`、`AIO_Preprocessor`、`ControlNetApplySD3`、`LoadImage`、`LoraLoaderModelOnly`、`VAEEncode`、`ControlNetLoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`StringConstantMultiline`、`VAELoader`、`KSampler (Efficient)`、`SaveImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、ControlNetLoader
