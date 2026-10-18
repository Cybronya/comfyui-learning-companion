---
key: 视频生成/图生视频/wan2.2+SVI-PRO2.0循环长视频生成_2006663467071180801.json
name: wan2.2+SVI-PRO2.0循环长视频生成_2006663467071180801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2+SVI-PRO2.0循环长视频生成_2006663467071180801.json
hash: c8238e223b4f7de4
coverage: 0.556962
learned_at: 2026-10-15 22:34:02
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Note, ImageResizeKJv2, VAEEncode, INTConstant, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, SetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, INTConstant, INTConstant, CLIPTextEncode, GetNode, GetNode, ModelSamplingSD3, GetNode, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, GetNode, GetNode, CLIPTextEncode, VHS_VideoCombine, easy forLoopEnd, VAEEncode, WanVideoNAG, KSamplerAdvanced, KSamplerAdvanced, PreviewAny, easy forLoopStart, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, SetNode, SetNode, GetNode, UNETLoader, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy promptLine, CLIPTextEncode, CR Prompt Text, GetNode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2+SVI-PRO2.0循环长视频生成_2006663467071180801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006663467071180801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（79 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `VAEEncode` ★核心
- `WanVideoNAG`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewAny`
- `easy forLoopStart`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `SetNode`
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy promptLine`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `GetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **56%**（44/79）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ImageResizeKJv2`、`VAEEncode`、`INTConstant`、`WanImageToVideoSVIPro`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerAdvanced`、`CLIPTextEncode`、`ModelSamplingSD3`、`easy forLoopEnd`、`WanVideoNAG`、`easy forLoopStart`、`ImageBatchExtendWithOverlap`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`easy promptLine`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
