---
key: 视频生成/图生视频/Wan2.2 Remix V3 图生视频工作流_极度丝滑模型_2070104941456351234.json
name: Wan2.2 Remix V3 图生视频工作流_极度丝滑模型_2070104941456351234.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070104941456351234.json
hash: 55406fe4c71aa31c
coverage: 1
learned_at: 2026-10-15 22:40:35
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, easy cleanGpuUsed, PathchSageAttentionKJ, ImageScaleBy, VAEDecode, WanImageToVideo, CLIPTextEncode, Text Concatenate, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, RIFE VFI, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, SimpleMath+, CR Text, INTConstant, Wan22PromptSelector, LoadImage, VHS_VideoCombine, VHS_VideoCombine, ModelPatchTorchSettings]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix V3 图生视频工作流_极度丝滑模型_2070104941456351234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070104941456351234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `RIFE VFI`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `SimpleMath+`
- `CR Text`
- `INTConstant`
- `Wan22PromptSelector`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ModelPatchTorchSettings`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`ImageScaleBy`、`VAEDecode`、`WanImageToVideo`、`CLIPTextEncode`、`Text Concatenate`、`CLIPVisionEncode`、`CLIPVisionLoader`、`RIFE VFI`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`SimpleMath+`、`CR Text`、`Wan22PromptSelector`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
