---
key: 视频生成/图生视频/Wan 2.2-SM无限时循环-高清动态图转视频_1987894798759735297.json
name: Wan 2.2-SM无限时循环-高清动态图转视频_1987894798759735297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2-SM无限时循环-高清动态图转视频_1987894798759735297.json
hash: e45420fd6a4474f4
coverage: 0.959184
learned_at: 2026-10-15 22:33:00
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, CLIPVisionLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, easy cleanGpuUsed, PrimitiveStringMultiline, Fast Bypasser (rgthree), SimpleMath+, easy cleanGpuUsed, VAEDecode, Text Load Line From File, WanMoeKSampler, GetImageSizeAndCount, RIFE VFI, Mute / Bypass Repeater (rgthree), VHS_VideoCombine, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPVisionEncode, WanImageToVideo, ImageResizeKJv2, MathExpression|pysssss, ImageFromBatch, easy batchAnything, easy forLoopEnd, Seed (rgthree), easy forLoopStart, UNETLoader, ImpactInt, ImpactInt, ImpactInt, ImpactInt, String Literal, LoadImage, UNETLoader, VHS_VideoCombine, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 1, "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2-SM无限时循环-高清动态图转视频_1987894798759735297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987894798759735297.json`

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
- `RIFE VFI`
- `Mute / Bypass Repeater (rgthree)`
- `VHS_VideoCombine`
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
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `String Literal`
- `LoadImage`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `1`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **96%**（47/49）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`easy cleanGpuUsed`、`Fast Bypasser (rgthree)`、`SimpleMath+`、`VAEDecode`、`Text Load Line From File`、`WanMoeKSampler`、`GetImageSizeAndCount`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPVisionEncode`、`WanImageToVideo`、`ImageResizeKJv2`、`MathExpression|pysssss`、`ImageFromBatch`、`easy batchAnything`、`easy forLoopEnd`、`Seed (rgthree)`、`easy forLoopStart`、`UNETLoader`、`ImpactInt`、`String Literal`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、Seed (rgthree)
