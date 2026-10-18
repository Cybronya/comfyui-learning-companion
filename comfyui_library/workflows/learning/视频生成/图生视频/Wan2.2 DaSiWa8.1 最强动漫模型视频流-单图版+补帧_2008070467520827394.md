---
key: 视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-单图版+补帧_2008070467520827394.json
name: Wan2.2 DaSiWa8.1 最强动漫模型视频流-单图版+补帧_2008070467520827394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-单图版+补帧_2008070467520827394.json
hash: b80ee86ebfc6926e
coverage: 0.815789
learned_at: 2026-10-15 22:34:06
nodes: [Note, PainterI2V, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, easy convertAnything, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, TextInput_, LoadImage, Int, Int, INTConstant, INTConstant, SimpleMath+, Int, MarkdownNote, Fast Groups Bypasser (rgthree), Note, VAEDecode, easy cleanGpuUsed, RHHiddenNodes, ModelSamplingSD3, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, GetImagesFromBatchIndexed, PreviewImage, Qwen3_VQA, easy showAnything, easy showAnything, JoinStrings, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-单图版+补帧_2008070467520827394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008070467520827394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `Note`
- `PainterI2V`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `easy convertAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `TextInput_`
- `LoadImage`
- `Int`
- `Int`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `Int`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RHHiddenNodes`
- `ModelSamplingSD3`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `Qwen3_VQA`
- `easy showAnything`
- `easy showAnything`
- `JoinStrings`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`PainterI2V`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`easy convertAnything`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`TextInput_`、`LoadImage`、`Int`、`INTConstant`、`SimpleMath+`、`VAEDecode`、`easy cleanGpuUsed`、`RHHiddenNodes`、`RIFE VFI`、`KSamplerAdvanced`、`GetImagesFromBatchIndexed`、`Qwen3_VQA`、`JoinStrings`、`CLIPLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、GetImagesFromBatchIndexed、Int、INTConstant
