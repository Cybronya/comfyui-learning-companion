---
key: 图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json
name: Flux2.Klein图像编辑与扩图重绘_2014617059883225089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json
hash: 6e165885b3193d52
coverage: 0.945946
learned_at: 2026-10-23 11:00:52
nodes: [KSamplerSelect, Flux2Scheduler, CFGGuider, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CFGGuider, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, RandomNoise, ReferenceLatent, ReferenceLatent, ReferenceLatent, GetImageSize, VAEEncode, GetImageSize, ReferenceLatent, ReferenceLatent, SamplerCustomAdvanced, EmptyFlux2LatentImage, SamplerCustomAdvanced, ReferenceLatent, SaveImage, KSamplerSelect, Flux2Scheduler, CFGGuider, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, RandomNoise, VAEEncode, GetImageSize, ReferenceLatent, SamplerCustomAdvanced, VAEDecode, ReferenceLatent, EmptyFlux2LatentImage, ImageScaleToTotalPixels, ImagePadForOutpaint, DrawMaskOnImage, ImageScaleToTotalPixels, VAEDecode, ImageScaleToTotalPixels, LoadImage, VAEDecode, CLIPTextEncode, VAEEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, easy imageConcat, SaveImage, RandomNoise, SaveImage, Image Comparer (rgthree), CLIPTextEncode, CLIPTextEncode, LoadImage, LoadImage, LoadImage, PreviewImage, SaveImage, Fast Groups Muter (rgthree), Note]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `RandomNoise`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `VAEEncode` ★核心
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `SaveImage`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `RandomNoise`
- `VAEEncode` ★核心
- `GetImageSize`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `ImagePadForOutpaint`
- `DrawMaskOnImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageConcat`
- `easy imageConcat`
- `SaveImage`
- `RandomNoise`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `Note`

## 知识

覆盖率 **95%**（70/74）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyFlux2LatentImage`、`RandomNoise`、`ReferenceLatent`、`GetImageSize`、`VAEEncode`、`SamplerCustomAdvanced`、`SaveImage`、`VAEDecode`、`ImageScaleToTotalPixels`、`ImagePadForOutpaint`、`DrawMaskOnImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageConcat`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
