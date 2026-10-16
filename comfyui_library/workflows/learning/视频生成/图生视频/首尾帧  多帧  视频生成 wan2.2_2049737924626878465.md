---
key: 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2049737924626878465.json
name: 首尾帧  多帧  视频生成 wan2.2_2049737924626878465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2049737924626878465.json
hash: 3527b3c7ab3fd27d
coverage: 0.563218
learned_at: 2026-10-15 22:37:15
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, GetNode, SetNode, SetNode, CLIPVisionLoader, SetNode, GetNode, GetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, GetNode, GetNode, LoraLoaderModelOnly, easy cleanGpuUsed, SetNode, Text, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Text, Text Concatenate, SetNode, GetNode, SetNode, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, LoadImage, LoadImage, JoinImages, ImageResizeKJv2, JoinImages, ImageResizeKJv2, GetNode, GetNode, SetNode, LoadImage, INTConstant, UNETLoader, CompressImages, INTConstant, INTConstant, SetNode, VAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, easy showAnything, UNETLoader, SimpleMath+, CompressImages, GetNode, SetNode, CLIPLoader, CompressImages, GetNode, easy seed, Text, VideoCombineNode, INTConstant, VAEDecode, INTConstant, ImageResizeKJv2, VHS_VideoCombine, GetNode, KSamplerAdvanced, KSamplerAdvanced, WanFirstMiddleLastFrameToVideo, Qwen3_VQA, CLIPTextEncode, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "normal", "sampler_name": 0.5, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2049737924626878465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049737924626878465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（87 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `Text`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Text`
- `Text Concatenate`
- `SetNode`
- `GetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `JoinImages`
- `ImageResizeKJv2`
- `JoinImages`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `INTConstant`
- `UNETLoader` ★核心
- `CompressImages`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `SimpleMath+`
- `CompressImages`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `CompressImages`
- `GetNode`
- `easy seed`
- `Text`
- `VideoCombineNode`
- `INTConstant`
- `VAEDecode` ★核心
- `INTConstant`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `TextInput_`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `0.5`
- `scheduler` = `euler_ancestral`
- `denoise` = `normal`

## 知识

覆盖率 **56%**（49/87）

**有卡**：`CLIPVisionEncode`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`Text`、`Text Concatenate`、`ModelSamplingSD3`、`LoadImage`、`JoinImages`、`ImageResizeKJv2`、`INTConstant`、`UNETLoader`、`CompressImages`、`VAELoader`、`CLIPTextEncode`、`SimpleMath+`、`CLIPLoader`、`easy seed`、`VideoCombineNode`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerAdvanced`、`WanFirstMiddleLastFrameToVideo`、`Qwen3_VQA`、`TextInput_`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
