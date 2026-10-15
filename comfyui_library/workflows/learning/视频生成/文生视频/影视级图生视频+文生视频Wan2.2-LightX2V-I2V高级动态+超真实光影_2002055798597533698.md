---
key: 视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json
name: 影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json
hash: 729ce1b9f8231236
coverage: 0.595745
learned_at: 2026-10-15 22:48:36
nodes: [ImpactInt, SimpleMath+, SetNode, SetNode, SetNode, CLIPLoader, UNETLoader, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, VAELoader, GetNode, VAEDecode, easy cleanGpuUsed, WanMoeKSampler, UNETLoader, ImpactInt, ImpactInt, wanBlockSwap, ModelPatchTorchSettings, WanImageToVideo, ModelPatchTorchSettings, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `ImpactInt`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `WanMoeKSampler` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `ImpactInt`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `WanImageToVideo`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **60%**（28/47）

**有卡**：`ImpactInt`、`SimpleMath+`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ImageResizeKJv2`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`WanMoeKSampler`、`wanBlockSwap`、`ModelPatchTorchSettings`、`WanImageToVideo`、`LoadImage`、`RIFE VFI`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
