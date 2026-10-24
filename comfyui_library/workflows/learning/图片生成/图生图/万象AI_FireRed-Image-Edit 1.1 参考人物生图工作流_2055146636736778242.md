---
key: 图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json
name: 万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json
hash: fb5bfacbd3fb5947
coverage: 0.947368
learned_at: 2026-10-23 12:01:40
nodes: [LoraLoaderModelOnly, CFGNorm, PrimitiveInt, TextEncodeQwenImageEditPlus, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, ModelSamplingAuraFlow, EmptySD3LatentImage, KSampler, VAEDecode, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, SaveImage, CR Text, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1034794939130164, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `1034794939130164`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LoraLoaderModelOnly`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
