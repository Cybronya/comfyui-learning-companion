---
key: 视频生成/图生视频/电影质感+动漫视频+单图版（DaSiWaV9 WAN2.single image）_2013251284761059330.json
name: 电影质感+动漫视频+单图版（DaSiWaV9 WAN2.single image）_2013251284761059330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013251284761059330.json
hash: c8bc1536aacdadbb
coverage: 0.916667
learned_at: 2026-10-15 22:34:30
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, KSamplerAdvanced, PathchSageAttentionKJ, PainterI2V, VAEDecode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, ModelPatchTorchSettings, LoadImage, Int, Int, SimpleMath+, ModelSamplingSD3, JoinStrings, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, RIFE VFI, JoinStrings, KSamplerAdvanced, INTConstant, INTConstant, CLIPTextEncode, CLIPTextEncode, Qwen3_VQA, easy showAnything, ShowText|pysssss, TextInput_, Int, TextInput_, VHS_VideoCombine, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/电影质感+动漫视频+单图版（DaSiWaV9 WAN2.single image）_2013251284761059330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013251284761059330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PainterI2V`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `LoadImage`
- `Int`
- `Int`
- `SimpleMath+`
- `ModelSamplingSD3`
- `JoinStrings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `JoinStrings`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `easy showAnything`
- `ShowText|pysssss`
- `TextInput_`
- `Int`
- `TextInput_`
- `VHS_VideoCombine`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`PainterI2V`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`Int`、`SimpleMath+`、`JoinStrings`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`RIFE VFI`、`INTConstant`、`CLIPTextEncode`、`Qwen3_VQA`、`TextInput_`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Int
