---
key: 图片生成/文生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209.json
name: 万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209.json
hash: 8944de10bdcc64d6
coverage: 0.947368
learned_at: 2026-10-21 02:58:23
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, EmptySD3LatentImage, ModelSamplingAuraFlow, CFGNorm, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, CR Text, LoadImage, KSampler, PrimitiveInt, VAELoader, CLIPTextEncode, CLIPLoader, TextEncodeQwenImageEditPlus]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 681341928091460, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `CR Text`
- `LoadImage`
- `KSampler` ★核心
- `PrimitiveInt`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`

## 关键参数

- `seed` = `681341928091460`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`CR Text`、`LoadImage`、`KSampler`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
