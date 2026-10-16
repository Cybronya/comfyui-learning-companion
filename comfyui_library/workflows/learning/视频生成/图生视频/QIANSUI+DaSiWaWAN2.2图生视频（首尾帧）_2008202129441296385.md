---
key: 视频生成/图生视频/QIANSUI+DaSiWaWAN2.2图生视频（首尾帧）_2008202129441296385.json
name: QIANSUI+DaSiWaWAN2.2图生视频（首尾帧）_2008202129441296385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008202129441296385.json
hash: 9b4eaab44eca1428
coverage: 0.85
learned_at: 2026-10-15 22:34:06
nodes: [Int, LoraLoaderModelOnly, CLIPTextEncode, Qwen3_VQA, ImageConcatMulti, Int, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, WanFirstLastFrameToVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, JoinStrings, TextInput_, CLIPTextEncode, RIFE VFI, easy cleanGpuUsed, VAEDecode, CLIPLoader, ShowText|pysssss, easy showAnything, KSamplerAdvanced, KSamplerAdvanced, LoadImage, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, MarkdownNote, INTConstant, INTConstant, GetNode, SetNode, GetNode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/QIANSUI+DaSiWaWAN2.2图生视频（首尾帧）_2008202129441296385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008202129441296385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `Int`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `ImageConcatMulti`
- `Int`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JoinStrings`
- `TextInput_`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`Int`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Qwen3_VQA`、`ImageConcatMulti`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`JoinStrings`、`TextInput_`、`RIFE VFI`、`easy cleanGpuUsed`、`VAEDecode`、`CLIPLoader`、`KSamplerAdvanced`、`LoadImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`INTConstant`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
