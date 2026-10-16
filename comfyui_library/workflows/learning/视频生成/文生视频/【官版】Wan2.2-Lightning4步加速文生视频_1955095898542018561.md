---
key: 视频生成/文生视频/【官版】Wan2.2-Lightning4步加速文生视频_1955095898542018561.json
name: 【官版】Wan2.2-Lightning4步加速文生视频_1955095898542018561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1955095898542018561.json
hash: 838c70166ffda95a
coverage: 0.666667
learned_at: 2026-10-15 22:43:39
nodes: [UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, EmptyHunyuanLatentVideo, MathExpression|pysssss, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, UNETLoader, ModelSamplingSD3, VAELoader, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, PrimitiveInt, RH_LLMAPI_NODE, CLIPLoader, ImpactSwitch, ShowText|pysssss, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/【官版】Wan2.2-Lightning4步加速文生视频_1955095898542018561.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1955095898542018561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `ImpactSwitch`
- `ShowText|pysssss`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **67%**（20/30）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`MathExpression|pysssss`、`CLIPTextEncode`、`VAELoader`、`RH_LLMAPI_NODE`、`CLIPLoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
