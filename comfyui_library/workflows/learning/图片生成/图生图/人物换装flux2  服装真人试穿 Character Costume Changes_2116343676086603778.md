---
key: 图片生成/图生图/人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778.json
name: 人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778.json
hash: f41f7e92fa0c7704
coverage: 0.843137
learned_at: 2026-11-02 19:13:51
nodes: [KSamplerSelect, Flux2Scheduler, ReferenceLatent, SamplerCustomAdvanced, easy showAnything, SeedVR2LoadDiTModel, easy cleanGpuUsed, SeedVR2LoadVAEModel, CLIPLoader, VAEEncode, SamplerCustomAdvanced, BasicScheduler, VAEDecode, RandomNoise, EmptyLatentImage, SamplerEulerAncestral, GroundingDinoModelLoader_SDPose, SDPoseOODProcessor, easy cleanGpuUsed, PreviewImage, ReferenceLatent, BasicGuider, VAEEncode, easy sleep, FluxKontextImageScale, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SDPoseOODLoader, UNETLoader, VAEEncode, easy imageSize, LoadImage, FluxKontextImageScale, CLIPTextEncode, LoadImage, Note, Note, SaveImage, Note, VAEEncode, ClothesSegment, PreviewImage, FluxKontextImageScale, ClothesSegment, PreviewImage, ImageScaleBy, VAEDecode, PreviewImage, SeedVR2VideoUpscaler, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 图片生成/图生图/人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `easy showAnything`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `SeedVR2LoadVAEModel`
- `CLIPLoader`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `SamplerEulerAncestral` ★核心
- `GroundingDinoModelLoader_SDPose`
- `SDPoseOODProcessor`
- `easy cleanGpuUsed`
- `PreviewImage`
- `ReferenceLatent`
- `BasicGuider`
- `VAEEncode` ★核心
- `easy sleep`
- `FluxKontextImageScale`
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `SDPoseOODLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `easy imageSize`
- `LoadImage`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Note`
- `Note`
- `SaveImage`
- `Note`
- `VAEEncode` ★核心
- `ClothesSegment`
- `PreviewImage`
- `FluxKontextImageScale`
- `ClothesSegment`
- `PreviewImage`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `RandomNoise`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`ReferenceLatent`、`SamplerCustomAdvanced`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`CLIPLoader`、`VAEEncode`、`BasicScheduler`、`VAEDecode`、`RandomNoise`、`EmptyLatentImage`、`SamplerEulerAncestral`、`GroundingDinoModelLoader_SDPose`、`SDPoseOODProcessor`、`BasicGuider`、`easy sleep`、`FluxKontextImageScale`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`SDPoseOODLoader`、`UNETLoader`、`easy imageSize`、`LoadImage`、`CLIPTextEncode`、`SaveImage`、`ClothesSegment`、`ImageScaleBy`、`SeedVR2VideoUpscaler`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、KSamplerSelect
