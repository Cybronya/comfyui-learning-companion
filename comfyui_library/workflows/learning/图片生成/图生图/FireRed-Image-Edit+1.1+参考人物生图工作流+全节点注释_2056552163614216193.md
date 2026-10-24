---
key: 图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json
name: FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json
hash: 163a71374cbedea1
coverage: 0.5
learned_at: 2026-10-23 10:55:41
nodes: [LoraLoaderModelOnly, CFGNorm, PrimitiveInt, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, ModelSamplingAuraFlow, EmptySD3LatentImage, KSampler, VAEDecode, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, SaveImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, CR Text, LoadImage, TextEncodeQwenImageEditPlus]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 301970920978961, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `PrimitiveInt`
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
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`

## 关键参数

- `seed` = `301970920978961`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **50%**（20/40）

**有卡**：`LoraLoaderModelOnly`、`CFGNorm`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`CR Text`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
