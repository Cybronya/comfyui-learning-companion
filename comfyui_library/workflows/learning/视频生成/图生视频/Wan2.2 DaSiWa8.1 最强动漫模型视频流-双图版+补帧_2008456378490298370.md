---
key: 视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-双图版+补帧_2008456378490298370.json
name: Wan2.2 DaSiWa8.1 最强动漫模型视频流-双图版+补帧_2008456378490298370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-双图版+补帧_2008456378490298370.json
hash: 08501c6a054f1bdf
coverage: 0.857143
learned_at: 2026-10-15 22:34:07
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Int, Int, INTConstant, INTConstant, VHS_VideoCombine, Int, TextInput_, SimpleMath+, ImageConcatMulti, Qwen3_VQA, easy showAnything, JoinStrings, easy cleanGpuUsed, CLIPTextEncode, ShowText|pysssss, CLIPLoader, CLIPTextEncode, Note, Fast Groups Bypasser (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Note, WanFirstLastFrameToVideo, easy cleanGpuUsed, KSamplerAdvanced, KSamplerAdvanced, easy cleanGpuUsed, VAEDecode, easy convertAnything, RIFE VFI, GetImagesFromBatchIndexed, RHHiddenNodes, ModelSamplingSD3, ModelSamplingSD3, PreviewImage, LoadImage, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-双图版+补帧_2008456378490298370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008456378490298370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Int`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `Int`
- `TextInput_`
- `SimpleMath+`
- `ImageConcatMulti`
- `Qwen3_VQA`
- `easy showAnything`
- `JoinStrings`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Note`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy convertAnything`
- `RIFE VFI`
- `GetImagesFromBatchIndexed`
- `RHHiddenNodes`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`INTConstant`、`VHS_VideoCombine`、`TextInput_`、`SimpleMath+`、`ImageConcatMulti`、`Qwen3_VQA`、`JoinStrings`、`easy cleanGpuUsed`、`CLIPTextEncode`、`CLIPLoader`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`easy convertAnything`、`RIFE VFI`、`GetImagesFromBatchIndexed`、`RHHiddenNodes`、`ModelSamplingSD3`、`LoadImage`

**用到的条目**：VAEDecode、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、GetImagesFromBatchIndexed、ImageConcatMulti、Int
