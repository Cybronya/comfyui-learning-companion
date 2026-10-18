---
key: 视频生成/图生视频/DaSiWa-WAN2.2图生视频-三图首中尾帧视频-动漫友好型_2001276134820114434.json
name: DaSiWa-WAN2.2图生视频-三图首中尾帧视频-动漫友好型_2001276134820114434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/DaSiWa-WAN2.2图生视频-三图首中尾帧视频-动漫友好型_2001276134820114434.json
hash: 53d76895592026e3
coverage: 0.644068
learned_at: 2026-10-15 22:33:45
nodes: [PathchSageAttentionKJ, Note, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, PreviewImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), ImageConcatMulti, WanMultiFrameRefToVideo, UNETLoader, LoraLoaderModelOnly, JoinStrings, easy showAnything, TextInput_, ShowText|pysssss, CLIPTextEncode, CLIPLoader, CLIPTextEncode, PathchSageAttentionKJ, UNETLoader, KSamplerAdvanced, Reroute, ImageResizeKJv2, ImageResizeKJv2, Note, Note, INTConstant, LoadImage, Reroute, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, Note, Note, PrimitiveInt, VAELoader, Reroute, MarkdownNote, Reroute, Qwen3_VQA, easy cleanGpuUsed, easy cleanGpuUsed, KSamplerAdvanced, PreviewImage, ImageBatchMulti, VHS_VideoCombine, GetImagesFromBatchIndexed, Int, SimpleMath+, VAEDecode, Int, easy showAnything, easy convertAnything]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/DaSiWa-WAN2.2图生视频-三图首中尾帧视频-动漫友好型_2001276134820114434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001276134820114434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `PathchSageAttentionKJ`
- `Note`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `WanMultiFrameRefToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `JoinStrings`
- `easy showAnything`
- `TextInput_`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `INTConstant`
- `LoadImage`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `Note`
- `Note`
- `PrimitiveInt`
- `VAELoader`
- `Reroute`
- `MarkdownNote`
- `Reroute`
- `Qwen3_VQA`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `GetImagesFromBatchIndexed`
- `Int`
- `SimpleMath+`
- `VAEDecode` ★核心
- `Int`
- `easy showAnything`
- `easy convertAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **64%**（38/59）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoadImage`、`LoraLoaderModelOnly`、`ImageConcatMulti`、`WanMultiFrameRefToVideo`、`UNETLoader`、`JoinStrings`、`TextInput_`、`CLIPTextEncode`、`CLIPLoader`、`KSamplerAdvanced`、`ImageResizeKJv2`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`Qwen3_VQA`、`easy cleanGpuUsed`、`ImageBatchMulti`、`VHS_VideoCombine`、`GetImagesFromBatchIndexed`、`Int`、`SimpleMath+`、`VAEDecode`、`easy convertAnything`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
