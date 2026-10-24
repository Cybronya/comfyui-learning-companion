---
key: 图片生成/图生图/Qwen inpaint， suitable for very small areas,_1963230055868641282.json
name: Qwen inpaint， suitable for very small areas,_1963230055868641282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen inpaint， suitable for very small areas,_1963230055868641282.json
hash: 3a8b983ee9257006
coverage: 0.88
learned_at: 2026-10-23 11:14:26
nodes: [EmptySD3LatentImage, ModelPatchLoader, GetImageSize, UNETLoader, VAELoader, Image Comparer (rgthree), Int, Text, VAEDecode, LoadImage, MaskPreview+, PreviewImage, easy sleep, CLIPTextEncode, ShowText, RH_Translator, CLIPTextEncode, KSampler, SaveImage, InpaintStitchImproved, QwenImageDiffsynthControlnet, CLIPLoader, LoraLoaderModelOnly, InpaintCropImproved, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 35467246157655, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen inpaint， suitable for very small areas,_1963230055868641282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen inpaint， suitable for very small areas,_1963230055868641282.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `EmptySD3LatentImage`
- `ModelPatchLoader`
- `GetImageSize`
- `UNETLoader` ★核心
- `VAELoader`
- `Image Comparer (rgthree)`
- `Int`
- `Text`
- `VAEDecode` ★核心
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `easy sleep`
- `CLIPTextEncode` ★核心
- `ShowText`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `InpaintStitchImproved`
- `QwenImageDiffsynthControlnet`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `InpaintCropImproved`
- `PreviewImage`

## 关键参数

- `seed` = `35467246157655`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`EmptySD3LatentImage`、`ModelPatchLoader`、`GetImageSize`、`UNETLoader`、`VAELoader`、`Int`、`Text`、`VAEDecode`、`LoadImage`、`MaskPreview+`、`easy sleep`、`CLIPTextEncode`、`ShowText`、`RH_Translator`、`KSampler`、`SaveImage`、`InpaintStitchImproved`、`QwenImageDiffsynthControlnet`、`CLIPLoader`、`LoraLoaderModelOnly`、`InpaintCropImproved`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
