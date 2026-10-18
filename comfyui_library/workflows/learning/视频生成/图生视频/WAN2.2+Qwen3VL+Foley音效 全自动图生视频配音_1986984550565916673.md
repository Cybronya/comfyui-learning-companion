---
key: 视频生成/图生视频/WAN2.2+Qwen3VL+Foley音效 全自动图生视频配音_1986984550565916673.json
name: WAN2.2+Qwen3VL+Foley音效 全自动图生视频配音_1986984550565916673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2+Qwen3VL+Foley音效 全自动图生视频配音_1986984550565916673.json
hash: 3ac8436fa3a396f0
coverage: 0.5
learned_at: 2026-10-15 22:32:57
nodes: [SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy promptLine, SetNode, UNETLoader, wanBlockSwap, wanBlockSwap, GetNode, SetNode, UNETLoader, ImageResizeKJv2, GetNode, GetNode, SetNode, QZ_ResolutionPreset, WanImageToVideo, CLIPLoader, GetNode, SetNode, VAELoader, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, Qwen3_VQA, SetNode, GetNode, WanMoeKSampler, easy showAnything, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, HunyuanVideoFoley, LoadImage, CLIPTextEncode, VAEDecode, easy cleanGpuUsed, RIFE VFI, SetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2+Qwen3VL+Foley音效 全自动图生视频配音_1986984550565916673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986984550565916673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
- `SetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy promptLine`
- `SetNode`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `QZ_ResolutionPreset`
- `WanImageToVideo`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Qwen3_VQA`
- `SetNode`
- `GetNode`
- `WanMoeKSampler` ★核心
- `easy showAnything`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `HunyuanVideoFoley`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `SetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **50%**（27/54）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`easy cleanGpuUsed`、`easy promptLine`、`UNETLoader`、`wanBlockSwap`、`ImageResizeKJv2`、`QZ_ResolutionPreset`、`WanImageToVideo`、`CLIPLoader`、`VAELoader`、`Qwen3_VQA`、`WanMoeKSampler`、`CR Prompt Text`、`VHS_VideoCombine`、`HunyuanVideoFoley`、`LoadImage`、`VAEDecode`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CR Prompt Text
