---
key: 视频生成/图生视频/Dasiwa V9模型VS Wan2.2 Smooth V2模型图生视频对比_2011762813080965122.json
name: Dasiwa V9模型VS Wan2.2 Smooth V2模型图生视频对比_2011762813080965122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2011762813080965122.json
hash: 0ddd2a2236c242e7
coverage: 0.764706
learned_at: 2026-10-15 22:34:24
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, Note, WanImageToVideo, Note, Note, Note, ModelSamplingSD3, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, ModelSamplingSD3, PreviewImage, ColorMatch, VHS_VideoCombine, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, AILab_QwenVL, CR Prompt Text, easy showAnything, KSamplerAdvanced, KSamplerAdvanced, easy showAnything, LoraLoaderModelOnly, UNETLoader, AddLabel, VAELoader, CLIPLoader, CLIPVisionLoader, UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, ImageScaleBy, Note, CLIPTextEncode, StringConcatenate, Note, Pick From Batch (mtb), CLIPVisionEncode, ModelSamplingSD3, Note, CLIPVisionLoader, VAELoader, easy showAnything, VHS_VideoCombine, Note, CLIPTextEncode, KSamplerAdvanced, Seed (rgthree), Note, Note, PrimitiveStringMultiline, easy cleanGpuUsed, UNETLoader, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelPatchTorchSettings, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, WanImageToVideo, ImageResizeKJv2, Note, KSamplerAdvanced, Reroute, VHS_VideoCombine, SaveImage, ImageScaleBy, ColorMatch, RIFE VFI, easy cleanGpuUsed, PreviewImage, Seed (rgthree), RH_LLMAPI_NODE, JWInteger, UNETLoader, UNETLoader, UNETLoader, AddLabel, VAEDecode, LoadImage, VHS_VideoCombine, ImageConcanate, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Dasiwa V9模型VS Wan2.2 Smooth V2模型图生视频对比_2011762813080965122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011762813080965122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ImageScaleBy`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `Note`
- `WanImageToVideo`
- `Note`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `PreviewImage`
- `ColorMatch`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `AILab_QwenVL`
- `CR Prompt Text`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `AddLabel`
- `VAELoader`
- `CLIPLoader`
- `CLIPVisionLoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `Note`
- `Pick From Batch (mtb)`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `easy showAnything`
- `VHS_VideoCombine`
- `Note`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `Note`
- `Note`
- `PrimitiveStringMultiline`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `Note`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `SaveImage`
- `ImageScaleBy`
- `ColorMatch`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Seed (rgthree)`
- `RH_LLMAPI_NODE`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `AddLabel`
- `VAEDecode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `ImageConcanate`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（78/102）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM`、`ColorMatch`、`VHS_VideoCombine`、`VAEDecode`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_QwenVL`、`CR Prompt Text`、`KSamplerAdvanced`、`UNETLoader`、`AddLabel`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`StringConcatenate`、`Seed (rgthree)`、`ModelPatchTorchSettings`、`RIFE VFI`、`RH_LLMAPI_NODE`、`JWInteger`、`LoadImage`、`ImageConcanate`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
