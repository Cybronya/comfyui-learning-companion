---
key: 图片生成/图生图/WAN2.2 图生视频_2026950338758053890.json
name: WAN2.2 图生视频_2026950338758053890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2 图生视频_2026950338758053890.json
hash: c7ef119e3c3de079
coverage: 0.921053
learned_at: 2026-10-23 11:27:27
nodes: [CM_IntToFloat, easy float, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, VAELoader, Qwen3_VQA, Qwen3_VQA, Int, INTConstant, INTConstant, easy int, LoadImage, Qwen3_VQA, easy showAnything, TextInput_, JoinStrings, ShowText|pysssss, CLIPTextEncode, CLIPLoader, UNETLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, Int, PainterI2V, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, MarkdownNote, CLIPTextEncode, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/WAN2.2 图生视频_2026950338758053890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2 图生视频_2026950338758053890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
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
- `VHS_VideoCombine`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CM_IntToFloat`、`easy float`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`Qwen3_VQA`、`Int`、`INTConstant`、`easy int`、`LoadImage`、`TextInput_`、`JoinStrings`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
