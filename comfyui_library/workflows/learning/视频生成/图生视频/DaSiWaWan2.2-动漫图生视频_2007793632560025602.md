---
key: 视频生成/图生视频/DaSiWaWan2.2-动漫图生视频_2007793632560025602.json
name: DaSiWaWan2.2-动漫图生视频_2007793632560025602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007793632560025602.json
hash: 520e50179df1841c
coverage: 1
learned_at: 2026-10-15 22:34:05
nodes: [INTConstant, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, VAELoader, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, INTConstant, INTConstant, SimpleMath+, UNETLoader, UNETLoader, LoadImage, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, PainterI2V_Wan2_2, KSamplerAdvanced, KSamplerAdvanced, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/DaSiWaWan2.2-动漫图生视频_2007793632560025602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007793632560025602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `INTConstant`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `PainterI2V_Wan2_2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`INTConstant`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SimpleMath+`、`UNETLoader`、`LoadImage`、`VHS_VideoCombine`、`CLIPTextEncode`、`ImageResizeKJv2`、`PainterI2V_Wan2_2`、`KSamplerAdvanced`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
