---
key: 图片生成/图生图/无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601.json
name: 无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601.json
hash: 75a385e53085d3b9
coverage: 1
learned_at: 2026-10-23 13:04:40
nodes: [CLIPLoader, ModelSamplingAuraFlow, CFGNorm, ConditioningZeroOut, GetImageSize+, EmptySD3LatentImage, KSampler, VAELoader, VAEDecode, SaveImage, ImageScaleDownToSize, ImageScaleDownToSize, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 642214318976014, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `ConditioningZeroOut`
- `GetImageSize+`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageScaleDownToSize`
- `ImageScaleDownToSize`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `642214318976014`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`ConditioningZeroOut`、`GetImageSize+`、`EmptySD3LatentImage`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`ImageScaleDownToSize`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
