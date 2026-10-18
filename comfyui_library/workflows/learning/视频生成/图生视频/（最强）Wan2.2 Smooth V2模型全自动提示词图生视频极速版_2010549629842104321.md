---
key: 视频生成/图生视频/（最强）Wan2.2 Smooth V2模型全自动提示词图生视频极速版_2010549629842104321.json
name: （最强）Wan2.2 Smooth V2模型全自动提示词图生视频极速版_2010549629842104321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（最强）Wan2.2 Smooth V2模型全自动提示词图生视频极速版_2010549629842104321.json
hash: fa8db59d51373d2b
coverage: 0.754386
learned_at: 2026-10-15 22:34:17
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, ImageScaleBy, Note, CLIPTextEncode, StringConcatenate, Note, easy cleanGpuUsed, RIFE VFI, SaveImage, ColorMatch, ImageScaleBy, Pick From Batch (mtb), CLIPVisionEncode, ModelSamplingSD3, Note, CLIPVisionLoader, VAELoader, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, Note, CLIPTextEncode, KSamplerAdvanced, Seed (rgthree), Note, Note, PrimitiveStringMultiline, VAEDecode, easy cleanGpuUsed, UNETLoader, UNETLoader, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelPatchTorchSettings, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, WanImageToVideo, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, mxSlider2D, PreviewImage, JWInteger, JWInteger, Note, AILab_QwenVL, RH_LLMAPI_NODE, CR Prompt Text, Note, LoadImage, easy showAnything, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（最强）Wan2.2 Smooth V2模型全自动提示词图生视频极速版_2010549629842104321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010549629842104321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `Note`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `Pick From Batch (mtb)`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `Note`
- `Note`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `mxSlider2D`
- `PreviewImage`
- `JWInteger`
- `JWInteger`
- `Note`
- `AILab_QwenVL`
- `RH_LLMAPI_NODE`
- `CR Prompt Text`
- `Note`
- `LoadImage`
- `easy showAnything`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（43/57）

**有卡**：`UnetLoaderGGUF`、`ImageScaleBy`、`CLIPTextEncode`、`StringConcatenate`、`easy cleanGpuUsed`、`RIFE VFI`、`SaveImage`、`ColorMatch`、`Pick From Batch (mtb)`、`CLIPVisionEncode`、`ModelSamplingSD3`、`CLIPVisionLoader`、`VAELoader`、`VHS_VideoCombine`、`KSamplerAdvanced`、`Seed (rgthree)`、`VAEDecode`、`UNETLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`CLIPLoader`、`WanImageToVideo`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`mxSlider2D`、`JWInteger`、`AILab_QwenVL`、`RH_LLMAPI_NODE`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
