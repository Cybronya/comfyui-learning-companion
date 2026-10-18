---
key: 视频生成/图生视频/[发布版]DaSiWa-WAN2.2场景首尾帧生视频_2033880906871611394.json
name: [发布版]DaSiWa-WAN2.2场景首尾帧生视频_2033880906871611394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/[发布版]DaSiWa-WAN2.2场景首尾帧生视频_2033880906871611394.json
hash: df6708ae542924dc
coverage: 0.755556
learned_at: 2026-10-15 22:35:42
nodes: [Reroute, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Note, ModelSamplingSD3, ModelSamplingSD3, VAELoader, Int, CLIPLoader, Int, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, PreviewImage, PreviewImage, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), ImageConcatMulti, LoadImage, VHS_VideoCombine, LoadImage, Note, Note, Note, Note, CLIPTextEncode, CLIPTextEncode, JoinStrings, Qwen3_VQA, easy showAnything, ShowText|pysssss, TextInput_, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/[发布版]DaSiWa-WAN2.2场景首尾帧生视频_2033880906871611394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033880906871611394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `Reroute`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `Int`
- `CLIPLoader`
- `Int`
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `Qwen3_VQA`
- `easy showAnything`
- `ShowText|pysssss`
- `TextInput_`
- `RIFE VFI`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`Int`、`CLIPLoader`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`、`VAEDecode`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`ImageConcatMulti`、`LoadImage`、`VHS_VideoCombine`、`CLIPTextEncode`、`JoinStrings`、`Qwen3_VQA`、`TextInput_`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
