---
key: 图片生成/图生图/Flux.2 Klein 细节增强_2058818588181622785.json
name: Flux.2 Klein 细节增强_2058818588181622785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 细节增强_2058818588181622785.json
hash: a5ad1303f93df37a
coverage: 0.954545
learned_at: 2026-10-23 10:58:45
nodes: [ReferenceLatent, ConditioningZeroOut, ReferenceLatent, SamplerCustomAdvanced, VAEEncode, CFGGuider, EmptyFlux2LatentImage, GetImageSize, VAELoader, CLIPTextEncode, CLIPLoader, UNETLoader, VAEDecode, KSamplerSelect, PreviewImage, SaveImage, RandomNoise, ImageScaleToTotalPixels, LoraLoaderModelOnly, Flux2Scheduler, LoadImage, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 Klein 细节增强_2058818588181622785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 细节增强_2058818588181622785.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `PreviewImage`
- `SaveImage`
- `RandomNoise`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `Flux2Scheduler`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAEEncode`、`CFGGuider`、`EmptyFlux2LatentImage`、`GetImageSize`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`KSamplerSelect`、`SaveImage`、`RandomNoise`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`Flux2Scheduler`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
