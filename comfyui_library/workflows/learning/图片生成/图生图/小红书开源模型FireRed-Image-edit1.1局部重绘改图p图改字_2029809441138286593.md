---
key: 图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json
name: 小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json
hash: e5f8f1f5057a82d5
coverage: 1
learned_at: 2026-10-21 00:52:18
nodes: [ConditioningZeroOut, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAEDecode, CFGNorm, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, KSampler, easy cleanGpuUsed, LoadImage, CR Prompt Text, easy int, InpaintModelConditioning, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 639298048305674, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书开源模型FireRed-Image-edit1.1局部重绘改图p图改字_2029809441138286593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `CR Prompt Text`
- `easy int`
- `InpaintModelConditioning`
- `SaveImage`

## 关键参数

- `seed` = `639298048305674`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAEDecode`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`easy cleanGpuUsed`、`LoadImage`、`CR Prompt Text`、`easy int`、`InpaintModelConditioning`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
