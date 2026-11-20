---
key: 平台全量/SD3 Coloring Book page maker + Upscaler_1868860739351101442.json
name: SD3 Coloring Book page maker + Upscaler_1868860739351101442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SD3 Coloring Book page maker + Upscaler_1868860739351101442.json
hash: 955b35672a485a5f
coverage: 0.6875
learned_at: 2026-11-14 00:56:03
nodes: [KSampler, ConditioningSetTimestepRange, ConditioningSetTimestepRange, Reroute, ConditioningZeroOut, ConditioningCombine, CLIPTextEncode, CLIPTextEncode, CR Text Concatenate, CR Text Concatenate, Note, UltimateSDUpscale, EmptySD3LatentImage, ModelSamplingSD3, Text Multiline, Note, Note, Note, SaveImage, Reroute, Reroute, TripleCLIPLoader, CheckpointLoaderSimple, Text Multiline, UpscaleModelLoader, PrimitiveNode, Text Multiline, ShowText|pysssss, RandomPromptGenerator, VAEDecode, PreviewImage, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 4.5, "checkpoint": "sd3_medium_incl_clips_t5xxlfp8.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 208045930549141, "steps": 28}
---

# 平台全量/SD3 Coloring Book page maker + Upscaler_1868860739351101442.json

> 来源文件 `comfyui_library/workflows/平台全量/SD3 Coloring Book page maker + Upscaler_1868860739351101442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `KSampler` ★核心
- `ConditioningSetTimestepRange`
- `ConditioningSetTimestepRange`
- `Reroute`
- `ConditioningZeroOut`
- `ConditioningCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Note`
- `UltimateSDUpscale`
- `EmptySD3LatentImage`
- `ModelSamplingSD3`
- `Text Multiline`
- `Note`
- `Note`
- `Note`
- `SaveImage`
- `Reroute`
- `Reroute`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `Text Multiline`
- `UpscaleModelLoader`
- `PrimitiveNode`
- `Text Multiline`
- `ShowText|pysssss`
- `RandomPromptGenerator`
- `VAEDecode` ★核心
- `PreviewImage`
- `Text Multiline`

## 关键参数

- `seed` = `208045930549141`
- `steps` = `28`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sd3_medium_incl_clips_t5xxlfp8.safetensors`

## 知识

覆盖率 **69%**（22/32）

**有卡**：`KSampler`、`ConditioningSetTimestepRange`、`ConditioningZeroOut`、`ConditioningCombine`、`CLIPTextEncode`、`CR Text Concatenate`、`UltimateSDUpscale`、`EmptySD3LatentImage`、`ModelSamplingSD3`、`Text Multiline`、`SaveImage`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`UpscaleModelLoader`、`RandomPromptGenerator`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、UltimateSDUpscale、UpscaleModelLoader、ConditioningCombine
