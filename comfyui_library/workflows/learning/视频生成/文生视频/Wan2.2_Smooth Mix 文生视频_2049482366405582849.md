---
key: 视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json
name: Wan2.2_Smooth Mix 文生视频_2049482366405582849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json
hash: 110272c8ca713220
coverage: 0.408163
learned_at: 2026-10-11 19:49:43
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Note, Note, Note, Reroute, ModelPatchTorchSettings, Reroute, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Fast Groups Bypasser (rgthree), Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Note, Int, VAEDecode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, easy cleanGpuUsed, WanMoeKSampler, wanBlockSwap, wanBlockSwap, Note, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, INTConstant, Int, Int, VHS_VideoCombine]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（49 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Int`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `WanMoeKSampler` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `Int`
- `Int`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **41%**（20/49）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanImageToVideo`、`Int`、`VAEDecode`、`WanMoeKSampler`、`wanBlockSwap`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`INTConstant`、`VHS_VideoCombine`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、Int、INTConstant

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
