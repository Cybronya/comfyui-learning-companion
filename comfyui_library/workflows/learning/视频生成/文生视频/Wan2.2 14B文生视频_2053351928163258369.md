---
key: 视频生成/文生视频/Wan2.2 14B文生视频_2053351928163258369.json
name: Wan2.2 14B文生视频_2053351928163258369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 14B文生视频_2053351928163258369.json
hash: 90ac9a9388b40de1
coverage: 0.580645
learned_at: 2026-10-15 22:47:08
nodes: [CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, VAEDecode, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, ComfyMathExpression, SaveVideo, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, PrimitiveFloat, PrimitiveFloat]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 14B文生视频_2053351928163258369.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 14B文生视频_2053351928163258369.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（31 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `PrimitiveFloat`
- `PrimitiveFloat`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **58%**（18/31）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`PrimitiveBoolean`、`ComfyMathExpression`、`SaveVideo`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
