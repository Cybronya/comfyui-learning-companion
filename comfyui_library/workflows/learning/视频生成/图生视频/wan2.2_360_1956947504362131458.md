---
key: 视频生成/图生视频/wan2.2_360_1956947504362131458.json
name: wan2.2_360_1956947504362131458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2_360_1956947504362131458.json
hash: 43712677bbb8c289
coverage: 0.931034
learned_at: 2026-10-15 22:31:15
nodes: [ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, VAELoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, SaveVideo, easy promptReplace, TextInput_, easy promptConcat, CLIPTextEncode, WanImageToVideo, CreateVideo, ShowText|pysssss, ShowText|pysssss, LoadImage, LoadImage, UNETLoader, VAEDecode, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, TextInput_, RH_Captioner]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2_360_1956947504362131458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956947504362131458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `easy promptReplace`
- `TextInput_`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CreateVideo`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextInput_`
- `RH_Captioner`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`SaveVideo`、`easy promptReplace`、`TextInput_`、`easy promptConcat`、`WanImageToVideo`、`CreateVideo`、`LoadImage`、`VAEDecode`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
