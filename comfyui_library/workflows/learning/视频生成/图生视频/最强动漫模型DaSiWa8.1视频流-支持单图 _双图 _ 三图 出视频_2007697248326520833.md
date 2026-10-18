---
key: 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2007697248326520833.json
name: 最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2007697248326520833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2007697248326520833.json
hash: b79bef1e86aef011
coverage: 0.425926
learned_at: 2026-10-15 22:34:05
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Int, Note, RIFE VFI, VHS_VideoCombine, Reroute, CLIPTextEncode, ModelSamplingSD3, Note, TextInput_, Reroute, easy showAnything, JoinStrings, Fast Groups Bypasser (rgthree), CLIPTextEncode, ShowText|pysssss, ImageConcatMulti, WanFirstLastFrameToVideo, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Reroute, Reroute, Int, LayerUtility: ImageScaleByAspectRatio V2, GetImagesFromBatchIndexed, PathchSageAttentionKJ, Note, easy showAnything, JoinStrings, ShowText|pysssss, Reroute, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, PathchSageAttentionKJ, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, ModelPatchTorchSettings, Reroute, Reroute, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Reroute, INTConstant, Note, Note, Reroute, INTConstant, TextInput_, Reroute, Reroute, VHS_VideoCombine, Int, Note, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageBatchMulti, ImageConcatMulti, GetImagesFromBatchIndexed, PreviewImage, WanMultiFrameRefToVideo, Reroute, LoadImage, LoadImage, LoadImage, Reroute, LoadImage, Qwen3_VQA, LoadImage, Qwen3_VQA, CLIPLoader, CLIPLoader, Fast Groups Bypasser (rgthree), UNETLoader, UNETLoader, UNETLoader, UNETLoader, RIFE VFI, PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Int, Note, VHS_VideoCombine, PreviewImage, PreviewImage, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, TextInput_, Reroute, easy showAnything, JoinStrings, Note, Int, GetImagesFromBatchIndexed, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, Reroute, CLIPTextEncode, Fast Groups Bypasser (rgthree), Note, Note, ShowText|pysssss, UNETLoader, PainterI2V, UNETLoader, Qwen3_VQA, RIFE VFI, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2007697248326520833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007697248326520833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（216 个）：
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
- `ShowText|pysssss`
- `ImageConcatMulti`
- `WanFirstLastFrameToVideo`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Reroute`
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
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `WanMultiFrameRefToVideo`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `Qwen3_VQA`
- `LoadImage`
- `Qwen3_VQA`
- `CLIPLoader`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RIFE VFI`
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
- `Reroute`
- `VAELoader`
- `Note`
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
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Note`
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
- `Note`
- `Int`
- `GetImagesFromBatchIndexed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `PainterI2V`
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `RIFE VFI`
- `LoadImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **43%**（92/216）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Int`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPTextEncode`、`TextInput_`、`JoinStrings`、`ImageConcatMulti`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImagesFromBatchIndexed`、`ImageResizeKJv2`、`ImageBatchMulti`、`WanMultiFrameRefToVideo`、`LoadImage`、`Qwen3_VQA`、`CLIPLoader`、`UNETLoader`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
