---
key: 图片生成/图生图/FLUX.2 Klein去水印＋高清放大急速版（超级猛）_2011780445423280130.json
name: FLUX.2 Klein去水印＋高清放大急速版（超级猛）_2011780445423280130
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein去水印＋高清放大急速版（超级猛）_2011780445423280130.json
hash: e5ad23e760d7c37b
coverage: 0.95122
learned_at: 2026-10-23 10:54:07
nodes: [CLIPLoader, UNETLoader, FluxGuidance, VAELoader, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, VAEDecode, CLIPTextEncode, KSampler, ImageResize+, SimpleMath+, DF_Integer, ImageResize+, TTP_Image_Tile_Batch, Cut By Mask, Get Image Size, ImpactMinMax, ImageCASharpening+, SeedVR2, TTP_Image_Assy, Get Image Size, ImageScale, easy cleanGpuUsed, InvertMask (segment anything), MaskToImage, DF_Integer, CR Value, CR Value, CR Value, CR Value, CR Value, CR Value, SaveImage, AutoImageResize, Image Comparer (rgthree), ImageCASharpening+, LoadImage, easy anythingIndexSwitch, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1116021421071361, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2 Klein去水印＋高清放大急速版（超级猛）_2011780445423280130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein去水印＋高清放大急速版（超级猛）_2011780445423280130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `FluxGuidance`
- `VAELoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageResize+`
- `SimpleMath+`
- `DF_Integer`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `Cut By Mask`
- `Get Image Size`
- `ImpactMinMax`
- `ImageCASharpening+`
- `SeedVR2`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImageScale`
- `easy cleanGpuUsed`
- `InvertMask (segment anything)`
- `MaskToImage`
- `DF_Integer`
- `CR Value`
- `CR Value`
- `CR Value`
- `CR Value`
- `CR Value`
- `CR Value`
- `SaveImage`
- `AutoImageResize`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `LoadImage`
- `easy anythingIndexSwitch`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1116021421071361`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`CLIPLoader`、`UNETLoader`、`FluxGuidance`、`VAELoader`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`ImageResize+`、`SimpleMath+`、`DF_Integer`、`TTP_Image_Tile_Batch`、`Cut By Mask`、`Get Image Size`、`ImpactMinMax`、`ImageCASharpening+`、`SeedVR2`、`TTP_Image_Assy`、`ImageScale`、`easy cleanGpuUsed`、`InvertMask (segment anything)`、`MaskToImage`、`CR Value`、`SaveImage`、`AutoImageResize`、`LoadImage`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
