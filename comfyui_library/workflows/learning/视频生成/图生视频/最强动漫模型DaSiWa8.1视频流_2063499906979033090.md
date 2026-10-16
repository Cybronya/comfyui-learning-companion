---
key: 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2063499906979033090.json
name: 最强动漫模型DaSiWa8.1视频流_2063499906979033090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063499906979033090.json
hash: 37cc1b64aef5bf53
coverage: 0.394366
learned_at: 2026-10-15 22:39:13
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, Reroute, VAEDecode, Note, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Note, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, TextInput_, Reroute, easy showAnything, JoinStrings, Reroute, CLIPTextEncode, Note, PainterI2V, ShowText|pysssss, UNETLoader, UNETLoader, CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), Note, Note, Qwen3_VQA, KSamplerAdvanced, KSamplerAdvanced, Reroute, Reroute, Int, INTConstant, INTConstant, Int, DuckHideNode, easy cleanGpuUsed, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2063499906979033090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063499906979033090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
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
- `ShowText|pysssss`
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

覆盖率 **39%**（28/71）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`TextInput_`、`JoinStrings`、`PainterI2V`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Qwen3_VQA`、`KSamplerAdvanced`、`Int`、`INTConstant`、`DuckHideNode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Int
