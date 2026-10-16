---
key: 视频生成/图生视频/单图版+最强动漫模型DaSiWa8.1视频流_2079761122793709569.json
name: 单图版+最强动漫模型DaSiWa8.1视频流_2079761122793709569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2079761122793709569.json
hash: 4daa67271edf942a
coverage: 0.446009
learned_at: 2026-10-15 22:42:06
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, Reroute, VAEDecode, Note, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Note, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, TextInput_, Reroute, easy showAnything, JoinStrings, Reroute, CLIPTextEncode, Note, PainterI2V, Fast Groups Bypasser (rgthree), PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Int, Note, Reroute, CLIPTextEncode, ModelSamplingSD3, Note, TextInput_, Reroute, easy showAnything, JoinStrings, Fast Groups Bypasser (rgthree), CLIPTextEncode, ShowText|pysssss, ImageConcatMulti, WanFirstLastFrameToVideo, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Int, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, Note, easy showAnything, JoinStrings, ShowText|pysssss, Reroute, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, PathchSageAttentionKJ, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, ModelPatchTorchSettings, Reroute, Reroute, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Reroute, INTConstant, Note, Note, Reroute, INTConstant, TextInput_, Reroute, Reroute, Int, Note, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageBatchMulti, ImageConcatMulti, WanMultiFrameRefToVideo, Reroute, LoadImage, LoadImage, LoadImage, Reroute, LoadImage, Qwen3_VQA, LoadImage, Qwen3_VQA, CLIPLoader, CLIPLoader, Fast Groups Bypasser (rgthree), UNETLoader, UNETLoader, UNETLoader, UNETLoader, ShowText|pysssss, SaveImage, TT_img_enc, TT_img_enc_v2, SaveImage, RIFE VFI, SaveImage, TT_img_enc_v2, SaveImage, TT_img_enc, RIFE VFI, UNETLoader, UNETLoader, CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), Note, Note, Qwen3_VQA, KSamplerAdvanced, KSamplerAdvanced, Reroute, Reroute, Int, INTConstant, INTConstant, Int, DuckHideNode, easy cleanGpuUsed, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/单图版+最强动漫模型DaSiWa8.1视频流_2079761122793709569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079761122793709569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（213 个）：
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
- `Note`
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
- `Reroute`
- `VAEDecode` ★核心
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `ModelSamplingSD3`
- `TextInput_`
- `Reroute`
- `easy showAnything`
- `JoinStrings`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Note`
- `PainterI2V`
- `Fast Groups Bypasser (rgthree)`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Int`
- `Note`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageBatchMulti`
- `ImageConcatMulti`
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
- `ShowText|pysssss`
- `SaveImage`
- `TT_img_enc`
- `TT_img_enc_v2`
- `SaveImage`
- `RIFE VFI`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `TT_img_enc`
- `RIFE VFI`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `Qwen3_VQA`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Int`
- `INTConstant`
- `INTConstant`
- `Int`
- `DuckHideNode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **45%**（95/213）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`TextInput_`、`JoinStrings`、`PainterI2V`、`VAELoader`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`INTConstant`、`Int`、`ImageConcatMulti`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`ImageBatchMulti`、`WanMultiFrameRefToVideo`、`LoadImage`、`Qwen3_VQA`、`CLIPLoader`、`UNETLoader`、`SaveImage`、`TT_img_enc`、`TT_img_enc_v2`、`RIFE VFI`、`DuckHideNode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
