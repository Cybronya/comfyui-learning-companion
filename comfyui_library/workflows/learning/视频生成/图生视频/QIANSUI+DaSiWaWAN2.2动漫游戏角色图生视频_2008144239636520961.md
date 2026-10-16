---
key: 视频生成/图生视频/QIANSUI+DaSiWaWAN2.2动漫游戏角色图生视频_2008144239636520961.json
name: QIANSUI+DaSiWaWAN2.2动漫游戏角色图生视频_2008144239636520961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008144239636520961.json
hash: bbe301833197da07
coverage: 0.923077
learned_at: 2026-10-15 22:34:06
nodes: [easy cleanGpuUsed, CM_IntToFloat, easy float, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, VAELoader, Qwen3_VQA, Qwen3_VQA, Int, INTConstant, INTConstant, easy int, LoadImage, Qwen3_VQA, easy showAnything, TextInput_, JoinStrings, ShowText|pysssss, CLIPTextEncode, CLIPLoader, UNETLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, Int, PainterI2V, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, RIFE VFI, VHS_VideoCombine, MarkdownNote, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/QIANSUI+DaSiWaWAN2.2动漫游戏角色图生视频_2008144239636520961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008144239636520961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `easy cleanGpuUsed`
- `CM_IntToFloat`
- `easy float`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `VAELoader`
- `Qwen3_VQA`
- `Qwen3_VQA`
- `Int`
- `INTConstant`
- `INTConstant`
- `easy int`
- `LoadImage`
- `Qwen3_VQA`
- `easy showAnything`
- `TextInput_`
- `JoinStrings`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `MarkdownNote`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`easy cleanGpuUsed`、`CM_IntToFloat`、`easy float`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`Qwen3_VQA`、`Int`、`INTConstant`、`easy int`、`LoadImage`、`TextInput_`、`JoinStrings`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`RIFE VFI`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
