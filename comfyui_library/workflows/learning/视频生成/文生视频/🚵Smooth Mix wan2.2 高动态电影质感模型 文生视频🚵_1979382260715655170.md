---
key: 视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json
name: 🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json
hash: ffe9f7ca7387e072
coverage: 0.666667
learned_at: 2026-10-10 23:14:53
nodes: [KSamplerAdvanced, wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, ImpactInt, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, WanImageToVideo, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, Note Plus (mtb), MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, UNETLoader]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Note Plus (mtb), RIFE VFI, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, Seed (rgthree)]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **67%**（24/36）

**有卡**：`KSamplerAdvanced`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`VAEDecode`、`WanImageToVideo`、`ImageScaleBy`、`CLIPTextEncode`、`VHS_VideoCombine`

**缺卡**（10）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Note Plus (mtb)`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、ImageScaleBy、ImpactInt

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
