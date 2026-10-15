---
key: 视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json
name: Wan2.2_Smooth Mix 文生视频_2049482366405582849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json
hash: 110272c8ca713220
coverage: 0.428571
learned_at: 2026-10-15 22:47:13
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Note, Note, Note, Reroute, ModelPatchTorchSettings, Reroute, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Fast Groups Bypasser (rgthree), Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Note, Int, VAEDecode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, easy cleanGpuUsed, WanMoeKSampler, wanBlockSwap, wanBlockSwap, Note, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, INTConstant, Int, Int, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
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

覆盖率 **43%**（21/49）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanImageToVideo`、`Int`、`VAEDecode`、`easy cleanGpuUsed`、`WanMoeKSampler`、`wanBlockSwap`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`INTConstant`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、Int、INTConstant
