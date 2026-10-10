---
key: 视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json
name: 影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json
hash: 729ce1b9f8231236
coverage: 0.531915
learned_at: 2026-10-11 02:57:40
nodes: [ImpactInt, SimpleMath+, SetNode, SetNode, SetNode, CLIPLoader, UNETLoader, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, VAELoader, GetNode, VAEDecode, easy cleanGpuUsed, WanMoeKSampler, UNETLoader, ImpactInt, ImpactInt, wanBlockSwap, ModelPatchTorchSettings, WanImageToVideo, ModelPatchTorchSettings, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: [RIFE VFI, SimpleMath+, easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
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

覆盖率 **53%**（25/47）

**有卡**：`ImpactInt`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ImageResizeKJv2`、`VAELoader`、`VAEDecode`、`WanMoeKSampler`、`wanBlockSwap`、`ModelPatchTorchSettings`、`WanImageToVideo`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（3）：`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
