---
key: 视频生成/图生视频/Wan2.2 Remix2 图生视频创作版_2019298877509210114.json
name: Wan2.2 Remix2 图生视频创作版_2019298877509210114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Remix2 图生视频创作版_2019298877509210114.json
hash: 536fba587c6858f8
coverage: 0.885714
learned_at: 2026-10-15 22:35:01
nodes: [PathchSageAttentionKJ, CLIPTextEncode, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, JWInteger, JWInteger, JWInteger, JWInteger, ImpactSwitch, ImpactSwitch, JWInteger, LoadImage, JWInteger, CR Text, ImageResizeKJv2, MathExpression|pysssss, Reroute, JWInteger, PathchSageAttentionKJ, INTConstant, WanImageToVideo, INTConstant, Reroute, VAEDecode, DF_Int_to_Float, VHS_VideoCombine, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix2 图生视频创作版_2019298877509210114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019298877509210114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ImpactSwitch`
- `ImpactSwitch`
- `JWInteger`
- `LoadImage`
- `JWInteger`
- `CR Text`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `Reroute`
- `JWInteger`
- `PathchSageAttentionKJ`
- `INTConstant`
- `WanImageToVideo`
- `INTConstant`
- `Reroute`
- `VAEDecode` ★核心
- `DF_Int_to_Float`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`UNETLoader`、`JWInteger`、`LoadImage`、`CR Text`、`ImageResizeKJv2`、`MathExpression|pysssss`、`INTConstant`、`WanImageToVideo`、`VAEDecode`、`DF_Int_to_Float`、`VHS_VideoCombine`、`VAELoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
