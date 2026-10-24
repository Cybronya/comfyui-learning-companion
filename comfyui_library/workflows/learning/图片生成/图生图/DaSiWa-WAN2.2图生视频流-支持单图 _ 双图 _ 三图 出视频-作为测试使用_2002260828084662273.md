---
key: 图片生成/图生图/DaSiWa-WAN2.2图生视频流-支持单图 _ 双图 _ 三图 出视频-作为测试使用_2002260828084662273.json
name: DaSiWa-WAN2.2图生视频流-支持单图 _ 双图 _ 三图 出视频-作为测试使用_2002260828084662273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/DaSiWa-WAN2.2图生视频流-支持单图 _ 双图 _ 三图 出视频-作为测试使用_2002260828084662273.json
hash: 32e106fc609b7d99
coverage: 0.453744
learned_at: 2026-10-23 10:52:14
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, LoraLoaderModelOnly, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Int, Note, RIFE VFI, VHS_VideoCombine, PreviewImage, PreviewImage, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, TextInput_, Reroute, easy showAnything, JoinStrings, PainterI2V, Note, Int, GetImagesFromBatchIndexed, PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Int, Note, RIFE VFI, VHS_VideoCombine, PreviewImage, Reroute, CLIPTextEncode, ModelSamplingSD3, Note, TextInput_, Reroute, easy showAnything, JoinStrings, Fast Groups Bypasser (rgthree), CLIPTextEncode, ImageConcatMulti, WanFirstLastFrameToVideo, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Reroute, Int, LayerUtility: ImageScaleByAspectRatio V2, GetImagesFromBatchIndexed, PathchSageAttentionKJ, Note, easy showAnything, JoinStrings, ShowText|pysssss, Reroute, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, PathchSageAttentionKJ, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, ModelPatchTorchSettings, Reroute, Reroute, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Reroute, INTConstant, Note, Note, Reroute, INTConstant, TextInput_, Reroute, Reroute, VHS_VideoCombine, Int, Note, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageBatchMulti, ImageConcatMulti, RIFE VFI, GetImagesFromBatchIndexed, PreviewImage, WanMultiFrameRefToVideo, Reroute, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, LoadImage, CLIPLoader, Reroute, CLIPTextEncode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Note, Reroute, Qwen3_VQA, Note, Qwen3_VQA, Qwen3_VQA, ShowText|pysssss, UNETLoader, CLIPLoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), UNETLoader, UNETLoader, UNETLoader, UNETLoader, LoadImage, Reroute, Reroute, Fast Groups Bypasser (rgthree), ShowText|pysssss, LoadImage, LoadImageFromUrl, Reroute, LoadImage, LoadImageFromUrl]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/DaSiWa-WAN2.2图生视频流-支持单图 _ 双图 _ 三图 出视频-作为测试使用_2002260828084662273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/DaSiWa-WAN2.2图生视频流-支持单图 _ 双图 _ 三图 出视频-作为测试使用_2002260828084662273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（227 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Note`
- `RIFE VFI`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `ModelSamplingSD3`
- `TextInput_`
- `Reroute`
- `easy showAnything`
- `JoinStrings`
- `PainterI2V`
- `Note`
- `Int`
- `GetImagesFromBatchIndexed`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Note`
- `RIFE VFI`
- `VHS_VideoCombine`
- `PreviewImage`
- `Reroute`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `Note`
- `TextInput_`
- `Reroute`
- `easy showAnything`
- `JoinStrings`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageConcatMulti`
- `WanFirstLastFrameToVideo`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Reroute`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImagesFromBatchIndexed`
- `PathchSageAttentionKJ`
- `Note`
- `easy showAnything`
- `JoinStrings`
- `ShowText|pysssss`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `Note`
- `Note`
- `Reroute`
- `INTConstant`
- `TextInput_`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `Int`
- `Note`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `RIFE VFI`
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `WanMultiFrameRefToVideo`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `Reroute`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Reroute`
- `Qwen3_VQA`
- `Note`
- `Qwen3_VQA`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `Reroute`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImageFromUrl`
- `Reroute`
- `LoadImage`
- `LoadImageFromUrl`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **45%**（103/227）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VAEDecode`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPTextEncode`、`TextInput_`、`JoinStrings`、`PainterI2V`、`GetImagesFromBatchIndexed`、`KSamplerAdvanced`、`ImageConcatMulti`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`ImageBatchMulti`、`WanMultiFrameRefToVideo`、`LoadImage`、`CLIPLoader`、`Qwen3_VQA`、`UNETLoader`、`LoadImageFromUrl`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
