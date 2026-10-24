---
key: 图片生成/图生图/最强万物迁移 f2k_9b_anything change clothes_2026650952215826434.json
name: 最强万物迁移 f2k_9b_anything change clothes_2026650952215826434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强万物迁移 f2k_9b_anything change clothes_2026650952215826434.json
hash: e02c32732b78e236
coverage: 0.967742
learned_at: 2026-10-23 13:05:40
nodes: [easy imageScaleDownToSize, CR Text, VAEEncode, UNETLoader, easy imageScaleDownToSize, VAELoader, CLIPTextEncode, CFGGuider, Flux2Scheduler, GetImageSize, EmptyFlux2LatentImage, ReferenceLatent, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, LoraLoaderModelOnly, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAEDecode, SaveImage, Image Comparer (rgthree), ImageConcanate, ImageConcanate, SaveImage, LoraLoaderModelOnly, CLIPLoader, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/最强万物迁移 f2k_9b_anything change clothes_2026650952215826434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强万物迁移 f2k_9b_anything change clothes_2026650952215826434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `easy imageScaleDownToSize`
- `CR Text`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `easy imageScaleDownToSize`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`easy imageScaleDownToSize`、`CR Text`、`VAEEncode`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`CFGGuider`、`Flux2Scheduler`、`GetImageSize`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`CLIPLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
