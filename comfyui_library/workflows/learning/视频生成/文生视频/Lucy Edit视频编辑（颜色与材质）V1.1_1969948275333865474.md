---
key: 视频生成/文生视频/Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474.json
name: Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474.json
hash: d39f6e1941bb46d6
coverage: 0.833333
learned_at: 2026-10-10 23:00:36
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, LucyConditionConcatNode, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PrimitiveFloat, VHS_LoadVideo, CLIPTextEncode, CLIPTextEncode, JWInteger, PrimitiveInt, UNETLoader, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 480884841018604, "steps": 50}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474.json`

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
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `480884841018604`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LucyConditionConcatNode`、`VAEEncode`、`KSampler`、`VAEDecode`、`VHS_LoadVideo`、`CLIPTextEncode`、`JWInteger`、`UNETLoader`、`VHS_VideoCombine`、`ImageConcanate`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、ImageConcanate

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
