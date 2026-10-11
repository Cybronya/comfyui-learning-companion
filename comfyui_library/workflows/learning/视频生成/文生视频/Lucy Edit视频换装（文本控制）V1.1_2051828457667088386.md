---
key: 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json
name: Lucy Edit视频换装（文本控制）V1.1_2051828457667088386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json
hash: 3c2b462414aa16d3
coverage: 0.833333
learned_at: 2026-10-11 19:49:41
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingSD3, LucyConditionConcatNode, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine, PrimitiveInt, JWInteger, PrimitiveFloat, UNETLoader, CLIPTextEncode, VHS_LoadVideo]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 728372684626996, "steps": 50}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json`

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

- `seed` = `728372684626996`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LucyConditionConcatNode`、`VAEEncode`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`ImageConcanate`、`JWInteger`、`UNETLoader`、`VHS_LoadVideo`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、ImageConcanate

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
