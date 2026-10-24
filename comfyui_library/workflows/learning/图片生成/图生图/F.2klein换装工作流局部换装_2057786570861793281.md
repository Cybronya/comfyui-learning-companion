---
key: 图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json
name: F.2klein换装工作流局部换装_2057786570861793281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json
hash: 8bc33e81ab35052c
coverage: 0.87931
learned_at: 2026-10-23 10:52:54
nodes: [LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, Mask Fill Holes, ImpactNeg, LayerMask: MaskGrow, Int, Int, easy int, easy imageSizeBySide, easy ifElse, Bool, BlockifyMask, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, 取色器_孤海, CLIPLoader, VAELoader, VAEEncode, CLIPTextEncode, SmartColorMatch, 图像接缝, easy imageSize, LayerMask: MaskGrow, ImageScale, LayerColor: BrightnessContrastV2, VAEDecode, easy isMaskEmpty, MaskPreview, easy ifElse, easy compare, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImpactMakeAnyList, easy ifElse, InpaintCropImproved, MaskPreview, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ReferenceLatent, ReferenceLatent, UNETLoader, VAEEncode, easy imageSize, BasicGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, Image Comparer (rgthree), SaveImage, ImpactMakeAnyList, ImpactMakeAnyList, ImpactMakeAnyList, Text Multiline, Image Comparer (rgthree), LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `Mask Fill Holes`
- `ImpactNeg`
- `LayerMask: MaskGrow`
- `Int`
- `Int`
- `easy int`
- `easy imageSizeBySide`
- `easy ifElse`
- `Bool`
- `BlockifyMask`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `取色器_孤海`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SmartColorMatch`
- `图像接缝`
- `easy imageSize`
- `LayerMask: MaskGrow`
- `ImageScale`
- `LayerColor: BrightnessContrastV2`
- `VAEDecode` ★核心
- `easy isMaskEmpty`
- `MaskPreview`
- `easy ifElse`
- `easy compare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImpactMakeAnyList`
- `easy ifElse`
- `InpaintCropImproved`
- `MaskPreview`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `easy imageSize`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImpactMakeAnyList`
- `ImpactMakeAnyList`
- `ImpactMakeAnyList`
- `Text Multiline`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **88%**（51/58）

**有卡**：`LayerMask: MaskGrow`、`LayerUtility: ImageMaskScaleAs`、`Mask Fill Holes`、`ImpactNeg`、`Int`、`easy int`、`easy imageSizeBySide`、`Bool`、`BlockifyMask`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageBlend`、`取色器_孤海`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`CLIPTextEncode`、`SmartColorMatch`、`图像接缝`、`easy imageSize`、`ImageScale`、`LayerColor: BrightnessContrastV2`、`VAEDecode`、`easy isMaskEmpty`、`MaskPreview`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactMakeAnyList`、`InpaintCropImproved`、`ReferenceLatent`、`UNETLoader`、`BasicGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`RandomNoise`、`SamplerCustomAdvanced`、`SaveImage`、`Text Multiline`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced
