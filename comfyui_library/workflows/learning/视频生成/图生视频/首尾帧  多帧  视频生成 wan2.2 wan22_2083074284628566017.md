---
key: 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json
name: 首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json
hash: 37228eb92fe09e94
coverage: 0.870968
learned_at: 2026-10-16 01:17:15
nodes: [ModelPatchTorchSettings, VAELoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelPatchTorchSettings, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, INTConstant, INTConstant, SimpleMath+, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, UNETLoader, ImageResizeKJv2, VHS_VideoCombine, LoadImage, LoadImage, CLIPTextEncode, CLIPLoader, INTConstant, ModelSamplingSD3, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `ModelPatchTorchSettings`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`ModelPatchTorchSettings`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ImageResizeKJv2`、`INTConstant`、`SimpleMath+`、`CLIPTextEncode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`CLIPLoader`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
