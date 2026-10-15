---
key: 视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json
name: 🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json
hash: ffe9f7ca7387e072
coverage: 0.944444
learned_at: 2026-10-15 22:49:14
nodes: [KSamplerAdvanced, wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, ImpactInt, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, WanImageToVideo, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, Note Plus (mtb), MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`KSamplerAdvanced`、`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`WanImageToVideo`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`Note Plus (mtb)`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageScaleBy
