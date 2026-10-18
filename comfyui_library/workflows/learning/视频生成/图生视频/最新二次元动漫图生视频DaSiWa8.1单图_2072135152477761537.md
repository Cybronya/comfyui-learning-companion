---
key: 视频生成/图生视频/最新二次元动漫图生视频DaSiWa8.1单图_2072135152477761537.json
name: 最新二次元动漫图生视频DaSiWa8.1单图_2072135152477761537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新二次元动漫图生视频DaSiWa8.1单图_2072135152477761537.json
hash: 1bafc370913d1371
coverage: 0.794118
learned_at: 2026-10-15 22:40:51
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Note, Note, ModelSamplingSD3, VAEDecode, Note, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, Note, PreviewImage, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, Note, PainterI2V, INTConstant, RIFE VFI, CLIPTextEncode, Qwen3_VQA, ShowText|pysssss, SomethingToString, ProcessString, VHS_VideoCombine, CLIPLoader, VAELoader, UNETLoader, UNETLoader, PathchSageAttentionKJ, KSamplerAdvanced, INTConstant, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最新二次元动漫图生视频DaSiWa8.1单图_2072135152477761537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072135152477761537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `PreviewImage`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `PainterI2V`
- `INTConstant`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `ShowText|pysssss`
- `SomethingToString`
- `ProcessString`
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`VAEDecode`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`CLIPTextEncode`、`PainterI2V`、`RIFE VFI`、`Qwen3_VQA`、`SomethingToString`、`ProcessString`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、INTConstant
