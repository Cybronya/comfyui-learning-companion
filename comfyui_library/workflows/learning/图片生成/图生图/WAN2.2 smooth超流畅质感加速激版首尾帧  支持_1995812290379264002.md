---
key: 图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json
name: WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json
hash: ef29b9cbfd0075aa
coverage: 0.689655
learned_at: 2026-10-23 11:27:27
nodes: [RIFE VFI, GetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, easy cleanGpuUsed, easy clearCacheAll, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, SetNode, Reroute, Reroute, Reroute, GetNode, GetNode, SetNode, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, INTConstant, INTConstant, SetNode, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, GetNode, PreviewImage, WanFirstLastFrameToVideo, INTConstant, CLIPLoader, VAELoader, Note, LoadImage, LoadImage, wanBlockSwap, SetNode, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VAEDecode, VHS_VideoCombine, CLIPVisionLoader, UNETLoader, UNETLoader, CLIPTextEncode, MarkdownNote, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `RIFE VFI`
- `GetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `GetNode`
- `PreviewImage`
- `WanFirstLastFrameToVideo`
- `INTConstant`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `LoadImage`
- `LoadImage`
- `wanBlockSwap`
- `SetNode`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（40/58）

**有卡**：`RIFE VFI`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`easy clearCacheAll`、`CLIPTextEncode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`ModelSamplingSD3`、`INTConstant`、`ImageResizeKJv2`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`CLIPLoader`、`VAELoader`、`LoadImage`、`wanBlockSwap`、`LoraLoaderModelOnly`、`ImageConcatMulti`、`VAEDecode`、`CLIPVisionLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
