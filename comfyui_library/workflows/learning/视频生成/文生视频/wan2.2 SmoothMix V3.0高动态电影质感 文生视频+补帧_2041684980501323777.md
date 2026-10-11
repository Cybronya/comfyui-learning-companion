---
key: 视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json
name: wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json
hash: 3ff5de5327502ee9
coverage: 0.694444
learned_at: 2026-10-11 19:49:45
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), VHS_VideoCombine, UNETLoader, easy promptConcat, ImpactInt, ImpactInt, VHS_VideoCombine, UNETLoader, PrimitiveStringMultiline, Wan22PromptSelector, ImpactInt]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), RIFE VFI, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, Seed (rgthree), easy promptConcat]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
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
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `easy promptConcat`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`
- `ImpactInt`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（25/36）

**有卡**：`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ImageScaleBy`、`CLIPTextEncode`、`WanImageToVideo`、`KSamplerAdvanced`、`VHS_VideoCombine`、`UNETLoader`、`ImpactInt`、`Wan22PromptSelector`

**缺卡**（10）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Seed (rgthree)`、`easy promptConcat`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Wan22PromptSelector、ImageScaleBy

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
