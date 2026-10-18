---
key: 视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json
name: YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json
hash: 8834742c8a819f04
coverage: 1
learned_at: 2026-10-15 22:36:04
nodes: [VHS_VideoCombine, ImpactInt, LoadImage, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, SimpleMath+, CLIPVisionEncode, easy cleanGpuUsed, KSamplerAdvanced, WanImageToVideo, VAELoader, CLIPVisionLoader, CLIPLoader, UNETLoader, UNETLoader, KSamplerAdvanced, ImageResizeKJv2, Seed (rgthree), easy cleanGpuUsed, VAEDecode, ImpactInt, ImpactInt, CLIPTextEncode, CLIPTextEncode, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038634972579373058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `VHS_VideoCombine`
- `ImpactInt`
- `LoadImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `CLIPVisionEncode`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `Seed (rgthree)`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextInput_`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`VHS_VideoCombine`、`ImpactInt`、`LoadImage`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`SimpleMath+`、`CLIPVisionEncode`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`WanImageToVideo`、`VAELoader`、`CLIPVisionLoader`、`CLIPLoader`、`UNETLoader`、`ImageResizeKJv2`、`Seed (rgthree)`、`VAEDecode`、`CLIPTextEncode`、`TextInput_`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
