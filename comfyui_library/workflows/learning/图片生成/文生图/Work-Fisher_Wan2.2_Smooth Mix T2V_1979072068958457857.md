---
key: 图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json
name: Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json
hash: 8d19c074c2e1745c
coverage: 0.461538
learned_at: 2026-10-15 22:27:37
nodes: [RIFE VFI, PathchSageAttentionKJ, PathchSageAttentionKJ, Int, Reroute, Reroute, Note, Note, Note, Reroute, ModelPatchTorchSettings, Reroute, ModelPatchTorchSettings, Reroute, Reroute, CLIPTextEncode, Reroute, Fast Groups Bypasser (rgthree), Note, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, UNETLoader, WanMoeKSampler, LoraLoaderModelOnly, wanBlockSwap, wanBlockSwap, Note, Int, Int, INTConstant, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPLoader, Reroute, easy cleanGpuUsed, CLIPTextEncode, UnetLoaderGGUF]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（52 个）：
- `RIFE VFI`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Int`
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
- `CLIPTextEncode` ★核心
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `WanMoeKSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Note`
- `Int`
- `Int`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Reroute`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **46%**（24/52）

**有卡**：`RIFE VFI`、`PathchSageAttentionKJ`、`Int`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`WanImageToVideo`、`UNETLoader`、`WanMoeKSampler`、`LoraLoaderModelOnly`、`wanBlockSwap`、`INTConstant`、`VHS_VideoCombine`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`easy cleanGpuUsed`、`UnetLoaderGGUF`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、Int
