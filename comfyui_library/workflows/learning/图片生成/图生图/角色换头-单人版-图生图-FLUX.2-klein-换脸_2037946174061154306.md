---
key: 图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306.json
name: 角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306.json
hash: a1010a98e45b35f7
coverage: 0.975
learned_at: 2026-10-23 13:27:10
nodes: [RandomNoise, Flux2Scheduler, CFGGuider, ConditioningZeroOut, PathchSageAttentionKJ, Image Comparer (rgthree), LoadImage, ReferenceLatent, ModelPatchTorchSettings, VAEDecode, ReferenceLatent, ReferenceLatent, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, GetImageSize, VAEEncode, LayerUtility: CropByMask V2, easy int, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, TT_img_enc_v2, Int, TwoWaySwitch, SaveImage, VAELoader, EmptyFlux2LatentImage, KSamplerSelect, SeedVR2, SeedVR2BlockSwap, CLIPLoader, CLIPTextEncode, CR Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `RandomNoise`
- `Flux2Scheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ReferenceLatent`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSize`
- `VAEEncode` ★核心
- `LayerUtility: CropByMask V2`
- `easy int`
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `TT_img_enc_v2`
- `Int`
- `TwoWaySwitch`
- `SaveImage`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `SeedVR2`
- `SeedVR2BlockSwap`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CR Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **98%**（39/40）

**有卡**：`RandomNoise`、`Flux2Scheduler`、`CFGGuider`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`LoadImage`、`ReferenceLatent`、`ModelPatchTorchSettings`、`VAEDecode`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`GetImageSize`、`LayerUtility: CropByMask V2`、`easy int`、`ClothesSegment`、`TT_img_enc_v2`、`Int`、`TwoWaySwitch`、`SaveImage`、`VAELoader`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`SeedVR2`、`SeedVR2BlockSwap`、`CLIPLoader`、`CLIPTextEncode`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
