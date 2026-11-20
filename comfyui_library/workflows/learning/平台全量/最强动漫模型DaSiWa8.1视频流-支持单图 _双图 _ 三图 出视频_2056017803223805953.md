---
key: 平台全量/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2056017803223805953.json
name: 最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2056017803223805953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2056017803223805953.json
hash: afa0327a7a703826
coverage: 0.426606
learned_at: 2026-11-14 02:14:28
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Int, Note, RIFE VFI, VHS_VideoCombine, Reroute, CLIPTextEncode, ModelSamplingSD3, Note, TextInput_, Reroute, easy showAnything, JoinStrings, Fast Groups Bypasser (rgthree), CLIPTextEncode, ImageConcatMulti, WanFirstLastFrameToVideo, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Reroute, Reroute, Int, LayerUtility: ImageScaleByAspectRatio V2, GetImagesFromBatchIndexed, PathchSageAttentionKJ, Note, easy showAnything, JoinStrings, ShowText|pysssss, Reroute, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, PathchSageAttentionKJ, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, ModelPatchTorchSettings, Reroute, Reroute, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Reroute, INTConstant, Note, Reroute, INTConstant, TextInput_, Reroute, Reroute, VHS_VideoCombine, Int, Note, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageBatchMulti, ImageConcatMulti, GetImagesFromBatchIndexed, PreviewImage, WanMultiFrameRefToVideo, Reroute, LoadImage, LoadImage, LoadImage, Reroute, LoadImage, Qwen3_VQA, LoadImage, Qwen3_VQA, CLIPLoader, CLIPLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, RIFE VFI, PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Int, Note, VHS_VideoCombine, PreviewImage, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, TextInput_, Reroute, easy showAnything, JoinStrings, Int, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, Reroute, CLIPTextEncode, Note, ShowText|pysssss, UNETLoader, PainterI2V, UNETLoader, Qwen3_VQA, RIFE VFI, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree), Note, GetImagesFromBatchIndexed, ShowText|pysssss, Note, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PreviewImage, Float, Note]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2056017803223805953.json

> 来源文件 `comfyui_library/workflows/平台全量/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2056017803223805953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（218 个）：
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
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `ModelSamplingSD3`
- `TextInput_`
- `Reroute`
- `easy showAnything`
- `JoinStrings`
- `Int`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `Reroute`
- `CLIPTextEncode` ★核心
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
- `Note`
- `GetImagesFromBatchIndexed`
- `ShowText|pysssss`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `Float`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **43%**（93/218）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Int`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPTextEncode`、`TextInput_`、`JoinStrings`、`ImageConcatMulti`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImagesFromBatchIndexed`、`ImageResizeKJv2`、`ImageBatchMulti`、`WanMultiFrameRefToVideo`、`LoadImage`、`Qwen3_VQA`、`CLIPLoader`、`UNETLoader`、`PainterI2V`、`Float`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader、KSamplerAdvanced
