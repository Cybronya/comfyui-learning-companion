---
key: 图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json
name: Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json
hash: c72915eaa62c36bc
coverage: 0.966667
learned_at: 2026-10-23 10:58:45
nodes: [VAELoader, Anything Everywhere3, UNETLoader, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, CFGGuider, Flux2Scheduler, VAEDecode, CLIPTextEncode, ReferenceLatent, CLIPTextEncode, ReferenceLatent, easy imageSize, DifferentialDiffusion, InpaintModelConditioning, ImageAndMaskPreview, GrowMaskWithBlur, Mask Fill Holes, SaveImage, KOOK_SaveJPGImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, CR Text, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAELoader`
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `easy imageSize`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `ImageAndMaskPreview`
- `GrowMaskWithBlur`
- `Mask Fill Holes`
- `SaveImage`
- `KOOK_SaveJPGImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`CFGGuider`、`Flux2Scheduler`、`VAEDecode`、`CLIPTextEncode`、`ReferenceLatent`、`easy imageSize`、`DifferentialDiffusion`、`InpaintModelConditioning`、`ImageAndMaskPreview`、`GrowMaskWithBlur`、`Mask Fill Holes`、`SaveImage`、`KOOK_SaveJPGImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
