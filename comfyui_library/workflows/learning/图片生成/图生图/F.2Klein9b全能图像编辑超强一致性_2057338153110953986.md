---
key: 图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2057338153110953986.json
name: F.2Klein9b全能图像编辑超强一致性_2057338153110953986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2057338153110953986.json
hash: bfacf1bc5b5c0fe1
coverage: 0.956522
learned_at: 2026-10-23 10:52:42
nodes: [ImageScaleToTotalPixels, UNETLoader, CLIPLoader, VAELoader, CFGGuider, Image Comparer (rgthree), SaveImage, SamplerCustomAdvanced, VAEDecode, KSamplerSelect, EmptyFlux2LatentImage, VAEEncode, GetImageSize, ConditioningZeroOut, CLIPTextEncode, ReferenceLatent, ReferenceLatent, RandomNoise, Int, Flux2Scheduler, LoadImage, CR Text, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2057338153110953986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2057338153110953986.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `GetImageSize`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `Int`
- `Flux2Scheduler`
- `LoadImage`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`ImageScaleToTotalPixels`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`SaveImage`、`SamplerCustomAdvanced`、`VAEDecode`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`VAEEncode`、`GetImageSize`、`ConditioningZeroOut`、`CLIPTextEncode`、`ReferenceLatent`、`RandomNoise`、`Int`、`Flux2Scheduler`、`LoadImage`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
