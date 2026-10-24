---
key: 图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json
name: FireRedImageedit1.1小红书局部重绘改图_2056041789731164161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json
hash: 850ea2197be22af7
coverage: 1
learned_at: 2026-10-23 10:55:55
nodes: [ConditioningZeroOut, CLIPLoader, UNETLoader, VAELoader, ModelSamplingAuraFlow, VAEDecode, CFGNorm, TextEncodeQwenImageEditPlus, KSampler, easy cleanGpuUsed, SaveImage, LoadImage, MaskFillHoles, InpaintModelConditioning, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, Int, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 462888668289439, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRedImageedit1.1小红书局部重绘改图_2056041789731164161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `LoadImage`
- `MaskFillHoles`
- `InpaintModelConditioning`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `CR Prompt Text`

## 关键参数

- `seed` = `462888668289439`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`KSampler`、`easy cleanGpuUsed`、`SaveImage`、`LoadImage`、`MaskFillHoles`、`InpaintModelConditioning`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
