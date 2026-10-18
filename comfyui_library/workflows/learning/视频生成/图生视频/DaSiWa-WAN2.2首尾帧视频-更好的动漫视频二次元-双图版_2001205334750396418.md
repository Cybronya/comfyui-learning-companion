---
key: 视频生成/图生视频/DaSiWa-WAN2.2首尾帧视频-更好的动漫视频二次元-双图版_2001205334750396418.json
name: DaSiWa-WAN2.2首尾帧视频-更好的动漫视频二次元-双图版_2001205334750396418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/DaSiWa-WAN2.2首尾帧视频-更好的动漫视频二次元-双图版_2001205334750396418.json
hash: e643120df7bc6aa7
coverage: 0.711864
learned_at: 2026-10-15 22:33:44
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, LoraLoaderModelOnly, Note, INTConstant, Note, PreviewImage, ModelSamplingSD3, GetImagesFromBatchIndexed, LoraLoaderModelOnly, LoadImage, UNETLoader, Fast Groups Bypasser (rgthree), Note, UNETLoader, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, Reroute, Note, Reroute, Reroute, Reroute, easy showAnything, JoinStrings, ShowText|pysssss, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, Reroute, Int, VAELoader, INTConstant, Note, SimpleMath+, Int, easy convertAnything, Reroute, VHS_VideoCombine, WanFirstLastFrameToVideo, easy cleanGpuUsed, easy cleanGpuUsed, Qwen3_VQA, TextInput_, CR Text Replace, TextInput_, Note, Note, Int, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/DaSiWa-WAN2.2首尾帧视频-更好的动漫视频二次元-双图版_2001205334750396418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001205334750396418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `INTConstant`
- `Note`
- `PreviewImage`
- `ModelSamplingSD3`
- `GetImagesFromBatchIndexed`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `JoinStrings`
- `ShowText|pysssss`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Int`
- `VAELoader`
- `INTConstant`
- `Note`
- `SimpleMath+`
- `Int`
- `easy convertAnything`
- `Reroute`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Qwen3_VQA`
- `TextInput_`
- `CR Text Replace`
- `TextInput_`
- `Note`
- `Note`
- `Int`
- `TextInput_`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **71%**（42/59）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`INTConstant`、`ModelSamplingSD3`、`GetImagesFromBatchIndexed`、`LoadImage`、`UNETLoader`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`JoinStrings`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`CLIPTextEncode`、`Int`、`VAELoader`、`SimpleMath+`、`easy convertAnything`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`Qwen3_VQA`、`TextInput_`、`CR Text Replace`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
