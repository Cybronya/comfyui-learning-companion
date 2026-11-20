---
key: 平台全量/小红书FireRed-Image-edit1.1局部重绘_2039272086446809090.json
name: 小红书FireRed-Image-edit1.1局部重绘_2039272086446809090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/小红书FireRed-Image-edit1.1局部重绘_2039272086446809090.json
hash: 6880ac1dd9b9b0a0
coverage: 1
learned_at: 2026-11-14 02:01:23
nodes: [VAELoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAEDecode, CFGNorm, TextEncodeQwenImageEditPlus, KSampler, easy cleanGpuUsed, InpaintModelConditioning, SaveImage, UNETLoader, LoadImage, easy int, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, CLIPLoader, CLIPLoader, CLIPLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 942875358947763, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/小红书FireRed-Image-edit1.1局部重绘_2039272086446809090.json

> 来源文件 `comfyui_library/workflows/平台全量/小红书FireRed-Image-edit1.1局部重绘_2039272086446809090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `InpaintModelConditioning`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `easy int`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`

## 关键参数

- `seed` = `942875358947763`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAEDecode`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`KSampler`、`easy cleanGpuUsed`、`InpaintModelConditioning`、`SaveImage`、`UNETLoader`、`LoadImage`、`easy int`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
