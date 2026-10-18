---
key: 视频生成/图生视频/Wan2.2-Smooth+Mix+九宫格全自动分割-自动衔接视频_2054151645621178370.json
name: Wan2.2-Smooth+Mix+九宫格全自动分割-自动衔接视频_2054151645621178370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth+Mix+九宫格全自动分割-自动衔接视频_2054151645621178370.json
hash: 7d7b85bc8c82766d
coverage: 0.84058
learned_at: 2026-10-15 22:37:46
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, Seed (rgthree), SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), VAEDecode, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, Note, ImpactInt, ImpactInt, ImpactInt, PreviewImage, ImageBatchGet, PreviewImage, PreviewImage, PreviewImage, PreviewImage, ImageBatchGet, easy imageSplitGrid, PrimitiveStringMultiline, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, ImageBatchGet, PreviewImage, PreviewImage, PreviewImage, PreviewImage, easy anythingIndexSwitch, easy anythingIndexSwitch, easy batchAnything, easy forLoopStart, Fast Bypasser (rgthree), easy forLoopEnd, ImageBatchGet, CLIPTextEncode, JWInteger, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Smooth+Mix+九宫格全自动分割-自动衔接视频_2054151645621178370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054151645621178370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `Seed (rgthree)`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `Note`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `PreviewImage`
- `ImageBatchGet`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageBatchGet`
- `easy imageSplitGrid`
- `PrimitiveStringMultiline`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `ImageBatchGet`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `easy forLoopStart`
- `Fast Bypasser (rgthree)`
- `easy forLoopEnd`
- `ImageBatchGet`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（58/69）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`VAEDecode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`RIFE VFI`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`ImpactInt`、`ImageBatchGet`、`easy imageSplitGrid`、`easy anythingIndexSwitch`、`easy batchAnything`、`easy forLoopStart`、`easy forLoopEnd`、`JWInteger`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
