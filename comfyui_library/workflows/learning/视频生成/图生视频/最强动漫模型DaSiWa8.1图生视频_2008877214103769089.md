---
key: 视频生成/图生视频/最强动漫模型DaSiWa8.1图生视频_2008877214103769089.json
name: 最强动漫模型DaSiWa8.1图生视频_2008877214103769089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008877214103769089.json
hash: 2fa7957726b11b9a
coverage: 0.823529
learned_at: 2026-10-15 22:34:09
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, VAELoader, Note, Note, Note, CLIPLoader, UNETLoader, Int, Int, INTConstant, Note, INTConstant, LoraLoaderModelOnly, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, Note, UNETLoader, Qwen3_VQA, JoinStrings, CLIPTextEncode, CLIPTextEncode, easy showAnything, TextInput_, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, LoadImage, PainterI2V]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/最强动漫模型DaSiWa8.1图生视频_2008877214103769089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008877214103769089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Int`
- `Int`
- `INTConstant`
- `Note`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `TextInput_`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `LoadImage`
- `PainterI2V`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`Int`、`INTConstant`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3_VQA`、`JoinStrings`、`CLIPTextEncode`、`TextInput_`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`RIFE VFI`、`VHS_VideoCombine`、`LoadImage`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
