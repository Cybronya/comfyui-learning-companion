---
key: 视频生成/图生视频/SmoothMix-V2.0首尾帧视频生成_2010689825397018625.json
name: SmoothMix-V2.0首尾帧视频生成_2010689825397018625.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010689825397018625.json
hash: af3de94a2168694a
coverage: 1
learned_at: 2026-10-15 22:34:18
nodes: [CLIPLoader, INTConstant, INTConstant, INTConstant, ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, UNETLoader, UNETLoader, VAEDecode, VHS_VideoCombine, VAELoader, ImageResizeKJv2, ImageResizeKJv2, SimpleMath+, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionEncode, LoadImage, LoadImage, CLIPVisionLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/SmoothMix-V2.0首尾帧视频生成_2010689825397018625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010689825397018625.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `CLIPLoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SimpleMath+`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`CLIPLoader`、`INTConstant`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`UNETLoader`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`ImageResizeKJv2`、`SimpleMath+`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`CLIPVisionEncode`、`LoadImage`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
