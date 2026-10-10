---
key: 视频生成/文生视频/Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137.json
name: Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137.json
hash: c83ff94c6f9928f3
coverage: 0.888889
learned_at: 2026-10-10 23:00:34
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingSD3, LucyConditionConcatNode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, VHS_VideoCombine, PrimitiveInt, CLIPTextEncode, VHS_VideoCombine, JWInteger, ImageConcanate, VHS_VideoInfo, VHS_LoadVideo, UNETLoader, KSampler]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1043588155084840, "steps": 50}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `LucyConditionConcatNode`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `ImageConcanate`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `1043588155084840`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LucyConditionConcatNode`、`VAEEncode`、`VAEDecode`、`VHS_VideoCombine`、`JWInteger`、`ImageConcanate`、`VHS_VideoInfo`、`VHS_LoadVideo`、`UNETLoader`、`KSampler`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、ImageConcanate

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
