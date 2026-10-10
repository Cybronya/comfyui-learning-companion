---
key: 视频生成/文生视频/Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378.json
name: Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378.json
hash: fd7c7725f8daa5ab
coverage: 0.833333
learned_at: 2026-10-10 23:00:33
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, LucyConditionConcatNode, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, ImageConcanate, PrimitiveFloat, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, JWInteger, UNETLoader]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 166656538831002, "steps": 50}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `LucyConditionConcatNode`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `JWInteger`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `166656538831002`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LucyConditionConcatNode`、`VAEEncode`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`ImageConcanate`、`VHS_VideoCombine`、`VHS_LoadVideo`、`JWInteger`、`UNETLoader`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、ImageConcanate

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
