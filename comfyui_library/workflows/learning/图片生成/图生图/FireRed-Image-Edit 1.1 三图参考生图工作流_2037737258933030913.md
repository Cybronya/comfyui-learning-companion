---
key: 图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json
name: FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json
hash: 0611aab3514077c7
coverage: 0.913043
learned_at: 2026-10-23 10:55:31
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingAuraFlow, CFGNorm, VAEDecode, KSampler, CLIPTextEncode, CLIPLoader, VAELoader, LoadImage, PrimitiveInt, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Text, EmptySD3LatentImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1044474294354693, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Text`
- `EmptySD3LatentImage`
- `SaveImage`

## 关键参数

- `seed` = `1044474294354693`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`CR Text`、`EmptySD3LatentImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
