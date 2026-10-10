---
key: 视频生成/文生视频/Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001.json
name: Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001.json
hash: 143fef22f0590074
coverage: 0.833333
learned_at: 2026-10-10 23:00:35
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingSD3, LucyConditionConcatNode, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, VHS_VideoCombine, PrimitiveInt, VHS_LoadVideo, CLIPTextEncode, PrimitiveFloat, JWInteger, ImageConcanate, VHS_VideoCombine, UNETLoader]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 947617432409471, "steps": 50}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001.json`

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
- `PrimitiveInt`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `JWInteger`
- `ImageConcanate`
- `VHS_VideoCombine`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `947617432409471`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LucyConditionConcatNode`、`VAEEncode`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`JWInteger`、`ImageConcanate`、`UNETLoader`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、ImageConcanate

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
