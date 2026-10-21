---
key: 图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json
name: FLUX.2 [Klein] 多图编辑_2074481156397035521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json
hash: 4d9bd3c624d06141
coverage: 0.939024
learned_at: 2026-10-20 00:18:56
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEEncode, Anything Everywhere3, ReferenceLatent, ReferenceLatent, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoadImage, CR Text, UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, LoadImage, LoadImage, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, LoadImage, CR Text, VAEDecode, VAEDecode, SaveImage, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleByAspectRatio, ImageConcanate, ImageConcanate, SaveImage, ImageConcanate, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), 孤海注释, LoadImage, LayerUtility: ImageScaleByAspectRatio, CR Text]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `Anything Everywhere3`
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoadImage`
- `CR Text`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleByAspectRatio`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio`
- `CR Text`

## 知识

覆盖率 **94%**（77/82）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LayerUtility: ImageScaleByAspectRatio`、`LoadImage`、`CR Text`、`VAEDecode`、`SaveImage`、`ImageConcanate`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
