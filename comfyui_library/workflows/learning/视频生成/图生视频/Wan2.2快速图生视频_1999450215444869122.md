---
key: 视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json
name: Wan2.2快速图生视频_1999450215444869122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json
hash: fab31b46b745b346
coverage: 0.481481
learned_at: 2026-10-15 22:33:37
nodes: [GetNode, ModelSamplingSD3, GetNode, GetNode, GetNode, GetNode, WanVideoNAG, SetNode, SetNode, ModelSamplingSD3, GetNode, GetNode, SetNode, CFGZeroStar, SetNode, PathchSageAttentionKJ, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, UNETLoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, LoraLoaderModelOnly, GetNode, CLIPVisionEncode, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, VAELoader, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, LoadImage, PreviewImage, INTConstant, INTConstant, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999450215444869122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoNAG`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `SetNode`
- `CFGZeroStar`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `LoadImage`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **48%**（26/54）

**有卡**：`ModelSamplingSD3`、`WanVideoNAG`、`CFGZeroStar`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`VAEDecode`、`ImageResizeKJv2`、`VAELoader`、`KSamplerAdvanced`、`WanImageToVideo`、`LoadImage`、`INTConstant`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
