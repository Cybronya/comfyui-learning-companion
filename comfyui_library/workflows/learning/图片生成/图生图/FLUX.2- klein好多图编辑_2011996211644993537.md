---
key: 图片生成/图生图/FLUX.2- klein好多图编辑_2011996211644993537.json
name: FLUX.2- klein好多图编辑_2011996211644993537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2- klein好多图编辑_2011996211644993537.json
hash: aedb43737ca2e6f9
coverage: 0.88
learned_at: 2026-10-23 10:54:10
nodes: [Anything Everywhere3, CLIPLoader, UNETLoader, VAELoader, LoadImage, VAEEncode, VAEEncode, VAEEncode, ReferenceLatent, FluxKontextImageScale, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, Note, ReferenceLatent, EmptyFlux2LatentImage, EmptyFlux2LatentImage, KSamplerSelect, RandomNoise, BasicGuider, Flux2Scheduler, VAEDecode, SaveImage, CLIPTextEncode, FluxGuidance, LayerUtility: ImageReelComposit, SamplerCustomAdvanced, CR SDXL Aspect Ratio, LoadImage, LoadImage, VAEEncode, ReferenceLatent, FluxKontextImageScale, CR Latent Input Switch, ReferenceLatent, ReferenceLatent, LoadImage, SDPoseOODLoader, FluxKontextImageScale, LayerUtility: ImageReel, VAEEncode, SDPoseOODProcessor, PreviewImage, LoadImage, LayerUtility: ImageReel, SaveImage, MarkdownNote, MarkdownNote, easy imageSize, Fast Groups Bypasser (rgthree), CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2- klein好多图编辑_2011996211644993537.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2- klein好多图编辑_2011996211644993537.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `Anything Everywhere3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicGuider`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LayerUtility: ImageReelComposit`
- `SamplerCustomAdvanced` ★核心
- `CR SDXL Aspect Ratio`
- `LoadImage`
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxKontextImageScale`
- `CR Latent Input Switch`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `SDPoseOODLoader`
- `FluxKontextImageScale`
- `LayerUtility: ImageReel`
- `VAEEncode` ★核心
- `SDPoseOODProcessor`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageReel`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `easy imageSize`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`VAEEncode`、`ReferenceLatent`、`FluxKontextImageScale`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`Flux2Scheduler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`FluxGuidance`、`LayerUtility: ImageReelComposit`、`SamplerCustomAdvanced`、`CR SDXL Aspect Ratio`、`CR Latent Input Switch`、`SDPoseOODLoader`、`LayerUtility: ImageReel`、`SDPoseOODProcessor`、`easy imageSize`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
