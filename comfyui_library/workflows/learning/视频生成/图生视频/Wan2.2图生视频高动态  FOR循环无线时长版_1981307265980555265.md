---
key: 视频生成/图生视频/Wan2.2图生视频高动态  FOR循环无线时长版_1981307265980555265.json
name: Wan2.2图生视频高动态  FOR循环无线时长版_1981307265980555265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频高动态  FOR循环无线时长版_1981307265980555265.json
hash: 93757fd0bc3fe6e0
coverage: 0.959184
learned_at: 2026-10-15 22:32:37
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, CLIPVisionLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, easy cleanGpuUsed, PrimitiveStringMultiline, Fast Bypasser (rgthree), SimpleMath+, easy cleanGpuUsed, VAEDecode, Text Load Line From File, WanMoeKSampler, GetImageSizeAndCount, VHS_VideoCombine, RIFE VFI, Mute / Bypass Repeater (rgthree), VHS_VideoCombine, Note Plus (mtb), MarkdownNote, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPVisionEncode, WanImageToVideo, ImageResizeKJv2, MathExpression|pysssss, ImageFromBatch, easy batchAnything, easy forLoopEnd, Seed (rgthree), easy forLoopStart, UNETLoader, UNETLoader, String Literal, LoadImage, ImpactInt, ImpactInt, ImpactInt, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 1, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2图生视频高动态  FOR循环无线时长版_1981307265980555265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981307265980555265.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `Fast Bypasser (rgthree)`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Text Load Line From File`
- `WanMoeKSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `RIFE VFI`
- `Mute / Bypass Repeater (rgthree)`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `MarkdownNote`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `easy batchAnything`
- `easy forLoopEnd`
- `Seed (rgthree)`
- `easy forLoopStart`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `String Literal`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`

## 关键参数

- `seed` = `1`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **96%**（47/49）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`easy cleanGpuUsed`、`Fast Bypasser (rgthree)`、`SimpleMath+`、`VAEDecode`、`Text Load Line From File`、`WanMoeKSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`RIFE VFI`、`Note Plus (mtb)`、`CLIPVisionEncode`、`WanImageToVideo`、`ImageResizeKJv2`、`MathExpression|pysssss`、`ImageFromBatch`、`easy batchAnything`、`easy forLoopEnd`、`Seed (rgthree)`、`easy forLoopStart`、`UNETLoader`、`String Literal`、`LoadImage`、`ImpactInt`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、Seed (rgthree)
