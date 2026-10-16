---
key: 视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+视频放大插帧-图生视频_1980235190960369666.json
name: Smooth Mix wan2.2 电影质画质-加速版+视频放大插帧-图生视频_1980235190960369666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980235190960369666.json
hash: 7c3c7d807f001b71
coverage: 0.867925
learned_at: 2026-10-15 22:32:29
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, easy cleanGpuUsed, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, UNETLoader, CLIPTextEncode, easy seed, CLIPTextEncode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), PrimitiveBoolean, easy ifElse, LoadImage, TextBox, Int, Int, ImageResizeKJv2, MarkdownNote, CR Text Replace, easy showAnything, easy showAnything, RH_Captioner, LayerUtility: PurgeVRAM, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, LoadImage, GetNode, CR Upscale Image, RIFE VFI, easy cleanGpuUsed, VAEDecode, SetNode, ImageResizeKJv2, VHS_VideoCombine, Int, SimpleMath+, VHS_VideoCombine, ImageConcatMulti, TextBox, JjkText]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+视频放大插帧-图生视频_1980235190960369666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980235190960369666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（53 个）：
- `wanBlockSwap`
- `wanBlockSwap`
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
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `easy seed`
- `CLIPTextEncode` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `PrimitiveBoolean`
- `easy ifElse`
- `LoadImage`
- `TextBox`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `MarkdownNote`
- `CR Text Replace`
- `easy showAnything`
- `easy showAnything`
- `RH_Captioner`
- `LayerUtility: PurgeVRAM`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `GetNode`
- `CR Upscale Image`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `Int`
- `SimpleMath+`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `TextBox`
- `JjkText`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（46/53）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`CLIPTextEncode`、`easy seed`、`PrimitiveBoolean`、`LoadImage`、`TextBox`、`Int`、`ImageResizeKJv2`、`CR Text Replace`、`RH_Captioner`、`LayerUtility: PurgeVRAM`、`WanImageToVideo`、`KSamplerAdvanced`、`CR Upscale Image`、`RIFE VFI`、`VAEDecode`、`VHS_VideoCombine`、`SimpleMath+`、`ImageConcatMulti`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、easy seed
