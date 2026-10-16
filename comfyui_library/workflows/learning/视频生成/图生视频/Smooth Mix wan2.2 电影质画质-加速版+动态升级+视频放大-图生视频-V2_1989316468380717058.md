---
key: 视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json
name: Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1989316468380717058.json
hash: 8cebad4bdee214ac
coverage: 0.973684
learned_at: 2026-10-15 22:33:06
nodes: [ModelSamplingSD3, CLIPLoader, Seed (rgthree), CLIPVisionLoader, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), wanBlockSwap, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, VAEDecode, CLIPTextEncode, ImageResizeKJv2, CLIPTextEncode, SimpleMath+, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, MarkdownNote, WanMoeKSampler, UNETLoader, UNETLoader, VAELoader, PainterI2V, Fast Bypasser (rgthree), ImpactInt, LoadImage, ImpactInt, ImpactInt, CR Text, VHS_VideoCombine, RIFE VFI, easy cleanGpuUsed, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 1, "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989316468380717058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `Seed (rgthree)`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `MarkdownNote`
- `WanMoeKSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PainterI2V`
- `Fast Bypasser (rgthree)`
- `ImpactInt`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `CR Text`
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`Seed (rgthree)`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`wanBlockSwap`、`ModelPatchTorchSettings`、`VAEDecode`、`CLIPTextEncode`、`ImageResizeKJv2`、`SimpleMath+`、`ImageScaleBy`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`WanMoeKSampler`、`UNETLoader`、`VAELoader`、`PainterI2V`、`ImpactInt`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、Seed (rgthree)
