---
key: 视频生成/图生视频/WAN2.2 DaSiWaV9  最强动漫短视频生成-提示词优化版_2073282904012181505.json
name: WAN2.2 DaSiWaV9  最强动漫短视频生成-提示词优化版_2073282904012181505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073282904012181505.json
hash: 46732a01b0a55bf1
coverage: 0.893805
learned_at: 2026-10-15 22:41:02
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, VAEDecode, Reroute, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, CLIPLoader, UNETLoader, VAELoader, KSamplerAdvanced, UNETLoader, UNETLoader, CLIPLoader, VAELoader, ModelSamplingSD3, Qwen3_VQA, ImageConcatMulti, easy showAnything, JoinStrings, ShowText|pysssss, CLIPTextEncode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanFirstLastFrameToVideo, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, SimpleMath+, Int, INTConstant, INTConstant, Int, VHS_VideoCombine, RIFE VFI, LoadImage, LoadImage, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ImageBatchMulti, ImageConcatMulti, CLIPLoader, VAELoader, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, TextInput_, JoinStrings, TextInput_, TextInput_, TextInput_, Qwen3_VQA, easy showAnything, JoinStrings, JoinStrings, ShowText|pysssss, LoadImage, LoadImage, LoadImage, WanMultiFrameRefToVideo, UNETLoader, UNETLoader, Int, INTConstant, INTConstant, ImageResizeKJv2, Int, PrimitiveInt, Int, SimpleMath+, RIFE VFI, KSamplerAdvanced, VHS_VideoCombine, Fast Groups Muter (rgthree), KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, RIFE VFI, Note, PainterI2V, LayerUtility: ImageScaleByAspectRatio V2, Int, Qwen3_VQA, INTConstant, JoinStrings, TextInput_, Int, JoinStrings, ShowText|pysssss, CLIPTextEncode, CLIPTextEncode, easy showAnything, SimpleMath+, VHS_VideoCombine, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, UNETLoader, LoadImage, Int, INTConstant, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2 DaSiWaV9  最强动漫短视频生成-提示词优化版_2073282904012181505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073282904012181505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `Qwen3_VQA`
- `ImageConcatMulti`
- `easy showAnything`
- `JoinStrings`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `Int`
- `INTConstant`
- `INTConstant`
- `Int`
- `VHS_VideoCombine`
- `RIFE VFI`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `TextInput_`
- `JoinStrings`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `Qwen3_VQA`
- `easy showAnything`
- `JoinStrings`
- `JoinStrings`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanMultiFrameRefToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Int`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `PrimitiveInt`
- `Int`
- `SimpleMath+`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `Note`
- `PainterI2V`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Qwen3_VQA`
- `INTConstant`
- `JoinStrings`
- `TextInput_`
- `Int`
- `JoinStrings`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `SimpleMath+`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoadImage`
- `Int`
- `INTConstant`
- `TextInput_`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（101/113）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSamplerAdvanced`、`Qwen3_VQA`、`ImageConcatMulti`、`JoinStrings`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`、`SimpleMath+`、`Int`、`INTConstant`、`VHS_VideoCombine`、`RIFE VFI`、`LoadImage`、`ImageResizeKJv2`、`ImageBatchMulti`、`TextInput_`、`WanMultiFrameRefToVideo`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
