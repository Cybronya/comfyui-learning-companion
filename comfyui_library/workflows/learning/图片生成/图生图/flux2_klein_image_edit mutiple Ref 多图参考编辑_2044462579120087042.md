---
key: 图片生成/图生图/flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042.json
name: flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042.json
hash: 02c2640c7a2730d1
coverage: 0.96
learned_at: 2026-10-23 11:36:33
nodes: [ConditioningZeroOut, MarkdownNote, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, VAEDecode, SaveImage, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetImageSize, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, LoadImage, CLIPLoader, VAELoader, LoadImage, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ConditioningZeroOut`
- `MarkdownNote`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **96%**（24/25）

**有卡**：`ConditioningZeroOut`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`SaveImage`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`GetImageSize`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
