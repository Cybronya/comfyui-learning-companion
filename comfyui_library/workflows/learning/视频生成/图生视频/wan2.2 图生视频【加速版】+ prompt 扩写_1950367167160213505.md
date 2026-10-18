---
key: 视频生成/图生视频/wan2.2 图生视频【加速版】+ prompt 扩写_1950367167160213505.json
name: wan2.2 图生视频【加速版】+ prompt 扩写_1950367167160213505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频【加速版】+ prompt 扩写_1950367167160213505.json
hash: 6d3b90be9b6dc179
coverage: 0.861111
learned_at: 2026-10-15 22:30:54
nodes: [DF_Integer, RH_Translator, PrimitiveBoolean, Note, LoraLoaderModelOnly, UNETLoader, UNETLoader, VAELoader, easy ifElse, ShowText|pysssss, string_util_StrReplace, RH_LLMAPI_NODE, RH_Translator, ShowText|pysssss, ShowText|pysssss, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, SimpleMath+, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, WanImageToVideo, VAEDecode, easy int, Text Multiline, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, LoadImage, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 图生视频【加速版】+ prompt 扩写_1950367167160213505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950367167160213505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `DF_Integer`
- `RH_Translator`
- `PrimitiveBoolean`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `easy ifElse`
- `ShowText|pysssss`
- `string_util_StrReplace`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `SimpleMath+`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `easy int`
- `Text Multiline`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `Text Multiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`DF_Integer`、`RH_Translator`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`SimpleMath+`、`CLIPVisionEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanImageToVideo`、`VAEDecode`、`easy int`、`Text Multiline`、`VHS_VideoCombine`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
