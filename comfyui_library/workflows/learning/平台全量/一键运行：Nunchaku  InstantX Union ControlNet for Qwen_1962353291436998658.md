---
key: 平台全量/一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658.json
name: 一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658.json
hash: f4505f1da1fe57b5
coverage: 0.740741
learned_at: 2026-11-14 01:30:08
nodes: [PreviewImage, LayerFilter: HDREffects, PreviewImage, ModelSamplingAuraFlow, CLIPLoader, NunchakuQwenImageDiTLoader, KSampler (Efficient), Anything Everywhere, Anything Everywhere, PreviewImage, ConditioningZeroOut, Anything Everywhere, ControlNetApplySD3, AIO_Preprocessor, SetUnionControlNetType, Seed Everywhere, KSampler (Efficient), LoadImage, StringConstantMultiline, VAELoader, ControlNetLoader, Prompts Everywhere, CLIPTextEncode, VAEEncode, LayerFilter: HDREffects, SaveImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 515590450038029, "steps": 30}
---

# 平台全量/一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Nunchaku  InstantX Union ControlNet for Qwen_1962353291436998658.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Output → Other

**节点**（27 个）：
- `PreviewImage`
- `LayerFilter: HDREffects`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `NunchakuQwenImageDiTLoader`
- `KSampler (Efficient)` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `PreviewImage`
- `ConditioningZeroOut`
- `Anything Everywhere`
- `ControlNetApplySD3` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `Seed Everywhere`
- `KSampler (Efficient)` ★核心
- `LoadImage`
- `StringConstantMultiline`
- `VAELoader`
- `ControlNetLoader`
- `Prompts Everywhere`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerFilter: HDREffects`
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `seed` = `515590450038029`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.75`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LayerFilter: HDREffects`、`ModelSamplingAuraFlow`、`CLIPLoader`、`NunchakuQwenImageDiTLoader`、`KSampler (Efficient)`、`ConditioningZeroOut`、`ControlNetApplySD3`、`AIO_Preprocessor`、`SetUnionControlNetType`、`Seed Everywhere`、`LoadImage`、`StringConstantMultiline`、`VAELoader`、`ControlNetLoader`、`Prompts Everywhere`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplySD3、ControlNetLoader、SetUnionControlNetType
