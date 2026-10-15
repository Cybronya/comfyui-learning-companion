---
key: 图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json
name: Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json
hash: 8d19c074c2e1745c
coverage: 0.423077
learned_at: 2026-10-10 20:59:15
nodes: [RIFE VFI, PathchSageAttentionKJ, PathchSageAttentionKJ, Int, Reroute, Reroute, Note, Note, Note, Reroute, ModelPatchTorchSettings, Reroute, ModelPatchTorchSettings, Reroute, Reroute, CLIPTextEncode, Reroute, Fast Groups Bypasser (rgthree), Note, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, UNETLoader, WanMoeKSampler, LoraLoaderModelOnly, wanBlockSwap, wanBlockSwap, Note, Int, Int, INTConstant, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPLoader, Reroute, easy cleanGpuUsed, CLIPTextEncode, UnetLoaderGGUF]
patterns: []
missing: [RIFE VFI, easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json`

## 结构

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
- `CLIPTextEncode`
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
- `UNETLoader`
- `WanMoeKSampler`
- `LoraLoaderModelOnly`
- `wanBlockSwap`
- `wanBlockSwap`
- `Note`
- `Int`
- `Int`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode`
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
- `CLIPTextEncode`
- `UnetLoaderGGUF`

## 关键参数

- `cfg` = `6`
- `denoise` = `euler_ancestral`
- `sampler_name` = `1`
- `scheduler` = `1`
- `seed` = `0.9`
- `steps` = `fixed`

## 知识

覆盖率 **42%**（22/52）

**有卡**：`RIFE VFI`、`PathchSageAttentionKJ`、`Int`、`Reroute`、`Note`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`Fast Groups Bypasser (rgthree)`

**缺卡**（2）：`RIFE VFI`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
