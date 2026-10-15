---
key: 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json
name: Lucy Edit视频换装（文本控制）V1.1_2051846229662937090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json
hash: 908e20feaeff7e76
coverage: 0.888889
learned_at: 2026-10-15 22:45:22
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingSD3, LucyConditionConcatNode, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine, PrimitiveInt, JWInteger, PrimitiveFloat, UNETLoader, CLIPTextEncode, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 866943494964420, "steps": 50}
---

# 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `LucyConditionConcatNode`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `JWInteger`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`

## 关键参数

- `seed` = `866943494964420`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LucyConditionConcatNode`、`VAEEncode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`VHS_VideoCombine`、`ImageConcanate`、`JWInteger`、`UNETLoader`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、ImageConcanate
