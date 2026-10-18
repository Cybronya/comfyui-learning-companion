---
key: 视频生成/图生视频/Wan2.2_Remix（首尾帧)_2001276328982740993.json
name: Wan2.2_Remix（首尾帧)_2001276328982740993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_Remix（首尾帧)_2001276328982740993.json
hash: fcb767b2f5746963
coverage: 0.589286
learned_at: 2026-10-15 22:33:45
nodes: [ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, Note, SetNode, Note, Int, SetNode, GetNode, GetNode, GetNode, Int, GetNode, GetNode, GetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, WanFirstLastFrameToVideo, easy cleanGpuUsed, SetNode, SetNode, INTConstant, SetNode, INTConstant, SetNode, GetNode, GetNode, RIFE VFI, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, VAEDecode, GetNode, ModelSamplingSD3, SetNode, Note, Note, KSamplerAdvanced, UNETLoader, PreviewImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, KSamplerAdvanced, VHS_VideoCombine, ImageResizeKJv2, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_Remix（首尾帧)_2001276328982740993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001276328982740993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
- `Note`
- `SetNode`
- `Note`
- `Int`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `RIFE VFI`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `SetNode`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **59%**（33/56）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`Int`、`WanFirstLastFrameToVideo`、`easy cleanGpuUsed`、`INTConstant`、`RIFE VFI`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`KSamplerAdvanced`、`UNETLoader`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
