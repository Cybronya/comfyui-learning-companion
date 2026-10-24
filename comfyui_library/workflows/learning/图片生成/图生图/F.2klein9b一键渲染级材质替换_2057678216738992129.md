---
key: 图片生成/图生图/F.2klein9b一键渲染级材质替换_2057678216738992129.json
name: F.2klein9b一键渲染级材质替换_2057678216738992129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein9b一键渲染级材质替换_2057678216738992129.json
hash: faa1f9754f48cbbc
coverage: 0.894737
learned_at: 2026-10-23 10:52:51
nodes: [ReferenceLatent, LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, easy ifElse, easy isMaskEmpty, LayerUtility: ImageMaskScaleAs, Mask Fill Holes, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, SetLatentNoiseMask, LayerMask: MaskGrow, MaskPreview, LayerUtility: ImageBlend, Note, BasicGuider, CLIPTextEncode, UNETLoader, MaskPreview, VAEDecode, VAELoader, ImageScaleToTotalPixels, easy positive, VAEEncode, VAEEncode, ReferenceLatent, RandomNoise, GetImageSize, Flux2Scheduler, SaveImage, Image Comparer (rgthree), Mask Fill Holes, easy imageSizeBySide, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.2klein9b一键渲染级材质替换_2057678216738992129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein9b一键渲染级材质替换_2057678216738992129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ReferenceLatent`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `easy ifElse`
- `easy isMaskEmpty`
- `LayerUtility: ImageMaskScaleAs`
- `Mask Fill Holes`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SetLatentNoiseMask`
- `LayerMask: MaskGrow`
- `MaskPreview`
- `LayerUtility: ImageBlend`
- `Note`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `MaskPreview`
- `VAEDecode` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `easy positive`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `GetImageSize`
- `Flux2Scheduler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Mask Fill Holes`
- `easy imageSizeBySide`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LoadImage`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`ReferenceLatent`、`LayerMask: MaskGrow`、`LayerUtility: ImageMaskScaleAs`、`easy isMaskEmpty`、`Mask Fill Holes`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`SetLatentNoiseMask`、`MaskPreview`、`LayerUtility: ImageBlend`、`BasicGuider`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`VAELoader`、`ImageScaleToTotalPixels`、`easy positive`、`VAEEncode`、`RandomNoise`、`GetImageSize`、`Flux2Scheduler`、`SaveImage`、`easy imageSizeBySide`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced
