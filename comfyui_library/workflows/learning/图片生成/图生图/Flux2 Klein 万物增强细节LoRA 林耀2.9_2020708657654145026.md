---
key: 图片生成/图生图/Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026.json
name: Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026.json
hash: a58d2b0e7e4887c8
coverage: 0.952381
learned_at: 2026-10-23 10:59:08
nodes: [ReferenceLatent, ConditioningZeroOut, ReferenceLatent, RandomNoise, SamplerCustomAdvanced, VAEEncode, CFGGuider, VAEDecode, GetImageSize, Flux2Scheduler, Image Comparer (rgthree), EmptyFlux2LatentImage, VAELoader, CLIPLoader, UNETLoader, KSamplerSelect, SaveImage, LoraLoaderModelOnly, LoadImage, ImageScaleToTotalPixels, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `GetImageSize`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEEncode`、`CFGGuider`、`VAEDecode`、`GetImageSize`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`KSamplerSelect`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`ImageScaleToTotalPixels`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
