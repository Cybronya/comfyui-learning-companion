---
key: 视频生成/图生视频/Wan2.2_i2v_Dasiwa__极速版V3_2080499273757712386.json
name: Wan2.2_i2v_Dasiwa__极速版V3_2080499273757712386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2080499273757712386.json
hash: 738532515d2906bd
coverage: 0.666667
learned_at: 2026-10-15 22:42:13
nodes: [VAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, WanImageToVideo, VAEDecode, VHS_VideoCombine, SetNode, ModelSamplingSD3, ModelSamplingSD3, PlaySound|pysssss, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), ModelPatchTorchSettings, ZmlLoraLoaderFive, ZmlLoraLoaderFive, CLIPTextEncode, LoadImage, Note, CLIPTextEncode, easy int, FloatConstant, easy int, easy int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "lora_name": "None", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "strength_clip": "None", "strength_model": 1}
---

# 视频生成/图生视频/Wan2.2_i2v_Dasiwa__极速版V3_2080499273757712386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080499273757712386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（42 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PlaySound|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ModelPatchTorchSettings`
- `ZmlLoraLoaderFive` ★核心
- `ZmlLoraLoaderFive` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Note`
- `CLIPTextEncode` ★核心
- `easy int`
- `FloatConstant`
- `easy int`
- `easy int`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `lora_name` = `None`
- `strength_model` = `1`
- `strength_clip` = `None`

## 知识

覆盖率 **67%**（28/42）

**有卡**：`VAELoader`、`ImageResizeKJv2`、`SimpleMath+`、`WanImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`ModelSamplingSD3`、`PlaySound|pysssss`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`UNETLoader`、`ZmlLoraLoaderFive`、`CLIPTextEncode`、`LoadImage`、`easy int`、`FloatConstant`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ZmlLoraLoaderFive
