---
key: 图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json
name: 一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json
hash: ba5c0e6b613dd3a1
coverage: 0.555556
learned_at: 2026-10-10 20:59:33
nodes: [LayerFilter: HDREffects, Anything Everywhere, Anything Everywhere, Anything Everywhere, SetUnionControlNetType, Seed Everywhere, UNETLoader, ModelSamplingAuraFlow, Prompts Everywhere, AIO_Preprocessor, PreviewImage, ControlNetApplySD3, LoadImage, LoraLoaderModelOnly, VAEEncode, ControlNetLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, StringConstantMultiline, PreviewImage, VAELoader, PreviewImage, KSampler (Efficient), KSampler (Efficient), SaveImage, MarkdownNote]
patterns: []
missing: [LayerFilter: HDREffects, KSampler (Efficient), KSampler (Efficient), Prompts Everywhere, Seed Everywhere]
parameters: {"cfg": 2.5, "controlnet_strength": 1, "denoise": 0.5000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 451677997825500, "steps": 20}
discoveries: [次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识, 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一键运行：标准 Qwen InstantX Union ControlNet 图像控制_1962344245782888449.json`

## 结构

**节点**（27 个）：
- `LayerFilter: HDREffects`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `SetUnionControlNetType`
- `Seed Everywhere`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `Prompts Everywhere`
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetApplySD3`
- `LoadImage`
- `LoraLoaderModelOnly`
- `VAEEncode`
- `ControlNetLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `StringConstantMultiline`
- `PreviewImage`
- `VAELoader`
- `PreviewImage`
- `KSampler (Efficient)`
- `KSampler (Efficient)`
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `cfg` = `2.5`
- `controlnet_strength` = `1`
- `denoise` = `0.5000000000000001`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `451677997825500`
- `steps` = `20`

## 知识

覆盖率 **56%**（15/27）

**有卡**：`LayerFilter: HDREffects`、`Anything Everywhere`、`SetUnionControlNetType`、`Seed Everywhere`、`UNETLoader`、`ModelSamplingAuraFlow`、`Prompts Everywhere`、`AIO_Preprocessor`、`PreviewImage`、`ControlNetApplySD3`、`LoadImage`、`LoraLoaderModelOnly`、`VAEEncode`

**缺卡**（5）：`LayerFilter: HDREffects`、`KSampler (Efficient)`、`KSampler (Efficient)`、`Prompts Everywhere`、`Seed Everywhere`

## 学习发现

- 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识
- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
