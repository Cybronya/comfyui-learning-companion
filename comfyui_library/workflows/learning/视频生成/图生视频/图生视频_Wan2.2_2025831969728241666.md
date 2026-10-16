---
key: 视频生成/图生视频/图生视频_Wan2.2_2025831969728241666.json
name: 图生视频_Wan2.2_2025831969728241666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2025831969728241666.json
hash: 27814482aebe0e46
coverage: 0.595745
learned_at: 2026-10-15 22:35:13
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SimpleMath+, PathchSageAttentionKJ, Reroute, Reroute, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, VAELoader, Reroute, VAEDecode, FastUnsharpSharpen, easy int, easy int, easy int, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, KSamplerAdvanced, SimpleMath+, PainterI2V, PrimitiveInt, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, CLIPLoader, easy cleanGpuUsed, VHS_VideoCombine, LoaderGGUF, LoadImage, JjkText, LoaderGGUF, KSamplerAdvanced, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/图生视频_Wan2.2_2025831969728241666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025831969728241666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SimpleMath+`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `VAEDecode` ★核心
- `FastUnsharpSharpen`
- `easy int`
- `easy int`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `PainterI2V`
- `PrimitiveInt`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LoaderGGUF`
- `LoadImage`
- `JjkText`
- `LoaderGGUF`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（28/47）

**有卡**：`SimpleMath+`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`VAEDecode`、`FastUnsharpSharpen`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`PainterI2V`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LoaderGGUF`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、FastUnsharpSharpen
