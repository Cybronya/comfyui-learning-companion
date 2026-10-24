---
key: 图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json
name: Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json
hash: 830a3aaac3108a49
coverage: 0.645161
learned_at: 2026-10-23 11:17:41
nodes: [UNETLoader, ModelSamplingAuraFlow, CFGNorm, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, TextEncodeQwenImageEditPlus, VAEEncode, ConditioningZeroOut, SetNode, GetNode, ImageScaleToTotalPixels, VAEDecode, GetNode, SaveImage, Image Comparer (rgthree), LoadImage, Text, SaveImage, LoadImage, SetNode, easy cleanGpuUsed, KSampler, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 324338566296109, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `GetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Text`
- `SaveImage`
- `LoadImage`
- `SetNode`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `324338566296109`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（20/31）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`LoadImage`、`Text`、`easy cleanGpuUsed`、`KSampler`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
