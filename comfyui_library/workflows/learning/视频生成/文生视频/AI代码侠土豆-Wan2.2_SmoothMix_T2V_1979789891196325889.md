---
key: 视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json
name: AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json
hash: 235da0104f7e6da1
coverage: 0.742857
learned_at: 2026-10-11 02:44:59
nodes: [SetNode, SetNode, ImpactInt, SetNode, UnetLoaderGGUF, UnetLoaderGGUF, VAELoader, easy cleanGpuUsed, VAEDecode, Reroute, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, WanImageToVideo, GetNode, GetNode, GetNode, wanBlockSwap, wanBlockSwap, ImpactInt, ImpactInt, VHS_VideoCombine, CLIPLoader, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, UNETLoader, UnetLoaderGGUF, LoraLoaderModelOnly, WanMoeKSampler, SimpleMath+]
patterns: []
missing: [SimpleMath+, easy cleanGpuUsed]
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
- `SetNode`
- `SetNode`
- `ImpactInt`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Reroute`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `wanBlockSwap`
- `wanBlockSwap`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanMoeKSampler` ★核心
- `SimpleMath+`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **74%**（26/35）

**有卡**：`ImpactInt`、`UnetLoaderGGUF`、`VAELoader`、`VAEDecode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`WanImageToVideo`、`wanBlockSwap`、`VHS_VideoCombine`、`CLIPLoader`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`WanMoeKSampler`

**缺卡**（2）：`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、ImpactInt

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
