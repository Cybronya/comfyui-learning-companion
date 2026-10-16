---
key: 视频生成/图生视频/最强动漫模型DaSiWa8.1  6秒视频流 浮云1.19_2013170330788958209.json
name: 最强动漫模型DaSiWa8.1  6秒视频流 浮云1.19_2013170330788958209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013170330788958209.json
hash: 2744c4184aba3d69
coverage: 0.405797
learned_at: 2026-10-15 22:34:30
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, VAEDecode, Note, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Int, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, Reroute, Note, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, Reroute, CLIPTextEncode, UNETLoader, PainterI2V, UNETLoader, RIFE VFI, Note, Note, Note, VHS_VideoCombine, LoadImage, ShowText|pysssss, JoinStrings, easy showAnything, Qwen3_VQA, Int, TextInput_, RH_LLMAPI_NODE]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最强动漫模型DaSiWa8.1  6秒视频流 浮云1.19_2013170330788958209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013170330788958209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（69 个）：
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
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `Reroute`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PainterI2V`
- `UNETLoader` ★核心
- `RIFE VFI`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `LoadImage`
- `ShowText|pysssss`
- `JoinStrings`
- `easy showAnything`
- `Qwen3_VQA`
- `Int`
- `TextInput_`
- `RH_LLMAPI_NODE`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **41%**（28/69）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`ModelSamplingSD3`、`VAEDecode`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPLoader`、`UNETLoader`、`PainterI2V`、`RIFE VFI`、`VHS_VideoCombine`、`LoadImage`、`JoinStrings`、`Qwen3_VQA`、`TextInput_`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Int
